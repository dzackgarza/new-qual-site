---
schema: qual/card@1
id: E-QGR6H
kind: problem
title: Compact unions of closed metrizable subspaces are metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: "Doug's World", "Munkres - Topology - Chapter
    4 Solutions" (30 August 2017), Problem 34.9 with its Proposition 7, printed pp. 11-12
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 34: Problem 9 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-34-the-urysohn-metrization-theorem/problem-9-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-9-solution.txt); checked
    against Munkres, Topology (2000), Section 34 Exercise 9, printed p. 218, and its printed hint,
    with Exercise 30.4. The card builds the countable family of the hint -- lifts of the bases of the
    two closed subspaces together with X - X_1 and X - X_2 -- and checks that its finite
    intersections form a basis, by taking for each i either the lifted basis element through x or the
    complement of X_i. What was corrected: Doug's World writes the cover at the end as B = B_1 cup B_2
    cup (X_1 - X_2) cup (X_2 - X_1) and then proves separateness in two cases, introducing a
    "B = B_1 cap B_2" that its own definition does not contain; the card takes the whole family of
    finite intersections, which is the hint's construction.
---

::: {.exercise}

Let $X$ be a compact Hausdorff space that is the union of the closed subspaces $X_1$ and $X_2$.
If $X_1$ and $X_2$ are metrizable, show that $X$ is metrizable.
[Hint: Construct a countable collection $\mathcal{A}$ of open sets of $X$ whose intersections with $X_i$ form a basis for $X_i$, for $i = 1, 2$. Assume $X_1 - X_2$ and $X_2 - X_1$ belong to $\mathcal{A}$. Let $\mathcal{B}$ consist of finite intersections of elements of $\mathcal{A}$.]
:::

::: {.solution}
Since each $X_i$ is closed in compact $X$, each $X_i$ is compact. Being metrizable, each $X_i$ therefore has a countable basis $\mathcal B_i$.

For every $B\in\mathcal B_i$, choose an open set $\widetilde B\subset X$ such that
$$
\widetilde B\cap X_i=B.
$$
Let $\mathcal A$ be the countable collection of all these chosen lifts, together with the two open sets
$$
X\setminus X_1,\qquad X\setminus X_2.
$$
Let $\mathcal C$ be the collection of all finite intersections of members of $\mathcal A$. It is countable.

We show $\mathcal C$ is a basis for $X$. Let $x\in U$ with $U\subset X$ open. For each $i=1,2$:

- if $x\in X_i$, choose $B_i\in\mathcal B_i$ with
$$
x\in B_i\subset U\cap X_i,
$$
and let $\widetilde B_i\in\mathcal A$ be its chosen lift;
- if $x\notin X_i$, use the member $X\setminus X_i\in\mathcal A$.

The intersection $C$ of the resulting one or two members of $\mathcal A$ contains $x$. For each $i$,
$$
C\cap X_i\subset U\cap X_i.
$$
Since $X=X_1\cup X_2$, this implies $C\subset U$. Hence $\mathcal C$ is a countable basis for $X$.

By the preceding compact-Hausdorff metrization criterion, $X$ is metrizable.
:::
