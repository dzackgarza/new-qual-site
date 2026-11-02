---
schema: qual/card@1
id: E-SMI-8000E-NR7
kind: problem
title: "Zorn's lemma: every proper ideal sits in a maximal ideal"
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-02
  note: >-
    Statement taken from the retained packet: assets/attachments/8000e.pdf, Noetherian-rings
    problem 7 ("Using Zorn's lemma, prove in any ring R, that every ideal I of R is contained in
    a maximal ideal"), read with pdftotext -layout. The card is new: the collection carried
    Noetherian problems 1-6, 8, 9 and 10 but not 7. The printed wording is kept on the card, and
    the one reading point it trails is named there: for the conclusion to have a chance to hold,
    the ideal has to be proper and the ring nonzero, since an ideal equal to R contains no
    maximal ideal and the zero ring has none.
- event: solution-written
  by: claude
  date: 2026-11-02
  note: >-
    Four steps: the poset of proper ideals containing I is nonempty because I is proper; chains
    have upper bounds in it since a chain of proper ideals has a proper union (an appeal to
    E-SMI-8000E-NR6, the packet's own preceding problem); Zorn gives a maximal element of the
    poset; and a poset-maximal member is a maximal ideal of R, because any strictly larger ideal,
    being again proper and so a member of the poset, would contradict maximality.
---

::: {.exercise}
Using Zorn's lemma, prove in any ring $R$ that every ideal $I$ of $R$ is contained in a maximal ideal.

:::

::: {.solution}
The statement is read with $R \neq 0$ and $I$ a proper ideal: an ideal equal to $R$ contains no maximal ideal, and the zero ring has none at all. The ring is commutative with $1$, as the whole problem sheet assumes.

::: pf

::: {.pf-step #poset}
The set
$$
\mathcal{P}=\{J : J\text{ is a proper ideal of }R,\ I\subseteq J\},
$$
ordered by inclusion, is nonempty.

::: pf-proof
$I \in \mathcal{P}$, since $I$ is proper.

:::

:::

::: {.pf-step #chains}
Every chain in $\mathcal{P}$ has an upper bound in $\mathcal{P}$.

::: pf-proof
A chain of proper ideals has a proper union: the union is an ideal because any two of its elements lie in a common chain member, and it is proper because $1$ would lie in one member were it equal to $R$, making that member $R$ itself. This is the packet's preceding problem [[E-SMI-8000E-NR6]]. The union contains $I$, so it belongs to $\mathcal{P}$ and is an upper bound of the chain there.

:::

:::

::: {.pf-step #zorn}
$\mathcal{P}$ has a maximal element.

::: pf-proof
This is Zorn's lemma, applied to the nonempty poset of step [](#poset){.pf-ref}, in which every chain has an upper bound by step [](#chains){.pf-ref}.

:::

:::

::: {.pf-step #maximal}
A maximal element $J$ of $\mathcal{P}$ is a maximal ideal of $R$ containing $I$.

::: pf-proof
$J \supseteq I$ holds by membership in $\mathcal{P}$. If $K$ is an ideal of $R$ with $J \subsetneq K$, then $K \notin \mathcal{P}$ by maximality of $J$ in $\mathcal{P}$; but $K \supseteq I$, so $K \notin \mathcal{P}$ means $K$ is not proper, hence $K = R$. Therefore no proper ideal of $R$ strictly contains $J$, which says $J$ is a maximal ideal of $R$.

:::

:::

:::

:::
