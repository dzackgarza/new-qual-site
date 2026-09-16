---
schema: qual/card@1
id: T-JH6VL
kind: theorem
title: Green's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Integrals
relations:
- kind: variant-of
  target: T-4M73O
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be a bounded open set whose boundary $\partial\Omega$ consists of finitely many piecewise smooth closed curves, oriented positively with respect to $\Omega$, and let $f,g\in C^1(\overline{\Omega})$ be real-valued.
Then
$$
\int_{\partial\Omega}f\,dx+g\,dy=\iint_{\Omega}\Bigl(\frac{\partial g}{\partial x}-\frac{\partial f}{\partial y}\Bigr)\dA.
$$
Equivalently, for the vector field $F\coloneqq(f,g)$ on $\overline{\Omega}$,
$$
\int_{\partial\Omega}F\cdot d\mathbf r=\iint_{\Omega}\curl F\dA,
$$
where $\curl F\coloneqq\frac{\partial g}{\partial x}-\frac{\partial f}{\partial y}$.
:::
