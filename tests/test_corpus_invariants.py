"""The corpus-level invariants of PLAN-QUAL-GRUNT-001, as runnable checks.

`test_invariants.py` owns the architectural claim that layout is inert.
This file owns the claims that decay silently: that every source file has a
disposition, that a disposition reason is true of its file, and that an
unregistered area cannot enter the corpus through a payload.

Each check here fails on an injected violation, not merely on a malformed file.
The `qualc check` gate is the reason the third one exists at all: it validated
`classification.areas` against the registry and never `payload.area`, so
`prelim` entered 29 UGA source cards unregistered, and the 419 cards that should
have inherited an area from them ended up with `areas: []` instead.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from audit import check_ledger_totality, check_queued_not_claimed, check_reason_truth
from qualc.diagnostics import DiagnosticCode
from qualc.index import load_vocabularies, validate
from qualc.model import ParsedCard, SourceCard

ROOT = Path(__file__).resolve().parent.parent


def _source_card(area: str) -> ParsedCard:
    return ParsedCard(
        card=SourceCard.model_validate(
            {
                "schema": "qual/card@1",
                "id": "SRC-TEST",
                "kind": "source",
                "title": "A sitting",
                "classification": {"areas": ["algebra"], "topics": []},
                "relations": [],
                "review": "draft",
                "payload": {
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


def test_unregistered_payload_area_is_rejected() -> None:
    """The injected violation: a source card whose payload names an area the
    registry does not know. Before this guard the corpus accepted it silently."""
    vocab = load_vocabularies(ROOT / "vocabularies")

    errors = validate([_source_card("not-a-real-area")], vocab)
    assert [error.code for error in errors] == [DiagnosticCode.UNKNOWN_AREA], f"an unregistered payload.area must be rejected as unknown-area; got {[e.code for e in errors]}"

    # And the same card with a registered area passes, so the guard is not
    # simply rejecting every source card.
    assert validate([_source_card("algebra")], vocab) == []


# These three read the source repos themselves, because the totality claim is
# only meaningful against the repos and never against a summary of them. CI has
# no clones, so it deselects this marker by name -- an explicit, stated exclusion
# rather than a skip that reads as a pass. G9's archive gate is what runs them
# against fresh clones before any repo is archived.
@pytest.mark.needs_source_clones
def test_every_source_file_has_exactly_one_disposition() -> None:
    check = check_ledger_totality()
    assert check.skipped is None, f"totality is unmeasurable: {check.skipped}"
    assert check.violations == []


@pytest.mark.needs_source_clones
def test_no_dropped_file_holds_problem_statements() -> None:
    """A disposition reason must be true of the file. The realized failure was
    `dropped / authored .md not routed (index/config/personal)` on files holding
    dozens of numbered problems."""
    check = check_reason_truth()
    assert check.violations == []
    assert check.skipped is None, f"some dropped rows were unreadable: {check.skipped}"


@pytest.mark.needs_source_clones
def test_no_migrated_row_without_evidence() -> None:
    assert check_queued_not_claimed().violations == []


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
