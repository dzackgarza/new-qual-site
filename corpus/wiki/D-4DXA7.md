---
schema: qual/card@1
id: D-4DXA7
kind: definition
title: "$T_n$ Spaces (Separation Axioms)"
classification:
  areas:
  - topology
  topics:
  - point-set
  - separation-axioms
  - hausdorff-spaces
relations: []
review: draft
---

::: {.definition title="$T_n$ Spaces (Separation Axioms)"}
\envlist

- $T_0$: Points are distinguishable.
  For any 2 points $x_1\neq x_2$, at least one $x_i$ (say $x_1$) admits a neighborhood not containing $x_2$.

- $T_1$: For any 2 points, *both* admit neighborhoods not containing the other.
  Equivalently, points are closed.

- $T_2$: For any 2 points, both admit *disjoint* separating neighborhoods.

- $T_{2.5}$: For any 2 points, both admit *disjoint closed* separating neighborhoods.

- $T_3$: $T_0$ & *regular*. Given any point $x$ and any closed $F\not\ni x$, there are neighborhoods separating $F$ and $x$.

- $T_{3.5}$: $T_0$ & completely regular.
  Any point $x$ and closed $F\not\ni x$ can be separated by a continuous function.

- $T_4$: $T_1$ & normal.
  Any two disjoint closed subsets can be separated by neighborhoods.
:::
