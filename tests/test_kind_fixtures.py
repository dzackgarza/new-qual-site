"""WS1's second acceptance criterion: a hand-built card of every kind checks green.

The fixtures live under `tests/fixtures/kinds/` rather than in `corpus/`, because
a card in the corpus is published content and these exist to exercise the schema.
Each is a real, small, correct statement all the same -- a fixture that says
`lorem ipsum` proves the parser runs, not that the kind can hold anything.
"""

from __future__ import annotations

import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import get_args, get_type_hints

import pytest
from conftest import diagnostic_codes, fixture_repo, run_qualc
from qualc.diagnostics import DiagnosticCode
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


def _fixture_for(kind: str) -> Path | None:
    for path in sorted(FIXTURES.glob("*.md")):
        for line in path.read_text().splitlines():
            if line.startswith("kind: ") and line.split(": ", 1)[1].strip() == kind:
                return path
    return None


# Parametrized over the *schema union*, not over the fixture directory. Driving
# it from the directory meant a kind with no fixture was simply never tested,
# and the gap was covered by a separate assertion that the fixture set was
# complete -- which proved something about the test suite rather than about the
# compiler. Now a kind added to the union with no fixture fails as an unparseable
# kind, which is a claim about behaviour.
@pytest.mark.parametrize("kind", sorted(card_kinds()))
def test_every_kind_parses(kind: str) -> None:
    """Each kind individually, so a failure names the kind that broke."""
    from qualc.model import parse_card

    fixture = _fixture_for(kind)
    assert fixture is not None, f"card kind {kind!r} is in the union with no fixture, so nothing exercises it"
    assert parse_card(fixture).card.kind == kind


def test_check_is_green_over_all_fixtures(tmp_path: Path) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "qualc", "check", "--root", str(fixture_repo(tmp_path))],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_unknown_textbook_is_rejected(tmp_path: Path) -> None:
    """`textbook` is an open registry, so it is checked like an institution."""
    work = fixture_repo(tmp_path)
    card = work / "corpus" / "SRC-DUMMIT.md"
    card.write_text(card.read_text().replace("dummit-foote", "dumit-foot"))
    assert diagnostic_codes(work) == [DiagnosticCode.UNKNOWN_TEXTBOOK]


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
    rendered_html = {p.stem for p in (work / "build" / "quarto" / "_site").rglob("*.html")}
    ids = {line.split(": ", 1)[1].strip() for p in FIXTURES.glob("*.md") for line in p.read_text().splitlines() if line.startswith("id: ")}
    assert ids - rendered == {"OCC-INDEXP"}, ids - rendered
    assert ids - rendered_html == {"OCC-INDEXP"}, ids - rendered_html

    problem_page = (work / "build" / "quarto" / "tag" / "PRB-INDEXP.qmd").read_text()
    assert "Problem 3" in problem_page, "the occurrence must render on its problem's page"
    problem_html = (work / "build" / "quarto" / "_site" / "tag" / "PRB-INDEXP.html").read_text()
    assert "Problem 3" in problem_html
    assert "by left translation" in problem_html

    exam_qmd = (work / "build" / "quarto" / "exam" / "SRC-UGA-FIX.qmd").read_text()
    assert "Problem 3" not in exam_qmd
    textbook_qmd = (work / "build" / "quarto" / "exam" / "SRC-DUMMIT.qmd").read_text()
    assert "0 problems." in textbook_qmd


def test_collection_page_is_the_problems_list(tmp_path: Path) -> None:
    """An exam page is the collection's `problems:` list, in list order.

    An empty list publishes empty. Filling it does not pull locators off
    occurrence cards.
    """
    work = fixture_repo(tmp_path)
    (work / "corpus" / "P-INDEXP.md").write_text(
        (work / "corpus" / "PRB-INDEXP.md")
        .read_text()
        .replace("PRB-INDEXP", "P-INDEXP")
        .replace("solved: true", "solved: false")
    )
    exam = work / "corpus" / "SRC-UGA-FIX.md"
    exam.write_text(
        exam.read_text().replace(
            "  area: algebra\n  date:\n",
            "  area: algebra\n  problems:\n  - P-INDEXP\n  date:\n",
        )
    )
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    exam_qmd = (work / "build" / "quarto" / "exam" / "SRC-UGA-FIX.qmd").read_text()
    assert "P-INDEXP" in exam_qmd
    assert "Problem 3" not in exam_qmd
    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    assert [
        row[0]
        for row in con.execute(
            "select problem_id from collection_problems where collection_id='SRC-UGA-FIX' order by ordinal"
        )
    ] == ["P-INDEXP"]
    assert list(
        con.execute("select problem_id from collection_problems where collection_id='SRC-DUMMIT'")
    ) == []


def test_each_source_variant_lands_in_its_own_table(tmp_path: Path) -> None:
    """The collection payload is a discriminated union and the catalog mirrors it
    rather than flattening it into one row with columns null for two kinds out
    of three. This proves the catalog: an exam reaches `exam_sources`, a
    textbook `textbook_sources`, an artifact `artifact_sources`, and each
    reaches exactly one of them.

    This replaces an assertion that the fixture set covered all three variant
    names, which restated the schema back to itself and proved nothing about
    where a variant ends up.
    """
    work = fixture_repo(tmp_path)
    assert run_qualc("build", work).returncode == 0
    con = sqlite3.connect(work / "build" / "catalog.sqlite")

    tables = {
        "university-exam": "exam_sources",
        "textbook": "textbook_sources",
        "contributed-artifact": "artifact_sources",
    }
    for variant, table in tables.items():
        ids = {i for (i,) in con.execute("select id from sources where source_kind = ?", (variant,))}
        assert ids, f"no fixture exercises the {variant!r} collection variant"
        projected = {i for (i,) in con.execute(f"select id from {table}")}
        assert ids == projected, f"{variant} rows must project into {table}"
        for other in set(tables.values()) - {table}:
            spilled = ids & {i for (i,) in con.execute(f"select id from {other}")}
            assert not spilled, f"{variant} must not also appear in {other}: {spilled}"
