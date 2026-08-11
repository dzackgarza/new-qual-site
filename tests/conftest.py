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
corpus's layout). `real_corpus_catalog` builds it once per session so they share
one build instead of paying for one each.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
FIXTURE_CORPUS = Path(__file__).resolve().parent / "fixtures" / "kinds"


def fixture_repo(tmp_path: Path, cards: dict[str, str]) -> Path:
    """A minimal valid repo: the kind fixtures plus whatever `cards` adds.

    No manifests -- the real ones name cards from the real corpus, and a
    publication is a separate decision from what a card must support.
    """
    work = tmp_path / "repo"
    for sub in ("vocabularies", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    shutil.copytree(FIXTURE_CORPUS, work / "corpus")
    (work / "publications").mkdir()
    for name, text in cards.items():
        (work / "corpus" / name).write_text(text)
    return work


def run_qualc(command: str, root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "qualc", command, "--root", str(root)],
        capture_output=True,
        text=True,
    )


@pytest.fixture(scope="session")
def real_corpus_catalog(tmp_path_factory: pytest.TempPathFactory) -> Iterator[Path]:
    """One build of the real corpus, shared by every test that needs it.

    Read-only: a test that mutates the tree must build its own, because the
    mutation is what it is testing.
    """
    work = tmp_path_factory.mktemp("real-corpus") / "repo"
    for sub in ("corpus", "vocabularies", "publications", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    (work / "assets").symlink_to(ROOT / "assets", target_is_directory=True)
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    yield work / "build" / "catalog.sqlite"
