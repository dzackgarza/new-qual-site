---
schema: qual/card@1
id: P-HCAX29
kind: problem
title: Local power-series expansions of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
---

::: problem
Prove that every holomorphic function has a convergent power-series expansion about each point of its domain.
:::

::: solution
Let $f$ be holomorphic on a domain $\Omega$, and fix $a\in\Omega$. Choose
\[
0<R<\operatorname{dist}(a,\partial\Omega)
\]
so that the closed disk $\overline{D(a,R)}$ lies in $\Omega$.

For $|z-a|<R$, Cauchy's integral formula gives
\[
f(z)=\frac{1}{2\pi i}
\int_{|\zeta-a|=R}\frac{f(\zeta)}{\zeta-z}\,d\zeta.
\]
On the integration circle,
\[
\frac1{\zeta-z}
=\frac1{\zeta-a}
\frac1{1-\frac{z-a}{\zeta-a}}
=\sum_{n=0}^{\infty}
\frac{(z-a)^n}{(\zeta-a)^{n+1}}.
\]
Because
\[
\left|\frac{z-a}{\zeta-a}\right|=\frac{|z-a|}{R}<1,
\]
this geometric series converges uniformly on the contour, so it may be integrated term by term. Hence
\[
f(z)=\sum_{n=0}^{\infty}a_n(z-a)^n,
\]
where
\[
a_n
=\frac{1}{2\pi i}
\int_{|\zeta-a|=R}
\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta.
\]
By Cauchy's differentiation formula,
\[
a_n=\frac{f^{(n)}(a)}{n!}.
\]

Therefore
\[
\boxed{
f(z)=\sum_{n=0}^{\infty}
\frac{f^{(n)}(a)}{n!}(z-a)^n}
\]
for every $|z-a|<R$. Since $R$ may be any radius smaller than the distance from $a$ to the boundary of the domain, every holomorphic function is analytic at every point of its domain.
:::
