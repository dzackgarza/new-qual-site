"""Semantic sections are found wherever they appear, not only at the top level.

Nesting is normal in this corpus: `solution` containing `proof` is its dominant
compound shape (159 occurrences in qual-wiki, 141 in qual-review-and-solutions),
and `claim` is *never* top-level in either repo. Neither the index nor the
renderer handled it: `site/filters/reveal.lua` does walk the whole block tree,
but it matches the `qual-*` classes the emitter assigns, and the emitter renamed
top-level divs only, so a nested solution rendered fully expanded.
"""

from __future__ import annotations

import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NESTED_CARD = """---
schema: qual/card@1
id: S-NEST1
kind: solution
title: A solution whose argument contains a nested proof
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: solution
The claim follows from Sylow.

::: proof
Counting Sylow subgroups gives $n_p \\equiv 1 \\pmod p$, and the only divisor
of the index congruent to $1$ is $1$ itself, so the subgroup is normal.
:::

:::
"""


def build(work: Path) -> sqlite3.Connection:
    subprocess.run(
        [sys.executable, "-m", "qualc", "build", "--root", str(work)],
        check=True,
        capture_output=True,
    )
    return sqlite3.connect(work / "build" / "catalog.sqlite")


def fixture_repo(tmp_path: Path) -> Path:
    work = tmp_path / "repo"
    for sub in ("corpus", "vocabularies", "publications", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    (work / "corpus" / "nested.md").write_text(NESTED_CARD)
    return work


def test_nested_section_is_indexed(tmp_path: Path) -> None:
    con = build(fixture_repo(tmp_path))
    kinds = [k for (k,) in con.execute("select section_kind from sections where card_id = 'S-NEST1'")]
    assert "solution" in kinds, "the enclosing solution should be indexed"
    assert "proof" in kinds, "the proof nested inside it should be indexed too"


def test_nested_section_is_searchable_as_its_own_kind(tmp_path: Path) -> None:
    """Searching must be able to distinguish a hit *in a proof* from one merely in
    the solution that encloses it.

    Asserting only that 'Sylow' matches somewhere is not a proof of anything: the
    parent's text already contains the nested prose because `pf.stringify` recurses,
    so that assertion passes while the bug is present. The discriminating question
    is whether the proof reaches the index as a proof.
    """
    con = build(fixture_repo(tmp_path))
    hits = con.execute("select section_kind from search where search match 'Sylow' and card_id = 'S-NEST1'").fetchall()
    assert ("proof",) in hits, "the nested proof must be searchable as a proof"


def test_enclosing_section_still_carries_its_own_text(tmp_path: Path) -> None:
    """Recursing must not move the nested text out of its parent, only add a row."""
    con = build(fixture_repo(tmp_path))
    (solution_text,) = con.execute("select text from sections where card_id = 'S-NEST1' and section_kind = 'solution'").fetchone()
    assert "follows from Sylow" in solution_text
