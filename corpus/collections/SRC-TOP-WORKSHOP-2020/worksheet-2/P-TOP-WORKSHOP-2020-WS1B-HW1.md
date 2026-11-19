---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1B-HW1
kind: problem
title: The definition of a topology on a set
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. The item asks for a definition, so the steps are
    the definition's clauses and the terminology, each justified rather than proved, with the
    observation that "$\varnothing\in\tau$" and "$X\in\tau$" are the empty-family conventions of
    the union and intersection axioms. The content is unchanged and matches Munkres §12. The
    collection's provenance is the worksheet, so no retained solution set bears on the item and the
    card says so. Not claimed: a reading of the workshop's own solution key, which is not in this
    checkout, and no numerical or structural claim is asserted beyond the definition.
---

::: {.problem}
What is a topology on a set?
:::

::: {.solution}
This item asks for the definition, and the definition below is the one of Munkres, §12, which is the workshop's text; the collection's provenance is the worksheet itself, so no retained solution set bears on it.

::: pf

::: {.pf-step #axioms}
A topology on a set $X$ is a collection $\tau\subseteq\mathcal{P}(X)$ with $\varnothing\in\tau$, $X\in\tau$, closed under arbitrary unions and under finite intersections.

::: pf-proof
That is the definition: $\tau$ must contain the empty set and $X$; for every family $\{U_\alpha\}_{\alpha\in A}$ of members of $\tau$, indexed by an arbitrary set $A$, the union $\bigcup_{\alpha\in A}U_\alpha$ must lie in $\tau$; and for members $U_1,\ldots,U_n$ with $n\ge1$, the intersection $U_1\cap\cdots\cap U_n$ must lie in $\tau$.
:::

:::

::: {.pf-step #conventions}
The two clauses "$\varnothing\in\tau$" and "$X\in\tau$" are listed because the union and intersection axioms are stated for families indexed by nonempty $A$ and for $n\ge1$ respectively; with the usual conventions $\bigcup_\varnothing=\varnothing$ and $\bigcap_\varnothing=X$ they would follow.

::: pf-proof
The empty union is the empty set, and the empty intersection is the whole set $X$ on which the family is taken. A statement of the axioms that admits the empty family therefore implies both clauses; the definition above states them separately, as the textbook does, and the two readings define the same class of collections $\tau$.
:::

:::

::: {.pf-step}
The members of a topology $\tau$ on $X$ are called the open subsets of $X$ for $\tau$, and the pair $(X,\tau)$ is a topological space.

::: pf-proof
This is the terminology attached to the definition, and it is what makes a topological space a set together with a topology on it. So a topology on $X$ is exactly the data of which subsets of $X$ are to be called open, subject to the three requirements of step [](#axioms){.pf-ref}.
:::

:::

:::
:::
