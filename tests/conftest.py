"""Shared test scaffolding.

Most tests that inject one card to prove one rule were copying the **real**
corpus to do it -- ~7,200 cards re-parsed through pandoc per test, several times
per suite run, on every commit and every push. The claim under test in those
cases is about the injected card, not about the corpus, so a small fixture
corpus proves it identically and in about a second.

`tests/fixtures/kinds` already exists for exactly this and `test_kind_fixtures`
already uses it; this just makes the pattern shared.

The real corpus is still the right input for two claims, and those keep it:
`test_the_current_corpus_uses_only_mapped_classes` (the totality check is worth
nothing if today's corpus does not satisfy it) and
`test_corpus_layout_is_semantically_inert` (the architectural claim is about this
corpus's layout). Those two are ~85% of the suite's runtime; sharing their builds
is the next real saving and needs its own change.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURE_CORPUS = Path(__file__).resolve().parent / "fixtures" / "kinds"


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
    for name, text in (cards or {}).items():
        (work / "corpus" / name).write_text(text)
    return work


def run_qualc(command: str, root: Path, *, as_json: bool = False) -> subprocess.CompletedProcess[str]:
    argv = [sys.executable, "-m", "qualc", command, "--root", str(root)]
    if as_json:
        argv.append("--json")
    return subprocess.run(argv, capture_output=True, text=True)


def diagnostic_codes(root: Path) -> list[str]:
    """The codes `qualc check` reports, through the real CLI boundary.

    Tests assert on these rather than on stderr wording: a code is the
    diagnostic's identity, the message is presentation. Substring matching on
    the message passes when it is reworded and passes when an unrelated
    diagnostic happens to share a word.
    """
    result = run_qualc("check", root, as_json=True)
    if result.returncode == 0:
        return []
    return [entry["code"] for entry in json.loads(result.stderr)]
