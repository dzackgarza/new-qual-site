---
schema: qual/card@1
id: PR-FULKSQ
kind: proposition
title: $K_X^2=12-\size\Sigma(1)$ for a smooth complete toric surface
slogan: 'For a smooth complete toric surface, every fan ray subtracts one from $K_X^2$: $K_X^2=12-\size\Sigma(1)$.'
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
- Compute $K_X^2$ for a smooth complete toric surface from its fan.
- How does Noether's formula read for toric surfaces?
---

::: {.proposition}
Let $X$ be a smooth complete toric surface with $d = \size \Sigma(1)$ rays and boundary divisors $D_1, \ldots, D_d$ in cyclic order.
Then
$$
K_X^2 = 12 - d .
$$
:::

::: {.proof}
Write $D_i^2 = -a_i$ with $\sum_i a_i = 3d - 12$, and $K_X = -\sum_i D_i$.
Adjacent divisors meet once and non-adjacent ones not at all, so the cross terms contribute $2d$:
$$
K_X^2 = \Big( \sum_i D_i \Big)^2 = \sum_i D_i^2 + 2 \sum_i D_i \cdot D_{i+1} = -\sum_i a_i + 2d = -(3d - 12) + 2d = 12 - d .
$$
:::

::: {.remark}
Over $k=\CC$, the same equality follows from Noether's formula. A smooth complete toric surface is rational, so $\chi(\OO_X)=1$. Its torus-orbit decomposition has one zero-dimensional orbit for each maximal cone and positive-dimensional orbits of Euler characteristic zero, hence
$$
\chi_{\mathrm{top}}(X(\CC))=\size\Sigma(2)=d.
$$
Noether's formula therefore gives
$$
K_X^2+\chi_{\mathrm{top}}(X(\CC))=12\chi(\OO_X)=12,
$$
again yielding $K_X^2=12-d$.

$\PP^2$ has $d = 3$ and $K^2 = 9$.
Each Hirzebruch surface $\FF_a$ has $d = 4$ and $K^2 = 8$, independent of $a$.
A blowup at a torus-fixed point is a star subdivision that adds one ray, so it decreases $K^2$ by one. For example, the blowups of $\PP^2$ at one, two, and three torus-fixed points have $K^2=8,7,6$ respectively.
The ray count does not characterize the Fano condition: $\FF_a$ has four rays for every $a\ge0$, while $-K_{\FF_a}\cdot S=2-a$ on its negative section $S$, so $\FF_a$ is not Fano for $a\ge2$.
:::
