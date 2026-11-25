---
schema: qual/card@1
id: T-QDRTC
kind: theorem
title: Quadratic formula over $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomials
  - Complex Numbers
relations: []
review: draft
---

::: {.theorem}
Let $a,b,c\in\CC$ with $a\neq0$, and let $\Delta=b^2-4ac$.
The roots of $az^2+bz+c$ are
$$
\frac{-b\pm w}{2a},
$$
where $w$ is either square root of $\Delta$.
The two roots coincide exactly when $\Delta=0$; over $\CC$ the discriminant always has a square root.

The existence of the square root is [@Ahl73, ch. 1, §1.2, Square Roots], which solves $(x+iy)^2=\alpha+i\beta$ for every complex $\alpha+i\beta$; the formula is completing the square.
:::
