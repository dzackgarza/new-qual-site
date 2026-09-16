---
schema: qual/card@1
id: T-GROTS
kind: theorem
title: Power series expansion of a holomorphic function on a disc
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, and let $z_0\in\Omega$ and $R>0$ satisfy $\overline{D_R(z_0)}\subseteq\Omega$.
Then for every $z\in D_R(z_0)$,
$$
f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n,
$$
where for every $n\geq0$ and every $r\in(0,R]$,
$$
a_n=\frac{f^{(n)}(z_0)}{n!}=\frac{1}{2\pi r^n}\int_0^{2\pi}f(z_0+re^{i\theta})e^{-in\theta}\dtheta.
$$
:::
