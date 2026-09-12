---
schema: qual/card@1
id: E-BSL3Q
kind: problem
title: Power series of holomorphic functions on the disk converge uniformly on compacta
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

::: {.exercise}
Show that if $f$ is holomorphic on $\DD$ then $f$ has a power series expansion that converges uniformly on every compact $K\subset \DD$.
:::

::: solution
Since $f$ is holomorphic on $\mathbb D$, its Taylor series at $0$ has radius of
convergence at least $1$:
\[
f(z)=\sum_{n=0}^\infty a_nz^n,
\qquad |z|<1.
\]
Let $K\subset\mathbb D$ be compact. Then
\[
r:=\max_{z\in K}|z|<1.
\]
Choose $R$ with $r<R<1$ and put
\[
M_R:=\max_{|\zeta|=R}|f(\zeta)|.
\]
Cauchy's estimate gives $|a_n|\le M_R/R^n$. Hence for $z\in K$,
\[
|a_nz^n|\le M_R(r/R)^n.
\]
The geometric series on the right converges, so the Weierstrass $M$-test
shows that the Taylor series converges uniformly on $K$.
:::
