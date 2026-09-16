---
schema: qual/card@1
id: T-LO7QM
kind: theorem
title: Stokes' theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $M$ be a compact oriented smooth $n$-manifold with boundary $\partial M$, carrying the induced orientation, and let $\omega$ be a smooth $(n-1)$-form on $M$.
Then
$$
\int_{\partial M}\omega=\int_M d\omega.
$$
In particular, let $\Omega\subseteq\CC$ be a bounded open set whose boundary consists of finitely many piecewise smooth closed curves, oriented positively with respect to $\Omega$, and let $f\in C^1(\overline{\Omega})$.
For $\omega=f(z)\dz$ one has $d\omega=\frac{\partial f}{\partial\overline z}\,d\overline z\wedge dz$ and $d\overline z\wedge dz=2i\,dx\wedge dy$, so
$$
\int_{\partial\Omega}f(z)\dz=2i\iint_\Omega\frac{\partial f}{\partial\overline z}\dA.
$$
:::
