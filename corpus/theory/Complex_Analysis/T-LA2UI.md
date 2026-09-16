---
schema: qual/card@1
id: T-LA2UI
kind: theorem
title: Cauchy integral formula
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Power Series
  - Contour Integration
relations: []
review: draft
---

::: {.theorem ref="CauchyIntegral"}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, and let $z_0\in\Omega$ and $R>0$ satisfy $\overline{D_R(z_0)}\subseteq\Omega$.
Let $\gamma\coloneqq\partial D_R(z_0)$, oriented counterclockwise.
Then for every $n\geq0$,
$$
f^{(n)}(z_0)=\frac{n!}{2\pi i}\int_\gamma\frac{f(\xi)}{(\xi-z_0)^{n+1}}\dxi,
$$
and in particular $f(z_0)=\frac{1}{2\pi i}\int_\gamma\frac{f(\xi)}{\xi-z_0}\dxi$.
Consequently, the coefficients of the Taylor expansion $f(z)=\sum_{k\geq0}c_k(z-z_0)^k$ at $z_0$ are
$$
c_k=\frac{f^{(k)}(z_0)}{k!}=\frac{1}{2\pi i}\int_\gamma\frac{f(\xi)}{(\xi-z_0)^{k+1}}\dxi.
$$
:::
