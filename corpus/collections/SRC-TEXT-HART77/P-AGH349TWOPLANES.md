---
schema: qual/card@1
id: P-AGH349TWOPLANES
kind: problem
title: Two disjointly meeting planes are not a set-theoretic complete intersection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomological Dimension
  - Complete Intersections
  - Affine Space
relations: []
review: draft
---

::: {.problem}
Let $X=\Spec k[x_1, x_2, x_3, x_4]$ be affine four-space over a field $k$.
Let $Y_1$ be the plane $x_1=x_2=0$ and let $Y_2$ be the plane $x_3=x_4=0$.
Show that $Y=Y_1 \union Y_2$ is not a set-theoretic complete intersection in $X$.
Therefore the projective closure $\bar{Y}$ in $\PP_k^4$ is also not a set-theoretic complete intersection.

Hints: Use an affine analogue of (Ex.
4.8e). Then show that $H^2(X-Y, \mco_X) \neq 0$, by using (Ex.
2.3) and (Ex.
2.4). If $P=Y_1 \intersect Y_2$, imitate (Ex.
4.3) to show $H^3(X-P, \mco_X) \neq 0$.
:::
