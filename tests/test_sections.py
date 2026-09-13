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
from test_invariants import read_html

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


COMPACT_NESTED_CARD = """---
schema: qual/card@1
id: P-NEST2
kind: problem
title: A solution whose proof fences follow their Lamport steps directly
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: problem
Prove two claims.
:::

::: solution
<1>1. The first claim.
::: {.proof}
This proves the first claim.
:::

<1>2. The second claim.
<2>1. Its first subclaim.
    ::: {.proof}
    This proves the first subclaim and must remain hidden with the solution.
    :::
<2>2. Its second subclaim.
::: {.proof}
This proves the second subclaim.
:::

<1>3. The third claim.
::: {.proof}
<1>2.2.
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


def test_compact_and_indented_proof_fences_do_not_leak_a_solution(tmp_path: Path) -> None:
    """The corpus's compact proof spelling is normalized before Pandoc reads it.

    A generated proof opener often follows its Lamport step with no intervening
    blank line, and deeper proof openers are indented by four or eight spaces.
    Pandoc otherwise reads those as paragraph/code text and the first bare
    `:::` closes the surrounding solution, exposing everything after it.
    """
    work = fixture_repo(tmp_path, {"compact-nested.md": COMPACT_NESTED_CARD})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    sections = con.execute(
        "select section_kind, text from sections where card_id='P-NEST2' order by ordinal",
    ).fetchall()
    assert [kind for kind, _ in sections].count("solution") == 1
    assert [kind for kind, _ in sections].count("proof") == 4
    solution = next(text for kind, text in sections if kind == "solution")
    assert "This proves the first claim" in solution
    assert "This proves the first subclaim and must remain hidden with the solution" in solution

    page = read_html(work / "build" / "quarto" / "_site" / "tag" / "P-NEST2.html")
    disclosures = page.root.find_all("details", **{"class": "reveal qual-solution"})
    assert len(disclosures) == 1
    disclosure_text = " ".join(disclosures[0].text.split())
    assert "This proves the first claim" in disclosure_text
    assert "This proves the first subclaim and must remain hidden with the solution" in disclosure_text
    numbers = [node.text.strip() for node in disclosures[0].find_all("span", **{"class": "pf-number"})]
    assert numbers == ["1.", "2.", "2.1.", "2.2.", "3."], numbers
    assert disclosure_text.endswith("2.2.")
    assert ":::" not in page.root.text
