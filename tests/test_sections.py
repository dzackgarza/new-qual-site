"""Semantic sections are found wherever they appear, not only at the top level.

Nesting is normal in this corpus: `solution` containing `proof` is its dominant
compound shape (159 instances in qual-wiki, 141 in qual-review-and-solutions),
and `claim` is *never* top-level in either repo. Neither the index nor the
renderer handled it: `site/filters/reveal.lua` does walk the whole block tree,
but it matches the `qual-*` classes the emitter assigns, and the emitter renamed
top-level divs only, so a nested solution rendered fully expanded.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from conftest import fixture_repo, run_qualc

NESTED_CARD = """---
schema: qual/card@1
id: P-NEST1
kind: problem
title: A problem whose solution contains a nested proof
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: problem
Show the relevant Sylow subgroup is normal.
:::

::: solution
The claim follows from Sylow.

::: proof
Counting Sylow subgroups gives $n_p \\equiv 1 \\pmod p$, and the only divisor
of the index congruent to $1$ is $1$ itself, so the subgroup is normal.
:::

:::
"""


ADJACENT_LAMPORT_CARD = """---
schema: qual/card@1
id: P-FENCE1
kind: problem
title: A solution with adjacent Lamport proof fences
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: problem
Show the claim.
:::

::: solution
<1>1. First step.
::: proof
First reason.
:::

<1>2. Second step.
    ::: proof
    <2>1. Nested reason.
    <2>2. Another nested reason.
:::

<1>3. Third step.
:::
::: proof
Third reason.
:::

<1>4. Final step.
:::
:::
"""


def build(tmp_path: Path) -> sqlite3.Connection:
    """The claim under test is about the nested card, so it is the only card that
    needs to be here. This used to copy and build the whole real corpus -- three
    times in this file -- to assert something one card proves."""
    work = fixture_repo(tmp_path, {"nested.md": NESTED_CARD})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    return sqlite3.connect(work / "build" / "catalog.sqlite")


def test_nested_section_is_indexed(tmp_path: Path) -> None:
    con = build(tmp_path)
    kinds = [k for (k,) in con.execute("select section_kind from sections where card_id = 'P-NEST1'")]
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
    con = build(tmp_path)
    hits = con.execute("select section_kind from search where search match 'Sylow' and card_id = 'P-NEST1'").fetchall()
    assert ("proof",) in hits, "the nested proof must be searchable as a proof"


def test_enclosing_section_still_carries_its_own_text(tmp_path: Path) -> None:
    """Recursing must not move the nested text out of its parent, only add a row."""
    con = build(tmp_path)
    (solution_text,) = con.execute("select text from sections where card_id = 'P-NEST1' and section_kind = 'solution'").fetchone()
    assert "follows from Sylow" in solution_text


def test_adjacent_lamport_proof_fences_stay_inside_the_solution(tmp_path: Path) -> None:
    """A proof fence adjacent to a Lamport step must not terminate the solution.

    The corpus has both unindented and Lamport-indented spellings.  Pandoc
    otherwise reads the opener as paragraph/code text and uses its closing
    fence to close the surrounding solution, exposing later solution steps as
    part of the public statement.
    """
    work = fixture_repo(tmp_path, {"fence.md": ADJACENT_LAMPORT_CARD})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    sections = con.execute("select section_kind, text from sections where card_id='P-FENCE1' order by ordinal").fetchall()
    assert [kind for kind, _ in sections] == ["problem", "solution", "proof", "proof", "proof"]
    solution = next(text for kind, text in sections if kind == "solution")
    assert "First step" in solution
    assert "Second step" in solution
    assert "Third step" in solution
    assert "Final step" in solution

    page = (work / "build" / "quarto" / "_site" / "tag" / "P-FENCE1.html").read_text()
    statement = page.split('<div class="card-statement">', 1)[1].split('<details class="reveal qual-solution">', 1)[0]
    disclosure = page.split('<details class="reveal qual-solution">', 1)[1].split("</details>", 1)[0]
    assert "First reason" not in statement
    assert "Second step" not in statement
    assert "Final step" not in statement
    assert "First reason" in disclosure
    assert "Nested reason" in disclosure
    assert "Another nested reason" in disclosure
    assert "Third reason" in disclosure
    assert "Final step" in disclosure
    assert ":::" not in page
    assert "<pre><code>" not in disclosure
    assert 'class="pf-step pf-level-2"' in disclosure
