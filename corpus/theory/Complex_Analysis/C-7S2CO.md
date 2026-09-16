---
schema: qual/card@1
id: C-7S2CO
kind: corollary
title: Cauchy integral formula for Taylor coefficients and the Cauchy estimates
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Cauchy Integral Formula
  - Cauchy Estimates
  - Power Series
relations: []
review: draft
---

::: {.corollary}
Let $f$ be [[D-E7A5W|holomorphic]] on an open set containing the closed disc $\overline{D_R(p)}$, and write $f(z)=\sum_{k\ge0}c_k(z-p)^k$ near $p$.
Then for every $k\ge0$,
$$
c_k=\frac{f^{(k)}(p)}{k!}=\frac{1}{2\pi i}\int_{\abs{z-p}=R}\frac{f(z)}{(z-p)^{k+1}}\dz=\frac{1}{2\pi R^k}\int_0^{2\pi}f(p+Re^{i\theta})e^{-ik\theta}\dtheta.
$$
Consequently, with $M_R\coloneqq\max_{\abs{z-p}=R}\abs{f(z)}$,
$$
\abs{c_k}\le\frac{M_R}{R^k},
$$
so $\limsup_k\abs{c_k}^{1/k}\le1/R$, and the Taylor series of $f$ at $p$ converges on $D_R(p)$, where it equals $f$.
:::

::: {.proof}
Differentiating the Cauchy integral formula $f(w)=\frac{1}{2\pi i}\int_{\abs{z-p}=R}\frac{f(z)}{z-w}\dz$ under the integral sign $k$ times at $w=p$ gives the first two equalities.
Parametrizing the circle by $z=p+Re^{i\theta}$, so that $\dz=iRe^{i\theta}\dtheta$, gives the third.
Bounding the integrand of the third expression by $M_R/R^k$ over an interval of length $2\pi$ gives the estimate, and the root test gives the radius of convergence.
:::
