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
Write $D_i^2 = -a_i$ with $\sum_i a_i = 3d - 12$, and $K_X = -\sum_i D_i$ [Cox--Little--Schenck, *Toric Varieties*, Theorem 8.2.3].
Adjacent divisors meet once and non-adjacent ones not at all [*ibid.*, Theorem 10.4.4(b)], so the cross terms contribute $2d$:
$$
K_X^2 = \Big( \sum_i D_i \Big)^2 = \sum_i D_i^2 + 2 \sum_i D_i \cdot D_{i+1} = -\sum_i a_i + 2d = -(3d - 12) + 2d = 12 - d .
$$
:::

::: {.remark title="The sum rule $\sum_i a_i=3d-12$"}
The sum rule used in the proof does not need Noether's formula, and is proved here.
By the classification of smooth complete toric surfaces [*ibid.*, Theorem 10.4.3] — the statement of [[T-TORSURF]] — $X$ is $\PP^2$ or $\FF_a$, or is obtained from one of these by blowups at torus-fixed points.
For $\PP^2$ the $a_i$ are $-1,-1,-1$, with sum $-3=3\cdot3-12$. For $\FF_a$ they are $a,0,-a,0$, with sum $0=3\cdot4-12$. Here $a_i = -D_i^2$ is the integer of the wall relation $v_{i-1}+v_{i+1}=a_iv_i$ of [*ibid.*, Lemma 10.4.1 and Theorem 10.4.4(a)].
A blowup at the fixed point of the cone spanned by $v_i,v_{i+1}$ inserts the ray $w=v_i+v_{i+1}$. The new ray has coefficient $1$, since $v_i+v_{i+1}=1\cdot w$. Each of the two neighbours gains $1$, since $v_{i-1}+w=(a_i+1)v_i$ and $w+v_{i+2}=(a_{i+1}+1)v_{i+1}$. So $d$ grows by $1$ and $\sum_i a_i$ grows by $3$.
:::

::: {.remark}
Over $k=\CC$, the same equality follows from Noether's formula [@Har77, Example A.4.1.2]. A smooth complete toric surface is rational, so $\chi(\OO_X)=1$; its torus-orbit decomposition has one zero-dimensional orbit for each maximal cone and positive-dimensional orbits of Euler characteristic zero, hence
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
