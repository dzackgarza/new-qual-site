---
schema: qual/card@1
id: PR-FULKSQ
kind: proposition
title: K squared equals twelve minus the number of rays on a smooth complete toric surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Surfaces
  - Intersection Theory
relations:
- kind: uses
  target: T-TORSURF
review: draft
prompts:
- Compute K^2 for a smooth complete toric surface from its fan.
- How does Noether's formula read for toric surfaces?
---

::: {.proposition}
Let $X$ be a smooth complete toric surface with $d = \size \Sigma(1)$ rays and boundary divisors $D_1, \ldots, D_d$ in cyclic order.
Then
\[
K_X^2 = 12 - d .
\]
:::

::: {.proof}
Write $D_i^2 = -a_i$ with $\sum_i a_i = 3d - 12$, and $K_X = -\sum_i D_i$.
Adjacent divisors meet once and non-adjacent ones not at all, so the cross terms contribute $2d$:
\[
K_X^2 = \Big( \sum_i D_i \Big)^2 = \sum_i D_i^2 + 2 \sum_i D_i \cdot D_{i+1} = -\sum_i a_i + 2d = -(3d - 12) + 2d = 12 - d .
\]
:::

::: {.remark}
This is Noether's formula made trivial.
A toric surface is rational, so $\chi(\OO_X) = 1$, and its topological Euler characteristic is the number of maximal cones, which for a complete surface is also $d$.
Noether's $K^2 + \chi_{\mathrm{top}} = 12 \chi(\OO_X)$ then reads $K^2 + d = 12$.

The checks are immediate.
$\PP^2$ has $d = 3$ and $K^2 = 9$.
Each Hirzebruch surface has $d = 4$ and $K^2 = 8$, independent of $a$.
Every blowup adds one ray and drops $K^2$ by one, so the toric del Pezzos $\Bl_1, \Bl_2, \Bl_3 \PP^2$ have $K^2 = 8, 7, 6$ and the list is exactly the surfaces with $d \leq 6$ and $-K$ ample.
:::
