"""WS1's second acceptance criterion: a hand-built card of every kind checks green.

The fixtures live under `tests/fixtures/kinds/` rather than in `corpus/`, because
a card in the corpus is published content and these exist to exercise the schema.
Each is a real, small, correct statement all the same -- a fixture that says
`lorem ipsum` proves the parser runs, not that the kind can hold anything.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import get_args, get_type_hints

import pytest
from qualc.model import Card

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "kinds"


def card_kinds() -> set[str]:
    """Every `kind` literal in the discriminated union.

    Read off the union itself rather than a list kept here, so the fixture set
    is checked against the schema and not against a copy of it.
    """
    union, _discriminator = get_args(Card)
    return {get_args(get_type_hints(variant)["kind"])[0] for variant in get_args(union)}


def fixture_repo(tmp_path: Path) -> Path:
    work = tmp_path / "repo"
    for sub in ("vocabularies", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    shutil.copytree(FIXTURES, work / "corpus")
    # No manifests: the real ones name cards from the real corpus, and a guide
    # is a publication decision, not part of what a card kind must support.
    (work / "publications").mkdir()
    return work


def test_every_kind_has_a_fixture() -> None:
    """A kind added to the union without a fixture fails here, not silently."""
    covered = {line.split(": ", 1)[1].strip() for p in FIXTURES.glob("*.md") for line in p.read_text().splitlines() if line.startswith("kind: ")}
    assert card_kinds() - covered == set()


def test_every_source_variant_has_a_fixture() -> None:
    variants = {line.split(": ", 1)[1].strip() for p in FIXTURES.glob("*.md") for line in p.read_text().splitlines() if line.strip().startswith("source_kind: ")}
    assert variants == {"university-exam", "textbook", "contributed-artifact"}, variants


@pytest.mark.parametrize("fixture", sorted(FIXTURES.glob("*.md")), ids=lambda p: p.stem)
def test_fixture_parses(fixture: Path) -> None:
    """Each card individually, so a failure names the kind that broke."""
    from qualc.model import parse_card

    parse_card(fixture)


def test_check_is_green_over_all_fixtures(tmp_path: Path) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "qualc", "check", "--root", str(fixture_repo(tmp_path))],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_unknown_textbook_is_rejected(tmp_path: Path) -> None:
    """`textbook` is an open registry, so it is checked like an institution."""
    work = fixture_repo(tmp_path)
    card = work / "corpus" / "SRC-DUMMIT.md"
    card.write_text(card.read_text().replace("dummit-foote", "dumit-foot"))
    result = subprocess.run(
        [sys.executable, "-m", "qualc", "check", "--root", str(work)],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "unknown textbook" in result.stderr


def test_every_card_reaches_a_page(tmp_path: Path) -> None:
    """A kind that indexes but never renders is data the reader cannot get to.

    Occurrences are the one deliberate exception: they render inline on the
    problem they instantiate, so they are checked for there instead.
    """
    work = fixture_repo(tmp_path)
    subprocess.run(
        [sys.executable, "-m", "qualc", "build", "--root", str(work)],
        check=True,
        capture_output=True,
    )
    rendered = {p.stem for p in (work / "build" / "quarto").rglob("*.qmd")}
    ids = {line.split(": ", 1)[1].strip() for p in FIXTURES.glob("*.md") for line in p.read_text().splitlines() if line.startswith("id: ")}
    assert ids - rendered == {"OCC-INDEXP"}, ids - rendered

    problem_page = (work / "build" / "quarto" / "tag" / "PRB-INDEXP.qmd").read_text()
    assert "Problem 3" in problem_page, "the occurrence must render on its problem's page"
