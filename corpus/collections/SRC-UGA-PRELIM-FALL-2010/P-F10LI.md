---
schema: qual/card@1
id: P-F10LI
kind: problem
title: A counterclockwise line integral $\int_C (x^3-y^3)\,dx+(x^3+y^3)\,dy$ is nonnegative
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

::: problem
Prove that $\int_C (x^3 - y^3)\,dx + (x^3 + y^3)\,dy \ge 0$ for every smooth, simple closed curve $C \subset \mathbb{R}^2$, oriented counterclockwise.
:::

::: solution
Set
\[
P(x,y)=x^3-y^3,\qquad Q(x,y)=x^3+y^3.
\]
If $D$ is the bounded region enclosed by the positively oriented smooth simple closed curve $C$, Green's theorem gives
\[
\int_C P\,dx+Q\,dy
=\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA.
\]
Now
\[
\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}
=3x^2-(-3y^2)=3(x^2+y^2)\ge0.
\]
Therefore
\[
\int_C (x^3-y^3)\,dx+(x^3+y^3)\,dy
=3\iint_D(x^2+y^2)\,dA\ge0.
\]
:::
