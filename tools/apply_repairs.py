#!/usr/bin/env python3
"""Apply CARD/OLD/NEW patch specifications written by the audit swarms.

Each specification is a block:

    CARD: <path relative to the repository>
    BOOK: <citation, ignored>
    OLD:
    ```
    <verbatim text>
    ```
    NEW:
    ```
    <replacement text>
    ```
    WHY: <ignored>

The OLD fenced block is replaced by the NEW fenced block, once. Every OLD must
occur exactly once in its card, otherwise the whole run is refused and nothing is
written: a patch that cannot be applied uniquely is not a repair.

    python3 tools/apply_repairs.py --check .ultramath/*/repairs-*.md
    python3 tools/apply_repairs.py .ultramath/*/repairs-*.md
"""

from __future__ import annotations


import sys
from pathlib import Path

BLOCK = None  # replaced by a line scanner; see parse()


def parse(path: Path) -> list[tuple[str, str, str]]:
    """Read CARD/OLD/NEW blocks with a linear scan.

    Two fence conventions occur in the swarm's files: a ``` fenced block on the
    lines after OLD:/NEW:, and the pipe convention `OLD: |text|` where the pipes
    are the fence. Both are handled.
    """
    lines = path.read_text(encoding="utf-8").split("\n")
    out: list[tuple[str, str, str]] = []
    card: str | None = None
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.startswith("CARD:"):
            card = line.split(":", 1)[1].strip()
            i += 1
            continue
        if card and line.startswith("OLD:"):
            old, j = read_value(lines, i)
            if old is None or j is None:
                i += 1
                continue
            i = j
            while i < n and not lines[i].startswith("NEW:"):
                i += 1
            if i >= n:
                return out
            new, k = read_value(lines, i)
            if new is not None and k is not None:
                out.append((card, old, new))
                i = k
            else:
                i += 1
            continue
        i += 1
    return out


def read_value(lines: list[str], i: int) -> tuple[str | None, int]:
    """Read the value of an OLD:/NEW: line: pipe-fenced inline, or a following fence."""
    rest = lines[i].split(":", 1)[1].strip()
    if rest == "|":
        body: list[str] = []
        j = i + 1
        while j < len(lines) and lines[j].strip() != "|":
            body.append(lines[j])
            j += 1
        if j >= len(lines):
            return None, None
        return "\n".join(body), j + 1
    if rest.startswith("|") and rest.endswith("|") and len(rest) >= 2:
        return rest[1:-1], i + 1
    return read_fence(lines, i + 1)


def read_fence(lines: list[str], i: int) -> tuple[str | None, int | None]:
    """Return the contents of the next ``` fence starting at or after line i."""
    n = len(lines)
    while i < n and not lines[i].startswith("```"):
        i += 1
    if i >= n:
        return None, None
    i += 1
    body: list[str] = []
    while i < n and not lines[i].startswith("```"):
        body.append(lines[i])
        i += 1
    if i >= n:
        return None, None
    return "\n".join(body), i + 1


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    root = Path(__file__).resolve().parent.parent
    patches: list[tuple[Path, str, str, str]] = []
    for spec in files:
        for card, old, new in parse(spec):
            patches.append((spec, card, old, new))
    if not patches:
        print("no patches parsed")
        return 1

    # Refuse the whole batch unless every OLD is unique in its card.
    by_card: dict[str, list[tuple[Path, str, str]]] = {}
    for spec, card, old, new in patches:
        by_card.setdefault(card, []).append((spec, old, new))
    failed = False
    for card, group in by_card.items():
        target = root / card
        if not target.exists():
            print(f"MISSING CARD {card}")
            failed = True
            continue
        text = target.read_text(encoding="utf-8")
        for spec, old, new in group:
            count = text.count(old)
            if count != 1:
                print(f"{card}: OLD occurs {count} times, refusing ({spec.name})")
                failed = True
    if failed:
        print("aborted, nothing written")
        return 1

    for card, group in by_card.items():
        target = root / card
        text = target.read_text(encoding="utf-8")
        for spec, old, new in group:
            text = text.replace(old, new, 1)
        if check_only:
            print(f"would patch {card} ({len(group)})")
        else:
            target.write_text(text, encoding="utf-8")
            print(f"patched {card} ({len(group)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
