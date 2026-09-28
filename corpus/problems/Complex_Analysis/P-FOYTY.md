---
schema: qual/card@1
id: P-FOYTY
kind: problem
title: A power series may be re-expanded about any point of its disk of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be a power series centered at the origin.
Prove that $f$ has a power series expansion about any point in its disc of convergence.
:::

::: {.solution}
Suppose
\[
f(z)=\sum_{n=0}^\infty a_nz^n
\]
has radius of convergence $R>0$, and let $z_0$ satisfy $|z_0|<R$. Then the
sum $f$ is holomorphic on $D(0,R)$. Choose
\[
0<\rho<R-|z_0|.
\]
By Cauchy's formula, for $|z-z_0|<\rho$,
\[
f(z)=\sum_{k=0}^\infty
\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k.
\]
Indeed, taking any circle $|\zeta-z_0|=s$ with
$|z-z_0|<s<R-|z_0|$, expand
\[
\frac1{\zeta-z}
=\frac1{\zeta-z_0}
\sum_{k=0}^\infty
\left(\frac{z-z_0}{\zeta-z_0}\right)^k
\]
uniformly on the circle and insert this into Cauchy's integral formula. Thus
$f$ has a power-series expansion about every point of its original disk of
convergence.
:::
