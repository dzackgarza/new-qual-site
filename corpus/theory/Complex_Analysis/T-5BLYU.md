---
schema: qual/card@1
id: T-5BLYU
kind: theorem
title: Mean value property for holomorphic functions
slogan: 'The value of a holomorphic function at the center of a closed disc in its domain equals its average over the boundary circle and its average over the disc.'
classification:
  areas:
  - complex-analysis
  topics:
  - Mean Value Property
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.theorem}
Let $f$ be [[D-E7A5W|holomorphic]] on an open set containing the closed disc $\overline{D_r(z_0)}$.
Then
$$
f(z_0)=\frac{1}{2\pi}\int_0^{2\pi}f(z_0+re^{i\theta})\dtheta=\frac{1}{\pi r^2}\iint_{D_r(z_0)}f(z)\dA.
$$
The same identities hold for $u=\Re f$ in place of $f$, by taking real parts.
:::
