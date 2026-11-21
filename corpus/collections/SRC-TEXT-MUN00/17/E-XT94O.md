---
schema: qual/card@1
id: E-XT94O
kind: problem
title: Equivalents of the T1 axiom
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 15, printed p. 101, with Theorem
    17.8 on printed p. 99; the stored statement is the printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.15, PDF p. 8. In a T1 space the complements of
    singletons are the required neighbourhoods, and conversely the union of the
    neighbourhoods omitting x is the complement of {x}. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as the two directions of the equivalence. Re-checked that one-point sets are closed in a $T_{1}$ space and Theorem 17.8 (printed p. 98) for the converse. No statement change.
---

::: {.exercise}

Show that the $T_1$ axiom is equivalent to the condition that for each pair of points of $X$, each has a neighborhood not containing the other.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.15** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both directions are theirs. Whitman, gives the same two directions through Corollary 17.7.

The points in the condition are distinct, since a neighbourhood of a point contains that point.

::: pf

::: pf-step

If $X$ satisfies the $T_{1}$ axiom, then each of two distinct points has a neighbourhood not containing the other.

::: pf-proof

Let $x\ne y$. In a $T_{1}$ space one-point sets are closed, so $X-\{x\}$ is open; it contains $y$ and not $x$. Likewise $X-\{y\}$ is open, contains $x$ and not $y$.

:::

:::

::: pf-step

If each of two distinct points has a neighbourhood not containing the other, then $X$ satisfies the $T_{1}$ axiom.

::: pf-proof

By Theorem 17.8 it is enough to show that every one-point set is closed. Let $x\in X$. For each $y\in X-\{x\}$ the hypothesis gives a neighbourhood $U_{y}$ of $y$ with $x\notin U_{y}$, that is $U_{y}\subset X-\{x\}$. Then
$$
X-\{x\}=\bigcup_{y\in X-\{x\}}U_{y},
$$
a union of the open sets $U_{y}$, hence open, and $\{x\}$ is closed.

:::

:::

:::
:::
