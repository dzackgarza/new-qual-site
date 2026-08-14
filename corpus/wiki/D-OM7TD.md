---
schema: qual/card@1
id: D-OM7TD
kind: definition
title: "$T_n$ Spaces (Separation Axioms)"
classification:
  areas:
  - topology
  topics:
  - point-set
  - separation-axioms
  - counterexamples
relations: []
review: draft
---

::: {.definition title="$T_n$ Spaces (Separation Axioms)"}
\envlist

- $T_0$: points are topologically distinguishable, i.e. for any 2 points $x_1\neq x_2$, at least one $x_i$ (say $x_1$) admits a neighborhood not containing $x_2$.

- $T_1$: For any 2 points, *both* admit neighborhoods not containing the other.
  Equivalently, points are closed.

- $T_2$: For any 2 points, both admit *disjoint* separating neighborhoods.

- $T_{2.5}$: For any 2 points, both admit *disjoint closed* separating neighborhoods.

- $T_3$: $T_0$ & *regular*. Given any point $x$ and any closed $F\not\ni x$, there are neighborhoods separating $F$ and $x$.

- $T_{3.5}$: $T_0$ & completely regular.
  Any point $x$ and closed $F\not\ni x$ can be separated by a continuous function.

- $T_4$: $T_1$ & normal.
  Any two disjoint closed subsets can be separated by neighborhoods.

::: {.example title="Counterexamples for separation axioms"}
\envlist

- Not $T_0$: the space \( \ts{ f:\RR\to \CC\st \int_\RR \abs{f}^2 < \infty } \), since two a.e. equal functions aren't *distinguishable* (they have precisely the same set of neighborhoods).

- $T_1$ but not $T_0$: $\spec R$ for $R\in \CRing$ with the Zariski topology.
  There are points that aren't closed: $\spec R \sm \mspec R$.
:::
:::
