---
schema: qual/card@1
id: T-4XPWL
kind: theorem
title: Laurent expansion on an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Principal Parts
  - Singularities
relations: []
review: draft
---

::: {.theorem}
Let $z_0\in\CC$, $0\le r<R\le\infty$, and let $f$ be [[D-E7A5W|holomorphic]] on the annulus
$$
A\coloneqq\ts{z\in\CC\st r<\abs{z-z_0}<R}.
$$
Then $f$ has a two-sided expansion
$$
f(z)=\sum_{n\in\ZZ}c_n(z-z_0)^n
$$
converging [[D-AIQG3|locally uniformly]] on $A$, with coefficients
$$
c_n=\frac{1}{2\pi i}\int_{\abs{z-z_0}=\rho}\frac{f(z)}{(z-z_0)^{n+1}}\dz
$$
for any $r<\rho<R$, independent of $\rho$.
The expansion is unique.

If $r=0$, so that $z_0$ is an [[D-IWIA5|isolated singularity]] of $f$, then the [[D-C3JIU|principal part]] $\sum_{n<0}c_n(z-z_0)^n$ has no nonzero terms if and only if $z_0$ is [[D-BQLJV|removable]], finitely many if and only if $z_0$ is a [[D-R4BDD|pole]], and infinitely many if and only if $z_0$ is [[D-VKP6N|essential]].
:::

::: {.concept}
See Ahlfors, *Complex Analysis*, ch. 5 §1.3, p. 184.
:::
