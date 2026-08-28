"""Shared test scaffolding.

Most tests that inject one card to prove one rule were copying the **real**
corpus to do it -- ~7,200 cards re-parsed through pandoc per test, several times
per suite run, on every commit and every push. The claim under test in those
cases is about the injected card, not about the corpus, so a small fixture
corpus proves it identically and in about a second.

`tests/fixtures/kinds` already exists for exactly this and `test_kind_fixtures`
already uses it; this just makes the pattern shared.

The real corpus is still the right input for
`test_corpus_layout_is_semantically_inert` (the architectural claim is about this
corpus's layout). That test is most of the suite's runtime; sharing its build is
the next real saving and needs its own change.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from qualc.diagnostics import DiagnosticCode

ROOT = Path(__file__).resolve().parent.parent
FIXTURE_CORPUS = Path(__file__).resolve().parent / "fixtures" / "kinds"


SUBJECTS = (("Algebra", "Algebra"), ("Topology", "Topology"), ("Complex_Analysis", "Complex Analysis"), ("Real_Analysis", "Real Analysis"))


def write_subject_branches(work: Path) -> None:
    """The wiki branches this suite's cards are classified under.

    A subject is a wiki folder -- that is where the area list is read from --
    so a corpus that classifies a card as algebra is a corpus with an Algebra
    branch. Without them every fixture card sits in an unknown area.
    """
    for subject, title in SUBJECTS:
        branch = work / "wiki" / subject
        branch.mkdir(parents=True, exist_ok=True)
        (branch / "index.md").write_text(f"---\ntitle: {title}\norder: 1\n---\n\n# {title}\n")


def fixture_repo(tmp_path: Path, cards: dict[str, str] | None = None) -> Path:
    """A minimal valid repo: the kind fixtures plus whatever `cards` adds.

    No manifests -- the real ones name cards from the real corpus, and a
    publication is a separate decision from what a card must support.
    """
    work = tmp_path / "repo"
    for sub in ("vocabularies", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    shutil.copytree(FIXTURE_CORPUS, work / "corpus")
    (work / "publications").mkdir()
    write_subject_branches(work)
    for name, text in (cards or {}).items():
        (work / "corpus" / name).write_text(text)
    return work


def run_qualc(command: str, root: Path) -> subprocess.CompletedProcess[str]:
    """The CLI as a reader runs it: diagnostics on stderr in human wording."""
    return _run_qualc(command, root)


def run_qualc_json(command: str, root: Path) -> subprocess.CompletedProcess[str]:
    """The CLI with `--json`, so a test can assert on the diagnostic code."""
    return _run_qualc(command, root, "--json")


def _run_qualc(command: str, root: Path, *flags: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-m", "qualc", command, "--root", str(root), *flags], capture_output=True, text=True)


def diagnostic_codes(root: Path) -> list[DiagnosticCode]:
    """The codes `qualc check` reports, through the real CLI boundary.

    Tests assert on the `DiagnosticCode` members rather than on stderr wording:
    the member is the diagnostic's identity, the message is presentation.
    Substring matching on the message passes when it is reworded and passes
    when an unrelated diagnostic happens to share a word.
    """
    result = run_qualc_json("check", root)
    if result.returncode == 0:
        return []
    return [DiagnosticCode(entry["code"]) for entry in json.loads(result.stderr)]
