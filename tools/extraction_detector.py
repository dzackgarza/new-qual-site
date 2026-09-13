"""Report problem statements that still contain Unicode mathematics outside LaTeX.

PDF extraction frequently leaves mathematical glyphs in prose rather than converting the
statement to LaTeX.  Those glyphs are a reliable signal that the extraction was pasted into a
card before transcription.  Dollar-delimited inline/display math is intentionally ignored:
Unicode inside an authored LaTeX span is not the defect measured here.

    just extraction-detector
    uv run python tools/extraction_detector.py

The staged gate mode is used by ``test-commit``.  It permits legacy damaged cards to be
modified for unrelated reasons, but refuses a new card with findings or a modified card whose
finding count increases relative to HEAD.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROBLEM_OPEN = re.compile(r"(?m)^::: \{\.problem\}\s*$")
PROBLEM_BLOCK = re.compile(r"(?ms)^::: \{\.problem\}\s*$\n(.*?)^:::\s*$")
DOLLAR_MATH = re.compile(r"\$\$.*?\$\$|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$", re.S)
CARD_ID = re.compile(r"(?m)^id:\s*([^\s]+)\s*$")

# The original extraction audit used Unicode's ``Sm`` (Symbol, Math) category,
# restricted to non-ASCII glyphs.  That criterion is intentionally narrower than
# "all non-ASCII": Greek letters, curly quotes, accented names, and ordinary prose
# are not findings unless a mathematical-symbol glyph is also present.



@dataclass(frozen=True)
class Finding:
    path: Path
    card_id: str
    chars: tuple[str, ...]
    occurrences: int


def is_math_unicode(ch: str) -> bool:
    """Return whether ``ch`` belongs to the extraction audit's math-symbol set."""
    return ord(ch) > 127 and unicodedata.category(ch) == "Sm"


def strip_dollar_math(text: str) -> str:
    """Remove authored ``$...$`` and ``$$...$$`` spans, preserving all other text."""
    return DOLLAR_MATH.sub("", text)


def problem_text(text: str) -> str | None:
    """Return the authored problem block, or ``None`` for a non-problem document."""
    match = PROBLEM_BLOCK.search(text)
    return match.group(1) if match else None


def finding_for_text(path: Path, text: str) -> Finding | None:
    """Return one card-level finding when its problem block has raw Unicode mathematics."""
    body = problem_text(text)
    if body is None:
        return None
    outside = strip_dollar_math(body)
    bad = [ch for ch in outside if is_math_unicode(ch)]
    if not bad:
        return None
    id_match = CARD_ID.search(text)
    card_id = id_match.group(1) if id_match else path.stem
    return Finding(path=path, card_id=card_id, chars=tuple(sorted(set(bad))), occurrences=len(bad))


def iter_card_paths(root: Path) -> Iterable[Path]:
    yield from sorted((root / "corpus" / "collections").rglob("*.md"))


def scan(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_card_paths(root):
        item = finding_for_text(path.relative_to(root), path.read_text(errors="replace"))
        if item is not None:
            findings.append(item)
    return findings


def render(findings: list[Finding]) -> str:
    lines = [
        f"Extraction detector: {len(findings)} problem card(s) contain Unicode mathematics outside dollar-delimited LaTeX.",
    ]
    for item in findings:
        glyphs = "".join(item.chars)
        lines.append(f"{item.path}: {item.card_id}: {glyphs} ({item.occurrences})")
    return "\n".join(lines)


def _git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=root, text=True, capture_output=True, check=check)


def _staged_paths(root: Path) -> list[Path]:
    result = _git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "corpus/collections")
    return [Path(line) for line in result.stdout.splitlines() if line.endswith(".md")]


def _git_text(root: Path, spec: str) -> str | None:
    result = _git(root, "show", spec, check=False)
    return result.stdout if result.returncode == 0 else None


def staged_gate(root: Path) -> int:
    """Reject staged cards that introduce or increase extraction findings."""
    failures: list[str] = []
    for path in _staged_paths(root):
        staged_text = _git_text(root, f":{path.as_posix()}")
        if staged_text is None:
            continue
        staged = finding_for_text(path, staged_text)
        staged_count = staged.occurrences if staged else 0
        head_text = _git_text(root, f"HEAD:{path.as_posix()}")
        head = finding_for_text(path, head_text) if head_text is not None else None
        head_count = head.occurrences if head else 0
        if staged_count > head_count:
            glyphs = "".join(staged.chars) if staged else ""
            failures.append(f"{path}: extraction findings {head_count} -> {staged_count} ({glyphs})")
    if not failures:
        print("extraction-detector: staged cards introduce no new Unicode-mathematics findings")
        return 0
    print("extraction-detector: refusing staged extraction regressions:", file=sys.stderr)
    for line in failures:
        print(f"  {line}", file=sys.stderr)
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--staged-gate", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.staged_gate:
        return staged_gate(root)
    findings = scan(root)
    print(render(findings))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
