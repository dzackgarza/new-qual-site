"""A solution written in the Lamport filter's syntax renders with the filter's numbering.

The proof source carries structure only: steps, their proofs, and labels on the
steps a later step cites. Numbers, indentation and the text of a reference come
from pandoc-config's `lamport_proof.lua`, so the card never states them.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from conftest import diagnostic_codes, fixture_repo, run_qualc
from qualc.diagnostics import DiagnosticCode

CARD = """---
schema: qual/card@1
id: P-LAMPORT
kind: problem
title: Sum of two odd integers
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: problem
Show that the sum of two odd integers is even.
:::

::: solution
::: pf

::: {.pf-step #forms}
Write the integers as $2a+1$ and $2b+1$ with $a, b \\in \\ZZ$.

::: pf-proof
An integer is odd exactly when it has this form.
:::

:::

::: pf-step
Their sum is $2(a+b+1)$.

::: pf-proof
Add the two forms from step [](#forms){.pf-ref}.
:::

:::

::: pf-qed
An integer of the form $2c$ is even.
:::

:::
:::
"""


@pytest.fixture(scope="module")
def site(tmp_path_factory: pytest.TempPathFactory) -> Path:
    work = fixture_repo(tmp_path_factory.mktemp("lamport"), {"P-LAMPORT.md": CARD})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    return work


def test_steps_are_numbered_and_references_resolved_by_the_filter(site: Path) -> None:
    page = (site / "build" / "quarto" / "_site" / "tag" / "P-LAMPORT.html").read_text()
    assert '<span class="pf-number">1.</span>' in page
    assert '<span class="pf-number">2.</span>' in page
    assert '<span class="pf-number">3. QED</span>' in page
    assert 'id="forms"' in page
    assert 'class="pf-ref">1</a>' in page


def test_a_malformed_proof_fails_the_check(tmp_path: Path) -> None:
    """Two steps with one label cannot both be the target of a reference."""
    card = CARD.replace("::: pf-step\nTheir sum", "::: {.pf-step #forms}\nTheir sum", 1)
    assert card != CARD
    assert diagnostic_codes(fixture_repo(tmp_path, {"P-LAMPORT.md": card})) == [DiagnosticCode.LAMPORT_PROOF_INVALID]
