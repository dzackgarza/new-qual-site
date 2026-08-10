"""The flashcard importer reads the deck dialect and keeps its own rules honest.

Each assertion here is a decision the import got wrong on a first pass and would
get wrong again silently: a title fold that erased the mathematics, a figureless
card minted as if it were complete, and a repeated front collapsed without
looking at what the two backs actually said.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def _importer() -> Any:
    """`tools/` is a script directory, not an installed package, so the path
    join happens at run time and the module is genuinely untyped here."""
    sys.path.insert(0, str(ROOT / "tools"))
    return importlib.import_module("import_flashcards")


F: Any = _importer()

DECK = """---
title: "Qual Algebra::Fixture"
---

- Sylow Theorems

    Write $\\abs{G} = p^n m$.

    1. $n_p$ divides $m$
    2. $n_p \\equiv 1 \\mod p$

    tags: theorem, important

- Definition: Free module

    ![](https://i.imgur.com/h5r2lty.png)

    tags: definition

- Give an example of a function that converges in $L^1$ but not pointwise.

    The Cathode Ray:

    ![](https://i.imgur.com/a4MatmT.png)

    tags: example

- Untagged card

    Body with no tags line.
"""


def _cards(tmp_path: Path) -> list[Any]:
    path = tmp_path / "Fixture.md"
    path.write_text(DECK)
    original, F.DECKS = F.DECKS, tmp_path
    try:
        return list(F.parse_deck(path))
    finally:
        F.DECKS = original


def test_parse_keeps_the_back_verbatim_and_drops_only_the_list_syntax(tmp_path: Path) -> None:
    sylow, *_ = _cards(tmp_path)
    assert sylow.front == "Sylow Theorems"
    assert sylow.back == "Write $\\abs{G} = p^n m$.\n\n1. $n_p$ divides $m$\n2. $n_p \\equiv 1 \\mod p$"
    assert "tags:" not in sylow.back


def test_kind_takes_the_highest_priority_tag_and_falls_back_to_fact(tmp_path: Path) -> None:
    sylow, free_module, example, untagged = _cards(tmp_path)
    # `important` is a study marker, not a kind, so `theorem` wins.
    assert sylow.kind == "theorem"
    assert free_module.kind == "definition"
    assert example.kind == "example"
    # A result stated with no tag is a `fact`, never promoted to `theorem`.
    assert untagged.kind == "fact"


def test_a_card_whose_back_is_only_a_figure_has_no_statement(tmp_path: Path) -> None:
    _, free_module, example, _ = _cards(tmp_path)
    assert F.figureless_body(free_module.back) == ""
    # `The Cathode Ray:` announces the figure rather than replacing it.
    assert F.figureless_body(example.back) == ""
    # But a full argument that merely ends on a label is still an argument.
    proof = "- $f(z) = \\sum_k c_k z^k$ since $f(0)=0$.\n- Take $r\\to 1$.\n- The actual source:"
    assert F.figureless_body(proof) == proof


def test_normalize_separates_the_trig_values_and_the_signed_characteristics() -> None:
    keys = {F.normalize(f"$\\{fn}(\\pi/4) = \\cdots$") for fn in ("sin", "cos", "tan")}
    assert len(keys) == 3, "stripping macro names folds every special angle onto one key"
    assert F.normalize("Euler Characteristic 2") != F.normalize("Euler Characteristic -2")
    # Case, whitespace and math delimiters are still not differences.
    assert F.normalize("Rouche's  Theorem") == F.normalize("$Rouche's$ theorem")


def test_the_real_import_mints_a_theory_layer_and_queues_the_figureless_cards() -> None:
    rows = F.dispositions()
    assert len(rows) == 496, "the 28 qual decks hold 496 cards"

    minted = [r for r in rows if r["disposition"] == "migrated"]
    kinds = {r["kind"] for r in minted}
    assert {"definition", "theorem", "fact"} <= kinds

    queued = [r for r in rows if r["disposition"] == "queued"]
    assert queued, "the lost figures must leave queued rows, not incomplete cards"
    assert all("figure" in r["reason"] for r in queued)

    # Every variant-of target is itself minted, so no relation dangles.
    ids = {r["id"] for r in minted}
    assert all(r["variant_of"] in ids for r in minted if "variant_of" in r)

    # An id is a function of deck path and front, so a re-run is idempotent.
    assert len(ids) == len(minted)
