---
schema: qual/card@1
id: P-PRACT20-W3-15
kind: problem
title: Plane through the origin perpendicular to the intersection line of two planes
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Planes
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the line name ell lost as a backtick and the unit vectors in the displayed determinant, checked against Week3_solns.pdf (Problem 15).
---

::: {.problem}
Let $\ell$ be the line of intersection for the planes $x + y + z = 3$ and $x - y + z = 5$. Find the equation for the plane containing $(0, 0, 0)$ and perpendicular to $\ell$.
:::

::: {.solution}
The planes have normal vectors $(1,1,1)$ and $(1,-1,1)$; the line of intersection is perpendicular to both, so it is parallel to

$$
(1,1,1)\times(1,-1,1)=\determinant{\begin{array}{ccc}\hat\imath&\hat\jmath&\hat k\\1&1&1\\1&-1&1\end{array}}=(2,0,-2).
$$

The new plane has this normal vector and contains the origin, so it is $2x-2z=0$, that is, $\boxed{x=z}$.
:::
