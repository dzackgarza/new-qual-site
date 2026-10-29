---
schema: qual/card@1
id: T-GROTS
kind: theorem
title: Power series expansion of a holomorphic function on a disc
slogan: 'Holomorphic functions equal their Taylor series throughout every closed disc contained in the domain.'
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
Then for every $z\in D_R(z_0)$ the series below converges and
$$
f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n,
$$
where for every $n\geq0$ and every $r\in(0,R]$,
$$
a_n=\frac{f^{(n)}(z_0)}{n!}=\frac{1}{2\pi i}\int_{\abs{z-z_0}=r}\frac{f(z)}{(z-z_0)^{n+1}}\dz=\frac{1}{2\pi r^n}\int_0^{2\pi}f(z_0+re^{i\theta})e^{-in\theta}\dtheta.
$$
In particular, $f$ is [[D-V6UQJ|analytic]] at every point of $\Omega$ [@SS03].
:::

::: {.remark}
Conversely, a function analytic on $\Omega$ is holomorphic on $\Omega$, since a power series is complex differentiable inside its disc of convergence; so holomorphic and analytic functions on $\Omega$ coincide.
Bounding the last integral by $\max_{\abs{z-z_0}=R}\abs{f}$ gives [[T-22RQZ|Cauchy's inequalities]].
:::
