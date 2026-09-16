---
schema: qual/card@1
id: T-5BLYU
kind: theorem
title: Mean value property for holomorphic functions
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

::: {.proof}
The Cauchy integral formula on the circle $z=z_0+\rho e^{i\theta}$, $0<\rho\le r$, gives
$$
f(z_0)=\frac{1}{2\pi i}\int_0^{2\pi}\frac{f(z_0+\rho e^{i\theta})}{\rho e^{i\theta}}\,i\rho e^{i\theta}\dtheta=\frac{1}{2\pi}\int_0^{2\pi}f(z_0+\rho e^{i\theta})\dtheta.
$$
Multiplying by $\rho$ and integrating over $0\le\rho\le r$ in polar coordinates gives $\frac{r^2}{2}f(z_0)=\frac{1}{2\pi}\iint_{D_r(z_0)}f\dA$.
:::
