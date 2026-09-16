---
schema: qual/card@1
id: T-B3BDO
kind: theorem
title: Goursat's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Theorem
  - Contour Integration
  - Holomorphic Functions
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, and let $T\subseteq\Omega$ be a closed triangle whose interior is also contained in $\Omega$.
Then the integral of $f$ over the boundary of $T$ vanishes:
$$
\int_{\bd T}f(z)\dz=0.
$$
:::

::: {.remark}
This is [@SS03].
The hypothesis is complex differentiability of $f$ at every point of $\Omega$; continuity of $f'$ is not assumed, and the proof proceeds by repeated subdivision of $T$ into four similar triangles.
Goursat's theorem gives primitives of holomorphic functions on discs, and from these follow Cauchy's theorem for toy contours, the Cauchy integral formula, and the power series expansion of holomorphic functions.
:::
