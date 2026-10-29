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
(a) Their sum is $2(a+b+1)$.

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
    # A claim opening with a part label stays one paragraph beside its number.
    assert '<span class="pf-number">2.</span> (a) Their sum is' in page
    assert '<span class="pf-number">3. QED</span>' in page
    assert 'id="forms"' in page
    assert 'class="pf-ref">1</a>' in page


PAIR_CARD = """---
schema: qual/card@1
id: __ID__
kind: problem
title: __TITLE__
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: problem
State the __TITLE__ step of the argument.
:::

::: solution
::: pf

::: {.pf-step #s2}
The labelled step, the one a later step cites.

::: pf-proof
A label is unique in its own card.
:::

:::

::: pf-step
Its successor, cited as [](#s2){.pf-ref}.

::: pf-proof
Because of [](#s2){.pf-ref}.
:::

:::

::: pf-qed
Done.
:::

:::
:::
"""


def test_two_transcluded_cards_may_reuse_a_step_label(tmp_path_factory: pytest.TempPathFactory) -> None:
    """A step label is unique in its card, not on the page that inlines several.

    Two cards both write `#s2`. Read on their own -- what `qualc check` does --
    both are valid; inlined onto one wiki page the lamport filter saw two
    `id="s2"` steps and rejected the page with "duplicate step label: s2",
    failing the build after check had passed.
    """
    work = fixture_repo(tmp_path_factory.mktemp("lamport-pairs"))
    cards = {
        "P-PFA.md": PAIR_CARD.replace("__ID__", "P-PFA").replace("__TITLE__", "First"),
        "P-PFB.md": PAIR_CARD.replace("__ID__", "P-PFB").replace("__TITLE__", "Second"),
    }
    for name, text in cards.items():
        (work / "corpus" / name).write_text(text)
    page = work / "wiki" / "proof-pairs.md"
    page.write_text("---\ntitle: Proof pairs\norder: 1\n---\n\n[[P-PFA]]\n\n[[P-PFB]]\n")
    assert diagnostic_codes(work) == [], "each card is valid read on its own"
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    html = (work / "build" / "quarto" / "_site" / "wiki" / "proof-pairs.html").read_text()
    # Each card's label kept its own step and its own references.
    for card in cards:
        label = f"{card.removesuffix('.md')}--s2"
        assert f'id="{label}"' in html, label
        assert f'href="#{label}"' in html, label
    assert 'id="s2"' not in html, "no card left its label shared on the page"


def test_a_malformed_proof_fails_the_check(tmp_path: Path) -> None:
    """Two steps with one label cannot both be the target of a reference."""
    card = CARD.replace("::: pf-step\n(a) Their sum", "::: {.pf-step #forms}\n(a) Their sum", 1)
    assert card != CARD
    assert diagnostic_codes(fixture_repo(tmp_path, {"P-LAMPORT.md": card})) == [DiagnosticCode.LAMPORT_PROOF_INVALID]
