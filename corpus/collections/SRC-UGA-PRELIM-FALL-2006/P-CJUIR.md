---
schema: qual/card@1
id: P-CJUIR
kind: problem
title: The line integral $\int_{\partial R} x\,dy+y\,dx$ on the upper region between
  $x^2+y^2=4$ and $(x-1)^2+y^2=1$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $R$ be the planar region between the circles $x^2 + y^2 = 4$ and $(x-1)^2 + y^2 = 1$, and lying in the halfplane $y \ge 0$.
Let $\partial R$ be its boundary, oriented so that $R$ is on its left.
Either using the definition or by applying theorems of Calculus, compute the line integral $$\int_{\partial R} x\, dy + y\, dx .$$
:::

::: solution
The differential form is exact:
\[
x\,dy+y\,dx=d(xy).
\]
Therefore its integral around any closed piecewise smooth curve is zero. Since $\partial R$ is closed,
\[
\int_{\partial R}x\,dy+y\,dx=0.
\]
Equivalently, Green's theorem gives the same result because
\[
\frac{\partial x}{\partial x}-\frac{\partial y}{\partial y}=1-1=0.
\]
:::
