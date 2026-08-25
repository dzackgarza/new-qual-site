"""Corpus-level claims that decay silently if only the schema is checked.

`test_invariants.py` owns the architectural claim that layout is inert.
This file owns the injected-violation proof that an unregistered area cannot
enter through a source.

The `qualc check` gate is the reason the source-area guard exists at all: it
validated `classification.areas` against the registry and never `source.area`,
so `prelim` entered 29 UGA collection cards unregistered, and the 419 cards that
should have inherited an area from them ended up with `areas: []` instead.
"""

from __future__ import annotations

from pathlib import Path

from qualc.diagnostics import DiagnosticCode
from qualc.index import load_vocabularies, validate
from qualc.model import CollectionCard, ParsedCard, ProblemCard

ROOT = Path(__file__).resolve().parent.parent


def _problem_card(card_id: str) -> ParsedCard:
    return ParsedCard(
        card=ProblemCard.model_validate(
            {
                "schema": "qual/card@1",
                "id": card_id,
                "kind": "problem",
                "title": "A problem",
                "classification": {"areas": ["algebra"], "topics": ["Groups"]},
                "relations": [],
                "review": "draft",
            }
        ),
        ast="[]",
        source_path="test",
        sections=[],
    )


def _collection_card(area: str) -> ParsedCard:
    return ParsedCard(
        card=CollectionCard.model_validate(
            {
                "schema": "qual/card@1",
                "id": "SRC-TEST",
                "kind": "collection",
                "title": "An exam",
                "classification": {"areas": ["algebra"], "topics": []},
                "relations": [],
                "review": "draft",
                "source": {
                    "source_kind": "university-exam",
                    "institution": "uga",
                    "area": area,
                    "date": {"kind": "year", "year": 2016},
                },
            }
        ),
        ast="[]",
        source_path="test",
        sections=[],
    )


def test_unregistered_source_area_is_rejected() -> None:
    """The injected violation: a collection card whose source names an area the
    registry does not know. Before this guard the corpus accepted it silently."""
    vocab = load_vocabularies(ROOT / "vocabularies")

    errors = validate([_collection_card("not-a-real-area")], vocab)
    assert [error.code for error in errors] == [DiagnosticCode.UNKNOWN_AREA], (
        f"an unregistered source.area must be rejected as unknown-area; got {[e.code for e in errors]}"
    )

    # And the same card with a registered area passes, so the guard is not
    # simply rejecting every collection card.
    assert validate([_collection_card("algebra")], vocab) == []
