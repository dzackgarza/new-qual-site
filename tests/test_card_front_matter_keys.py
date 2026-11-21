"""A card whose front matter YAML or Pandoc would read differently is unreadable.

YAML's safe loader keeps the last of two equal keys. Two writers appending to
one card produced two `audit:` lists, and single-card validation reported the
card sound while one list was discarded.
"""

from __future__ import annotations

from pathlib import Path

from conftest import diagnostic_codes, fixture_repo
from qualc.diagnostics import DiagnosticCode

REPEATED_TITLE = """---
schema: qual/card@1
id: P-TWOTITLES
kind: problem
title: The first title
title: The second title
classification:
  areas: [algebra]
  topics: [Groups]
relations: []
review: draft
---

::: problem
Show that a group of prime order is cyclic.
:::
"""


def test_a_repeated_front_matter_key_makes_the_card_unreadable(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"P-TWOTITLES.md": REPEATED_TITLE})

    assert DiagnosticCode.CARD_UNREADABLE in diagnostic_codes(work)


GLUED_CLOSE = REPEATED_TITLE.replace("title: The first title\ntitle: The second title\n", "title: A prime-order group\n").replace("review: draft\n---\n", "review: draft---\n")


def test_extraction_residue_makes_the_card_unreadable(tmp_path: Path) -> None:
    card = REPEATED_TITLE.replace("title: The first title\ntitle: The second title\n", "title: A prime-order group\n")
    for residue in ("an automorphism \x00 of a group", "a group with elements g<sub>j</sub>"):
        work = fixture_repo(tmp_path / str(len(residue)), {"P-TWOTITLES.md": card.replace("a group", residue, 1)})

        assert DiagnosticCode.CARD_UNREADABLE in diagnostic_codes(work)


def test_a_closing_delimiter_that_does_not_stand_alone_makes_the_card_unreadable(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"P-TWOTITLES.md": GLUED_CLOSE})

    assert DiagnosticCode.CARD_UNREADABLE in diagnostic_codes(work)


DOUBLED_TERMINATOR = REPEATED_TITLE.replace(
    "title: The first title\ntitle: The second title\n", "title: A prime-order group\n"
).replace(
    "review: draft\n---\n\n::: problem",
    "review: draft\n---\n---\n\n::: problem",
)


def test_a_doubled_front_matter_terminator_makes_the_card_unreadable(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"P-TWOTITLES.md": DOUBLED_TERMINATOR})

    assert DiagnosticCode.CARD_UNREADABLE in diagnostic_codes(work)


def test_a_horizontal_rule_later_in_the_body_is_not_a_doubled_terminator(tmp_path: Path) -> None:
    card = REPEATED_TITLE.replace(
        "title: The first title\ntitle: The second title\n", "title: A prime-order group\n"
    ).replace("Show that a group of prime order is cyclic.", "Show that a group of prime order is cyclic.\n\n---\n\nThen it is cyclic.")
    work = fixture_repo(tmp_path, {"P-TWOTITLES.md": card})

    assert DiagnosticCode.CARD_UNREADABLE not in diagnostic_codes(work)
