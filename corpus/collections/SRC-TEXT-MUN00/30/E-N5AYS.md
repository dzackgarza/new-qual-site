---
schema: qual/card@1
id: E-N5AYS
kind: problem
title: Disjoint open collections in separable spaces are countable
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), the second item printed under
    the heading "Problem 30.12", printed p. 3 (tmp/sources/munkres-solutions-dougsworld-ch4.pdf);
    its statement is the printed Exercise 30.13 (Munkres, Topology (2000), printed p. 194), which
    that set numbers as 30.12 -- the numbering slip is in the source, and the exercise it answers
    is the one on this card. Checked against the printed exercise; the injection U -> a point of
    D cap U is the source's argument and no correction was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the injection from the nonempty members of the
    disjoint collection into the countable dense set, and the removal of the empty set.
    Doug's World, Chapter 4 Solutions, the second item under its Problem 30.12 (printed p.
    3), which answers the printed Exercise 30.13 of Munkres; the numbering slip is the
    source's. The printed statement needed no repair.
---

::: {.exercise}

Show that if $X$ has a countable dense subset, every collection of disjoint open sets in $X$ is countable.
:::

::: {.solution}
The published solution is **"Doug's World", *Munkres - Topology - Chapter 4 Solutions* (30 August 2017; the file names no author), the second item under its heading "Problem 30.12"** (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`); the numbering slip is the source's, and the exercise it answers is Exercise 30.13 of Munkres, which is the one on this card. The injection below is its argument.

::: pf

::: {.pf-step #nonempty}
Let $\mathcal{U}'$ be the nonempty members of $\mathcal{U}$, and for each $U\in\mathcal{U}'$ choose a point $d_{U}\in D\cap U$.

::: pf-proof
$D$ is dense, so it meets every nonempty open subset of $X$ (§17, definition of dense); since $U$ is open and nonempty, $D\cap U\ne\varnothing$. Choosing one point from each such intersection gives $d_{U}\in U$.
:::

:::

::: {.pf-step #injection}
$U\mapsto d_{U}$ is injective on $\mathcal{U}'$.

::: pf-proof
If $U\ne U'$ are members of $\mathcal{U}'$ then $U\cap U'=\varnothing$ by pairwise disjointness, so $d_{U}\in U$ and $d_{U'}\in U'$ are distinct points of $D$.
:::

:::

::: {.pf-step}
$\mathcal{U}$ is countable.

::: pf-proof
The map of step [](#injection){.pf-ref} injects $\mathcal{U}'$ into the countable set $D$, so $\mathcal{U}'$ is countable. A countable set together with at most one further element, $\varnothing$, is countable, and $\mathcal{U}$ differs from $\mathcal{U}'$ by at most that element.
:::

:::

:::
:::
