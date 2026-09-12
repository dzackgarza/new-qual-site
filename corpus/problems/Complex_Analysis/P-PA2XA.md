---
schema: qual/card@1
id: P-PA2XA
kind: problem
title: $\int_T f=0$ when $f$ is holomorphic and bounded near an interior puncture
  of $T$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Morera
  - Contour Integration
relations: []
review: draft
---

::: problem
Suppose that $f$ is holomorphic on a punctured open set $\Omega\setminus\theset{w_0}$ and let $T\subset \Omega$ be a triangle containing $w_0$.
Prove that if $f$ is bounded near $w_0$, then $\int_T f(z) ~dz = 0$.
:::

::: solution
Because $f$ is holomorphic on a punctured neighborhood of $w_0$ and bounded
there, Riemann's removable-singularity theorem gives a holomorphic extension
\[
\widetilde f:\Omega\to\mathbb C.
\]
On the boundary of $T$, the functions $f$ and $\widetilde f$ agree. Therefore,
by Cauchy's theorem on the triangle,
\[
\int_T f(z)\,dz
=\int_{\partial T}\widetilde f(z)\,dz
=0.
\]
Thus the puncture contributes no contour integral when the function is bounded
near it.
:::
