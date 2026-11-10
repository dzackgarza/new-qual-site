---
schema: qual/card@1
id: E-X1QM4
kind: problem
title: Compact locally euclidean Hausdorff spaces are manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: "Doug's World", "Munkres - Topology - Chapter
    4 Solutions" (30 August 2017), Problem 36.3 with Proposition 8, printed pp. 13-14
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 36: Problem 3 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-36-imbeddings-of-manifolds/problem-3-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-36-imbeddings-of-manifolds/problem-3-solution.txt); checked against
    Munkres, Topology (2000), Section 36 Exercise 3, printed p. 227, Exercise 30.4 and Theorem 30.2.
    The card's proof is the direct one: each point has an open neighbourhood that is an open subspace
    of a Euclidean open set, hence second countable, and compactness gives finitely many of them whose
    countable bases together form a countable basis. The sources reach the same conclusion differently
    -- dbFin through Exercise 2 and second countability of a subspace of a Euclidean space, Doug's
    World by showing X is a finite union of closed metrizable subspaces, hence metrizable, and then
    citing Exercise 30.4; no correction to the mathematics was needed.
---

::: {.exercise}

Let $X$ be a Hausdorff space such that each point of $X$ has a neighborhood that is homeomorphic with an open subset of $\RR^m$.
Show that if $X$ is compact, then $X$ is an $m$-manifold.
:::

::: {.solution}
By hypothesis, for each $x\in X$ there is a neighborhood $U_x$ homeomorphic to an open subset of $\RR^m$. Choose an open set $V_x$ with
$$
x\in V_x\subset U_x.
$$
Each $V_x$ is an open subspace of a Euclidean open set, hence is second countable.

Compactness gives finitely many points $x_1,\dots,x_r$ such that
$$
X=V_{x_1}\cup\cdots\cup V_{x_r}.
$$
For each $i$, choose a countable basis $\mathcal B_i$ for the open subspace $V_{x_i}$. Since each $V_{x_i}$ is open in $X$,
$$
\mathcal B=\bigcup_{i=1}^r\mathcal B_i
$$
is a countable basis for $X$. The space is Hausdorff by assumption and locally homeomorphic to $\RR^m$ by hypothesis. Thus it satisfies the standard definition of an $m$-manifold.
:::
