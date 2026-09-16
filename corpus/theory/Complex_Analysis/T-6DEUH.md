---
schema: qual/card@1
id: T-6DEUH
kind: theorem
title: Cauchy integral formula on a disc
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations:
- kind: variant-of
  target: T-LA2UI
review: draft
---

::: {.theorem ref="CauchyIntegral"}
Let $\Omega\subseteq\CC$ be open and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$.
Let $z_0\in\Omega$ and $R>0$ satisfy $\overline{D_R(z_0)}\subseteq\Omega$, and let $\gamma=\bd D_R(z_0)$ be the positively oriented circle.
Then
$$
f(z_0)=\frac{1}{2\pi i}\int_\gamma\frac{f(\xi)}{\xi-z_0}\dxi,
$$
and for every $n\ge0$,
$$
f^{(n)}(z_0)=\frac{n!}{2\pi i}\int_\gamma\frac{f(\xi)}{(\xi-z_0)^{n+1}}\dxi.
$$
:::
