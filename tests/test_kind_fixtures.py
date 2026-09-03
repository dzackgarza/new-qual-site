"""WS1's second acceptance criterion: a hand-built card of every kind checks green.

The fixtures live under `tests/fixtures/kinds/` rather than in `corpus/`, because
a card in the corpus is published content and these exist to exercise the schema.
Each is a real, small, correct statement all the same -- a fixture that says
`lorem ipsum` proves the parser runs, not that the kind can hold anything.
"""

from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import get_args, get_type_hints

import pytest
from conftest import diagnostic_codes, fixture_repo, run_qualc
from qualc.diagnostics import DiagnosticCode
from qualc.model import AuditEvent, Card, CollectionCard, CompilationSource, ProblemCard

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


def test_standalone_solution_kind_is_rejected(tmp_path: Path) -> None:
    """A solution is a section of a problem, never its own card."""
    from qualc.model import parse_card

    path = tmp_path / "S-OLD.md"
    path.write_text((FIXTURES / "PRB-INDEXP.md").read_text().replace("id: PRB-INDEXP", "id: S-OLD", 1).replace("kind: problem", "kind: solution", 1))
    with pytest.raises(ValueError):
        parse_card(path)


def test_solves_relation_is_rejected(tmp_path: Path) -> None:
    """There is no relation-based second home for a solution."""
    from qualc.model import parse_card

    path = tmp_path / "PRB-INDEXP.md"
    path.write_text((FIXTURES / "PRB-INDEXP.md").read_text().replace("relations: []", "relations:\n- kind: solves\n  target: EXE-CENTER", 1))
    with pytest.raises(ValueError):
        parse_card(path)


def test_standalone_hint_kind_is_rejected(tmp_path: Path) -> None:
    """A hint is a section of a problem, never its own card."""
    from qualc.model import parse_card

    path = tmp_path / "H-OLD.md"
    path.write_text((FIXTURES / "PRB-INDEXP.md").read_text().replace("id: PRB-INDEXP", "id: H-OLD", 1).replace("kind: problem", "kind: hint", 1))
    with pytest.raises(ValueError):
        parse_card(path)


def test_exercise_is_not_a_card_kind_and_e_ids_remain_valid_problem_ids(tmp_path: Path) -> None:
    """Exercise is source appearance vocabulary, not an intrinsic problem kind."""
    from qualc.model import parse_card

    e_card = parse_card(FIXTURES / "EXE-CENTER.md")
    assert isinstance(e_card.card, ProblemCard)
    assert e_card.card.id == "EXE-CENTER"
    assert e_card.card.kind == "problem"
    assert e_card.sections[0][0] == "problem"

    legacy = tmp_path / "E-LEGACY.md"
    legacy.write_text((FIXTURES / "EXE-CENTER.md").read_text().replace("kind: problem", "kind: exercise", 1))
    with pytest.raises(ValueError):
        parse_card(legacy)


def test_hints_at_relation_is_rejected(tmp_path: Path) -> None:
    """There is no relation-based second home for a hint."""
    from qualc.model import parse_card

    path = tmp_path / "PRB-INDEXP.md"
    path.write_text((FIXTURES / "PRB-INDEXP.md").read_text().replace("relations: []", "relations:\n- kind: hints-at\n  target: EXE-CENTER", 1))
    with pytest.raises(ValueError):
        parse_card(path)


def test_collection_completion_defaults_to_complete() -> None:
    from qualc.model import parse_card

    card = parse_card(FIXTURES / "SRC-DUMMIT.md").card
    assert isinstance(card, CollectionCard)
    assert card.completion == "complete"
    assert card.provenance == []


def test_incomplete_completion_parses(tmp_path: Path) -> None:
    from qualc.model import parse_card

    path = tmp_path / "SRC-DUMMIT.md"
    path.write_text((FIXTURES / "SRC-DUMMIT.md").read_text().replace("review: draft\n", "review: draft\ncompletion: incomplete\n", 1))
    card = parse_card(path).card
    assert isinstance(card, CollectionCard)
    assert card.completion == "incomplete"


def test_unknown_completion_is_rejected(tmp_path: Path) -> None:
    from qualc.model import parse_card

    path = tmp_path / "SRC-DUMMIT.md"
    path.write_text((FIXTURES / "SRC-DUMMIT.md").read_text().replace("review: draft\n", "review: draft\ncompletion: todo\n", 1))
    with pytest.raises(ValueError):
        parse_card(path)


def test_collection_provenance_parses(tmp_path: Path) -> None:
    from qualc.model import parse_card

    path = tmp_path / "SRC-DUMMIT.md"
    path.write_text(
        (FIXTURES / "SRC-DUMMIT.md")
        .read_text()
        .replace(
            "review: draft\n",
            "review: draft\nprovenance:\n  - https://example.org/source.pdf\n  - assets/attachments/notes.pdf\n",
            1,
        )
    )
    card = parse_card(path).card
    assert isinstance(card, CollectionCard)
    assert card.provenance == [
        "https://example.org/source.pdf",
        "assets/attachments/notes.pdf",
    ]


def test_empty_provenance_href_is_rejected(tmp_path: Path) -> None:
    from qualc.model import parse_card

    path = tmp_path / "SRC-DUMMIT.md"
    path.write_text((FIXTURES / "SRC-DUMMIT.md").read_text().replace("review: draft\n", 'review: draft\nprovenance:\n  - ""\n', 1))
    with pytest.raises(ValueError):
        parse_card(path)


def test_compilation_sections_are_the_collection_listing_and_central_problem_index(tmp_path: Path) -> None:
    from qualc.model import parse_card

    work = fixture_repo(tmp_path)
    (work / "corpus" / "P-INDEXP.md").write_text((work / "corpus" / "PRB-INDEXP.md").read_text().replace("PRB-INDEXP", "P-INDEXP"))
    card = work / "corpus" / "SRC-NEILNOTES.md"
    card.write_text(
        card.read_text().replace(
            "    term: fall\n",
            "    term: fall\n  sections:\n  - name: Day 1\n    problems:\n    - P-INDEXP\n",
        )
    )
    parsed = parse_card(card).card
    assert isinstance(parsed, CollectionCard)
    assert isinstance(parsed.source, CompilationSource)
    assert parsed.source.sections[0].name == "Day 1"
    assert parsed.source.listed_problem_ids() == ["P-INDEXP"]

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    source_qmd = (work / "build" / "quarto" / "source" / "SRC-NEILNOTES.qmd").read_text()
    assert "Day 1" in source_qmd
    assert "P-INDEXP" in source_qmd
    assert "problems.html?collection=SRC-NEILNOTES" in source_qmd

    index = json.loads((work / "build" / "quarto" / "_site" / "collection-problems.json").read_text())
    [item] = index["SRC-NEILNOTES"]["items"]
    assert item["id"] == "P-INDEXP"
    assert item["meta"]["collection_section"] == "Day 1"
    assert item["meta"]["collection_locator"] == "Problem 1"

    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    rows = con.execute("select section_name, problem_id from collection_problems where collection_id='SRC-NEILNOTES' order by section_ordinal, ordinal").fetchall()
    assert rows == [("Day 1", "P-INDEXP")]


def test_compilation_section_may_list_a_collection_without_putting_it_in_problem_results(tmp_path: Path) -> None:
    from qualc.model import parse_card

    work = fixture_repo(tmp_path)
    card = work / "corpus" / "SRC-NEILNOTES.md"
    card.write_text(
        card.read_text().replace(
            "    term: fall\n",
            "    term: fall\n  sections:\n  - name: Day 1\n    problems:\n    - SRC-UGA-FIX\n",
        )
    )
    parsed = parse_card(card).card
    assert isinstance(parsed, CollectionCard)
    assert isinstance(parsed.source, CompilationSource)
    assert [e.id for e in parsed.source.sections[0].problems] == ["SRC-UGA-FIX"]
    assert parsed.source.listed_problem_ids() == []

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    source_qmd = (work / "build" / "quarto" / "source" / "SRC-NEILNOTES.qmd").read_text()
    assert "Day 1" in source_qmd
    assert "SRC-UGA-FIX" in source_qmd
    index = json.loads((work / "build" / "quarto" / "_site" / "collection-problems.json").read_text())
    assert "SRC-NEILNOTES" not in index

    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    rows = con.execute("select section_name, problem_id from collection_problems where collection_id='SRC-NEILNOTES'").fetchall()
    assert rows == [("Day 1", "SRC-UGA-FIX")]


def test_compilation_rejects_problems_and_sections(tmp_path: Path) -> None:
    from qualc.model import parse_card

    path = tmp_path / "SRC-NEILNOTES.md"
    text = (
        (FIXTURES / "SRC-NEILNOTES.md")
        .read_text()
        .replace(
            "    term: fall\n",
            "    term: fall\n  problems:\n  - PRB-INDEXP\n  sections:\n  - name: Day 1\n    problems:\n    - PRB-INDEXP\n",
        )
    )
    path.write_text(text)
    with pytest.raises(ValueError):
        parse_card(path)


def test_compilation_section_rejects_an_untyped_id(tmp_path: Path) -> None:
    from qualc.model import parse_card

    path = tmp_path / "SRC-NEILNOTES.md"
    text = (
        (FIXTURES / "SRC-NEILNOTES.md")
        .read_text()
        .replace(
            "    term: fall\n",
            "    term: fall\n  sections:\n  - name: Day 1\n    problems:\n    - NOT-AN-ID\n",
        )
    )
    path.write_text(text)
    with pytest.raises(ValueError, match="not a problem or collection id"):
        parse_card(path)


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

    Appearances on a problem page come from collection `problems:` / `sections:`
    lists.
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
    assert ids <= rendered, ids - rendered
    assert ids <= rendered_html, ids - rendered_html

    problem_html = (work / "build" / "quarto" / "_site" / "tag" / "PRB-INDEXP.html").read_text()
    assert "by left translation" in problem_html

    textbook_qmd = (work / "build" / "quarto" / "source" / "SRC-DUMMIT.qmd").read_text()
    assert "0 problems." in textbook_qmd


def test_collection_page_lists_problems_and_links_the_central_browser(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    (work / "corpus" / "P-INDEXP.md").write_text((work / "corpus" / "PRB-INDEXP.md").read_text().replace("PRB-INDEXP", "P-INDEXP"))
    exam = work / "corpus" / "SRC-UGA-FIX.md"
    exam.write_text(
        exam.read_text().replace(
            "  area: algebra\n  date:\n",
            "  area: algebra\n  problems:\n  - id: P-INDEXP\n    comment: Problem 3\n  date:\n",
        )
    )
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    exam_qmd = (work / "build" / "quarto" / "exam" / "SRC-UGA-FIX.qmd").read_text()
    assert "P-INDEXP" in exam_qmd
    assert "Problem 3" in exam_qmd
    assert "problems.html?collection=SRC-UGA-FIX" in exam_qmd

    index = json.loads((work / "build" / "quarto" / "_site" / "collection-problems.json").read_text())
    assert [item["id"] for item in index["SRC-UGA-FIX"]["items"]] == ["P-INDEXP"]

    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    assert [row[0] for row in con.execute("select problem_id from collection_problems where collection_id='SRC-UGA-FIX' order by ordinal")] == ["P-INDEXP"]
    assert list(con.execute("select problem_id from collection_problems where collection_id='SRC-DUMMIT'")) == []


def test_collection_page_renders_provenance_links(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    local_pdf = work / "assets" / "attachments" / "fixture-paper.pdf"
    local_pdf.parent.mkdir(parents=True, exist_ok=True)
    local_pdf.write_bytes(b"%PDF-1.4\n%%EOF\n")
    local_extraction = local_pdf.parent / "extracted" / "fixture-paper.md"
    local_extraction.parent.mkdir()
    local_extraction.write_text("A checked-in extraction of the fixture paper.\n")
    exam = work / "corpus" / "SRC-UGA-FIX.md"
    provenance = (
        "review: draft\n"
        "provenance:\n"
        "  - https://www.math.uga.edu/past-qualifying-exams-1\n"
        "  - https://www.math.uga.edu/sites/default/files/inline-files/8000e.pdf\n"
        "  - assets/attachments/fixture-paper.pdf\n"
    )
    exam.write_text(
        exam.read_text().replace(
            "review: draft\n",
            provenance,
            1,
        )
    )
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    exam_qmd = (work / "build" / "quarto" / "exam" / "SRC-UGA-FIX.qmd").read_text()
    body = exam_qmd.split("---\n", 2)[2]
    assert "Provenance" not in body
    assert "assets/attachments/fixture-paper.pdf" not in body

    exam_html = (work / "build" / "quarto" / "_site" / "exam" / "SRC-UGA-FIX.html").read_text()
    assert "<dt>Area</dt><dd>Algebra</dd>" in exam_html
    assert "<dt>Topics</dt><dd>Groups</dd>" in exam_html
    assert "<dt>Status</dt><dd>draft</dd>" in exam_html
    assert "<dt>Source</dt>" in exam_html
    assert 'href="https://www.math.uga.edu/past-qualifying-exams-1" aria-label="Source"' in exam_html
    assert 'href="https://www.math.uga.edu/sites/default/files/inline-files/8000e.pdf" aria-label="PDF source"' in exam_html
    assert 'href="../assets/attachments/fixture-paper.pdf" aria-label="PDF source"' in exam_html
    assert 'href="../assets/attachments/extracted/fixture-paper.md" aria-label="Markdown extraction"' in exam_html
    assert ">assets/attachments/fixture-paper.pdf<" not in exam_html
    published = work / "build" / "quarto" / "_site" / "assets" / "attachments"
    assert (published / "fixture-paper.pdf").samefile(local_pdf)
    assert (published / "extracted" / "fixture-paper.md").samefile(local_extraction)
    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    assert [row[0] for row in con.execute("select href from collection_provenance where collection_id='SRC-UGA-FIX' order by ordinal")] == [
        "https://www.math.uga.edu/past-qualifying-exams-1",
        "https://www.math.uga.edu/sites/default/files/inline-files/8000e.pdf",
        "assets/attachments/fixture-paper.pdf",
    ]
    assert list(con.execute("select href from collection_provenance where collection_id='SRC-DUMMIT'")) == []


def test_each_source_variant_lands_in_its_own_table(tmp_path: Path) -> None:
    """The collection source is a discriminated union and the catalog mirrors it
    rather than flattening it into one row with columns null for other kinds.
    """
    work = fixture_repo(tmp_path)
    assert run_qualc("build", work).returncode == 0
    con = sqlite3.connect(work / "build" / "catalog.sqlite")

    tables = {
        "university-exam": "exam_sources",
        "textbook": "textbook_sources",
        "homework": "homework_sources",
        "compilation": "compilation_sources",
    }
    for variant, table in tables.items():
        ids = {i for (i,) in con.execute("select id from sources where source_kind = ?", (variant,))}
        assert ids, f"no fixture exercises the {variant!r} collection variant"
        projected = {i for (i,) in con.execute(f"select id from {table}")}
        assert ids == projected, f"{variant} rows must project into {table}"
        for other in set(tables.values()) - {table}:
            spilled = ids & {i for (i,) in con.execute(f"select id from {other}")}
            assert not spilled, f"{variant} must not also appear in {other}: {spilled}"


# The audit block: who wrote the solution, who checked the statement against the
# original source, who reviewed the solution, and when each of those happened.
AUDIT_BLOCK = """review: draft
audit:
- event: solution-written
  by: dzackgarza
  date: 2026-08-16
- event: source-checked
  by: dzackgarza
  date: 2026-08-20
  note: checked against the UGA prelim paper
- event: solution-reviewed
  by: dzackgarza
  date: 2026-08-24
- event: solution-reviewed
  by: neil
  date: 2026-08-27
"""


@pytest.mark.parametrize("fixture", ["PRB-INDEXP.md", "EXE-CENTER.md"])
def test_audit_rounds_parse_in_authored_order(tmp_path: Path, fixture: str) -> None:
    """Problem cards carry the audit list regardless of their historical ID prefix.

    A repeated event kind is kept rather than collapsed: two
    `solution-reviewed` rounds stay two.

    The dates come back as `datetime.date`, which is what makes them sortable
    and what makes a mistyped day a build failure.
    """
    from qualc.model import parse_card

    path = tmp_path / fixture
    path.write_text((FIXTURES / fixture).read_text().replace("review: draft\n", AUDIT_BLOCK, 1))
    card = parse_card(path).card
    assert isinstance(card, ProblemCard)
    assert card.audit == [
        AuditEvent(event="solution-written", by="dzackgarza", date=date(2026, 8, 16)),
        AuditEvent(event="source-checked", by="dzackgarza", date=date(2026, 8, 20), note="checked against the UGA prelim paper"),
        AuditEvent(event="solution-reviewed", by="dzackgarza", date=date(2026, 8, 24)),
        AuditEvent(event="solution-reviewed", by="neil", date=date(2026, 8, 27)),
    ]


def test_unknown_audit_event_is_rejected(tmp_path: Path) -> None:
    """The three events are a closed vocabulary. A fourth spelling is a typo,
    and a typo that validates is metadata nobody can query."""
    from qualc.model import parse_card

    path = tmp_path / "PRB-INDEXP.md"
    path.write_text(
        (FIXTURES / "PRB-INDEXP.md")
        .read_text()
        .replace(
            "review: draft\n",
            "review: draft\naudit:\n- event: solution-approved\n  by: dzackgarza\n  date: 2026-08-16\n",
            1,
        )
    )
    with pytest.raises(ValueError):
        parse_card(path)


def test_day_first_audit_date_is_rejected(tmp_path: Path) -> None:
    """`27-08-2026` is the habitual non-ISO spelling, and YAML hands it over as
    a plain string rather than a date. A string field would store it and sort it
    beside 2027; the typed field fails the build. This is the claim the
    `datetime.date` annotation exists to make -- YAML itself already rejects an
    impossible day such as February 30th, so that is not this schema's work.
    """
    from qualc.model import parse_card

    path = tmp_path / "PRB-INDEXP.md"
    path.write_text(
        (FIXTURES / "PRB-INDEXP.md")
        .read_text()
        .replace(
            "review: draft\n",
            "review: draft\naudit:\n- event: solution-written\n  by: dzackgarza\n  date: 27-08-2026\n",
            1,
        )
    )
    with pytest.raises(ValueError):
        parse_card(path)


def test_prompts_parse_in_authored_order(tmp_path: Path) -> None:
    """Several questions may front one card, so the mathematics is stored once
    and asked for in more than one way. Order is the author's."""
    from qualc.model import parse_card

    path = tmp_path / "DEF-PGROUP.md"
    path.write_text(
        (FIXTURES / "DEF-PGROUP.md")
        .read_text()
        .replace(
            "classification:\n",
            "prompts:\n- What is a normal family?\n- Give the Montel criterion.\nclassification:\n",
            1,
        )
    )
    assert parse_card(path).card.prompts == [
        "What is a normal family?",
        "Give the Montel criterion.",
    ]


def test_card_without_prompts_is_never_asked() -> None:
    """Empty, not a default and not the title: a card with no authored question
    has nothing to front it, and the title is a name rather than a question."""
    from qualc.model import parse_card

    assert parse_card(FIXTURES / "DEF-PGROUP.md").card.prompts == []


APPEARANCE = "    term: spring\n  problems:\n  - id: P-INDEXP\n    comment: {comment}\n  - E-CENTER\n"


def test_appearance_comment_belongs_to_the_collection(tmp_path: Path) -> None:
    """A comment says where the problem sits in THIS source, so one problem
    listed by two collections carries a different comment on each. That is the
    thing a field on the problem card could not express: it would have to pick
    one of the two numbers and delete the other appearance.

    The second entry is a bare id, which stays legal and arrives with no
    comment -- most appearances have nothing to add beyond what the collection
    already says, and are not forced into a mapping to say it.
    """
    work = fixture_repo(tmp_path)
    corpus = work / "corpus"
    (corpus / "P-INDEXP.md").write_text((corpus / "PRB-INDEXP.md").read_text().replace("PRB-INDEXP", "P-INDEXP"))
    (corpus / "E-CENTER.md").write_text((corpus / "EXE-CENTER.md").read_text().replace("EXE-CENTER", "E-CENTER"))
    for name, comment in (("SRC-UGA-FIX.md", "Problem 6"), ("SRC-HW.md", "Problem 5")):
        card = corpus / name
        card.write_text(card.read_text().replace("    term: spring\n", APPEARANCE.format(comment=comment), 1))

    assert run_qualc("build", work).returncode == 0
    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    assert con.execute("select collection_id, problem_id, comment from collection_problems order by collection_id, ordinal").fetchall() == [
        ("SRC-HW", "P-INDEXP", "Problem 5"),
        ("SRC-HW", "E-CENTER", None),
        ("SRC-UGA-FIX", "P-INDEXP", "Problem 6"),
        ("SRC-UGA-FIX", "E-CENTER", None),
    ]

    # Both numbers reach the reader, each next to the source that uses it. An
    # entry with no comment falls back on the only locator its collection has,
    # which is the position it was listed in.
    appearances = (work / "build" / "quarto" / "_site" / "tag" / "P-INDEXP.html").read_text()
    assert "Algebra homework 3, Spring 2020, Problem 5" in appearances
    assert "UGA Algebra qualifying exam, Spring 2019, Problem 6" in appearances
    uncommented = (work / "build" / "quarto" / "_site" / "tag" / "E-CENTER.html").read_text()
    assert "Algebra homework 3, Spring 2020, problem 2" in uncommented
    assert '<div class="card-statement">' in uncommented
    assert "<dt>Area</dt>" in uncommented
    assert "<dt>Topics</dt>" in uncommented
    assert "<dt>Status</dt>" in uncommented


def test_textbook_source_is_not_exam_metadata_and_stays_separate_from_guide_appearances(tmp_path: Path) -> None:
    """A textbook date belongs to the source, not to the problem's exam facts.

    The same problem may also be deliberately placed in a study guide. Those
    two edges answer different questions and therefore render in separate
    relation groups: where the problem came from, and where the site uses it.
    """
    work = fixture_repo(tmp_path)
    corpus = work / "corpus"
    (corpus / "P-INDEXP.md").write_text((corpus / "PRB-INDEXP.md").read_text().replace("PRB-INDEXP", "P-INDEXP"))
    textbook = work / "corpus" / "SRC-DUMMIT.md"
    textbook.write_text(
        textbook.read_text().replace(
            "    year: 2004\n",
            "    year: 2004\n  sections:\n  - name: '4.1'\n    problems:\n    - id: P-INDEXP\n      comment: Exercise 4.1.7\n",
            1,
        )
    )
    (work / "publications" / "algebra-guide.yaml").write_text(
        """schema: qual/publication@2
id: GUIDE-ALGEBRA
kind: study-guide
title: Algebra
lede: A short algebra guide.
sections:
- slug: groups
  title: Groups
  parent: GUIDE-ALGEBRA
  lede: The group-theory section.
  items:
  - ref: P-INDEXP
"""
    )

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "tag" / "P-INDEXP.html").read_text()
    assert "<dt>Seen at</dt>" not in page
    assert "<dt>Years</dt>" not in page
    assert 'data-relation-group="source-collections"' in page
    assert "Dummit and Foote, Abstract Algebra, Exercise 4.1.7" in page
    assert 'data-relation-group="guide-appearances"' in page
    assert ">Groups</a>" in page


def test_commented_entry_must_still_be_an_id(tmp_path: Path) -> None:
    """A comment does not buy an entry out of the id check. Prose in the id
    position fails the build rather than entering the catalog as a problem."""
    from qualc.model import parse_card

    path = tmp_path / "SRC-UGA-FIX.md"
    path.write_text((FIXTURES / "SRC-UGA-FIX.md").read_text().replace("    term: spring\n", "    term: spring\n  problems:\n  - id: Problem 6\n    comment: P-INDEXP\n", 1))
    with pytest.raises(ValueError):
        parse_card(path)


def test_commented_entry_may_be_a_nested_collection(tmp_path: Path) -> None:
    """A section entry that is itself a collection keeps working, comment and
    all: the workshop packet whose day 1 *is* another exam paper."""
    from qualc.model import parse_card

    path = tmp_path / "SRC-NEILNOTES.md"
    path.write_text(
        (FIXTURES / "SRC-NEILNOTES.md")
        .read_text()
        .replace(
            "    term: fall\n",
            "    term: fall\n  sections:\n  - name: Day 1\n    problems:\n    - id: SRC-UGA-FIX\n      comment: the Spring 2019 paper, whole\n",
            1,
        )
    )
    parsed = parse_card(path).card
    assert isinstance(parsed, CollectionCard)
    assert isinstance(parsed.source, CompilationSource)
    assert [(e.id, e.comment) for e in parsed.source.sections[0].problems] == [("SRC-UGA-FIX", "the Spring 2019 paper, whole")]
    assert parsed.source.listed_problem_ids() == []
