"""Every authored fenced-div class must map to a card kind, or the build fails.

WS1's first acceptance criterion is that no class in the corpus is *silently
treated as prose*. A typo (`::: definitoin`) and a genuinely new environment are
indistinguishable to the compiler, so both must stop the build: the alternative
is a definition that never reaches the index and no diagnostic saying so.

`foldopen` is the one measured class that is presentational, and it is listed as
such rather than ignored, so "we never looked at it" and "we looked and it means
nothing" stay distinguishable.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from conftest import ROOT, fixture_repo, run_qualc

CARD = """---
schema: qual/card@1
id: D-TYPO1
kind: definition
title: A definition behind a misspelled fence
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: definitoin
A group is a monoid whose every element is invertible.
:::
"""

NESTED_IN_QUOTE = """---
schema: qual/card@1
id: S-QUOTE1
kind: solution
title: A solution whose proof sits inside a block quote
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: solution
The argument is quoted from the original sheet.

> ::: proof
> Lagrange gives the order of every subgroup, so the index is an integer.
> :::

:::
"""


def test_unmapped_class_fails_the_build(tmp_path: Path) -> None:
    result = run_qualc("check", fixture_repo(tmp_path, {"typo.md": CARD}))
    assert result.returncode != 0, "an unmapped div class must not pass check"
    assert "definitoin" in result.stderr, "the diagnostic must name the offending class"


def test_the_current_corpus_uses_only_mapped_classes(tmp_path: Path) -> None:
    """The totality check is worth nothing if it is not satisfied today."""
    result = run_qualc("check", ROOT)
    assert result.returncode == 0, result.stderr


def test_section_inside_a_non_div_container_is_still_found(tmp_path: Path) -> None:
    """Recursion must follow the block tree, not only chains of divs.

    A proof quoted inside a `>` block is a proof. Descending only into `Div`
    children loses it, and loses the totality check along with it.
    """
    work = fixture_repo(tmp_path, {"quoted.md": NESTED_IN_QUOTE})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    kinds = [k for (k,) in con.execute("select section_kind from sections where card_id = 'S-QUOTE1'")]
    assert kinds == ["solution", "proof"], kinds
