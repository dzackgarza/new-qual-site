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
---

::: {.exercise}

Show that the $T_1$ axiom is equivalent to the condition that for each pair of points of $X$, each has a neighborhood not containing the other.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.15, PDF p. 8** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both directions are theirs. Whitman, printed p. 166, gives the same two directions through Corollary 17.7.

The points in question must be distinct, since a neighbourhood of a point contains that point.

*$T_{1}$ implies the condition.* Let $x\ne y$. In a $T_{1}$ space one-point sets are closed, so $X-\{x\}$ is open; it contains $y$ and not $x$. Likewise $X-\{y\}$ is a neighbourhood of $x$ not containing $y$.

*The condition implies $T_{1}$.* It is enough to show that every one-point set is closed (Munkres, Theorem 17.8: $X$ is $T_{1}$ exactly when its finite subsets are closed). Let $x\in X$. For each $y\in X-\{x\}$ the condition gives a neighbourhood $U_{y}$ of $y$ with $x\notin U_{y}$, that is $U_{y}\subset X-\{x\}$. Then
$$
X-\{x\}=\bigcup_{y\in X-\{x\}}U_{y}
$$
is a union of open sets, hence open, and $\{x\}$ is closed.
:::
