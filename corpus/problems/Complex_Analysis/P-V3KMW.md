---
schema: qual/card@1
id: P-V3KMW
kind: problem
title: The $ML$ estimate for contour integrals and $\left|\int_{|z|=R}\frac{\log z}{z^2}\,dz\right|$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Complex Logarithm
relations: []
review: draft
---

::: {.problem}
Let $f:D\to\CC$ be continuous and let $\alpha:[a,b]\to D$ be a smooth
curve. (a) Define $\int_\alpha f$. (b) If $|f|\le M$ on the image of
$\alpha$, prove
\[
\left|\int_\alpha f\right|\le M\,\operatorname{length}(\alpha).
\]
(c) For $C_R:|z|=R$, $R>1$, give an upper bound for
\[
\left|\int_{C_R}\frac{\log z}{z^2}\,dz\right|,
\]
after fixing a continuous determination of the logarithm along the
parametrized circle.
:::

::: {.solution}
By definition,
\[
\int_\alpha f(z)\,dz
=\int_a^b f(\alpha(t))\alpha'(t)\,dt.
\]
Therefore
\[
\left|\int_\alpha f\right|
\le\int_a^b|f(\alpha(t))|\,|\alpha'(t)|\,dt
\le M\,\operatorname{length}(\alpha).
\]
For $C_R$, use $z=Re^{it}$, $0\le t\le2\pi$, and the continuous lift
$L(t)=\log R+it$ along this parametrization. Then
\[
|L(t)|\le\log R+2\pi,
\qquad |z|=R,
\]
so the $ML$ estimate yields
\[
\left|\int_{C_R}\frac{L(z)}{z^2}\,dz\right|
\le \frac{2\pi}{R}(\log R+2\pi).
\]
There is no single-valued holomorphic logarithm on a neighborhood of the full
circle, so a determination along the parametrized contour is part of the data
needed to interpret the last integral.
:::