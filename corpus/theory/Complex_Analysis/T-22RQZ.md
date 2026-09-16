---
schema: qual/card@1
id: T-22RQZ
kind: theorem
title: Cauchy's inequalities
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.theorem ref="CauchyInequality"}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, and let $z_0\in\Omega$ and $R>0$ satisfy $\overline{D_R(z_0)}\subseteq\Omega$.
Let $\gamma$ be the circle $\abs{z-z_0}=R$ and $M\coloneqq\max_{z\in\gamma}\abs{f(z)}$.
Then for every $n\ge0$,
$$
\abs{f^{(n)}(z_0)}\le\frac{n!\,M}{R^n}.
$$
:::

::: {.proof}
By the Cauchy integral formula for derivatives, with $\gamma$ parametrized by $z=z_0+Re^{i\theta}$,
$$
\abs{f^{(n)}(z_0)}=\abs{\frac{n!}{2\pi i}\int_\gamma\frac{f(z)}{(z-z_0)^{n+1}}\dz}\le\frac{n!}{2\pi}\int_0^{2\pi}\frac{M}{R^{n+1}}R\dtheta=\frac{n!\,M}{R^n}.
$$
:::
