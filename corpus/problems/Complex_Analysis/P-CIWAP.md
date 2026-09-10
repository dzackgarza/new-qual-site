---
schema: qual/card@1
id: P-CIWAP
kind: problem
title: Holomorphic functions on the disk expand as power series uniformly on compact
  subsets
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
---

::: problem
- Show that if $f$ is holomorphic on $\DD$ then $f$ has a power series expansion that converges uniformly on every compact $K\subset \DD$.
:::

::: solution
Write the Taylor expansion at $0$ as
\[
f(z)=\sum_{n=0}^\infty a_nz^n,
\qquad |z|<1.
\]
Let $K\subset\mathbb D$ be compact and choose numbers
\[
r:=\max_{z\in K}|z|<R<1.
\]
If $M_R=\max_{|\zeta|=R}|f(\zeta)|$, Cauchy's estimates give
\[
|a_n|\le\frac{M_R}{R^n}.
\]
Hence for $z\in K$,
\[
|a_nz^n|\le M_R(r/R)^n.
\]
The right-hand side is a summable geometric majorant, so the Weierstrass
$M$-test gives uniform convergence on $K$.
:::
