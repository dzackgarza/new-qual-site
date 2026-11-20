---
schema: qual/card@1
id: E-L4NKO
kind: problem
title: Locally compact Hausdorff spaces are regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), Problem 32.3, printed p. 6
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 32 Exercise 3, printed p. 205, Theorem 32.3 (a compact Hausdorff space is normal),
    Theorem 29.1 and Theorem 31.2(b) (a subspace of a regular space is regular). Its route is
    the one on the card: a compact locally compact Hausdorff space is normal by Theorem 32.3, and
    otherwise the one-point compactification is normal and the space is a subspace of it. The card
    also gives the direct route through Theorem 29.2, which is the statement the source is
    reproducing; no correction to the mathematics was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked both conditions of regularity: points closed
    from the Hausdorff axiom, and a point separated from a closed set by a neighbourhood
    with compact closure inside the complementary open set (Theorem 29.2). Doug's World,
    Chapter 4 Solutions, Problem 32.3, printed p. 6, whose route is reproduced by Theorem
    29.2; the card takes the direct route and says so. The printed statement needed no
    repair.
---

::: {.exercise}

Show that every locally compact Hausdorff space is regular.
:::

::: {.solution}
The published solution is **"Doug's World", *Munkres - Topology - Chapter 4 Solutions* (30 August 2017; the file names no author), Problem 32.3** (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`); the route through Theorem 29.2 below is the card's direct one, which is the statement that source reproduces.

::: pf

::: {.pf-step #t1}
Points of $X$ are closed.

::: pf-proof
$X$ is Hausdorff, so for each $y\ne x$ there are disjoint open sets $U_{y}\ni y$ and $W_{y}\ni x$. Then $X-\{x\}=\bigcup_{y\ne x}U_{y}$ is open, since each $U_{y}$ is open and misses $x$, so $\{x\}$ is closed. In particular every singleton is closed, which is the first requirement in the definition of a regular space.
:::

:::

::: {.pf-step #separate}
For $A$ closed in $X$ and $x\notin A$ there are disjoint open sets containing $x$ and $A$.

::: pf-proof
The set $U=X-A$ is open and contains $x$. Since $X$ is locally compact Hausdorff, Theorem 29.2 gives a neighbourhood $V$ of $x$ with $\overline{V}$ compact and $\overline{V}\subset U$. Then $V$ is open and contains $x$, and $X-\overline{V}$ is open because $\overline{V}$ is closed, and contains $A$ because $A\subset X-U\subset X-\overline{V}$. The two are disjoint, since $V\subset\overline{V}$.
:::

:::

::: {.pf-step}
$X$ is regular.

::: pf-proof
A space is regular when points are closed and each point can be separated from each closed set not containing it by disjoint open sets (§31). Steps [](#t1){.pf-ref} and [](#separate){.pf-ref} are exactly these two conditions.
:::

:::

:::
:::
