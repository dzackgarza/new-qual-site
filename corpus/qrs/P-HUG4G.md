---
schema: qual/card@1
id: P-HUG4G
kind: problem
title: Cauchy's theorem via Green's theorem, and Goursat's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Cauchy Integral Theorem
  - Contour Integration
relations: []
review: draft
---

::: problem
Suppose $f\in C_\CC^1(\Omega)$ and $T\subset \Omega$ is a triangle with $T^\circ \subset \Omega$.
1. Apply Green's theorem to show that $\int_T f(z) ~dz = 0$.

2. Assume that $f'$ is continuous and prove Goursat's theorem.

> Hint: Green's theorem states
\[
\int_{T} F d x+G d y=\int_{T^\circ}\left(\frac{\partial G}{\partial x}-\frac{\partial F}{\partial y}\right) d x d y
.\]
:::
