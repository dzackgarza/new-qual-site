---
schema: qual/card@1
id: P-PRACT20-W3-17
kind: problem
title: Point on the plane $2x+y+3z=3$ closest to the origin
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Lagrange Multipliers
relations: []
review: draft
---

::: {.problem}
Find the point on the plane $2 x + y + 3 z = 3$ which is closest to the origin.
:::

::: {.solution}
We need to minimize $f(x,y,z)=x^2+y^2+z^2$ subject to $g(x,y,z):=2x+y+3z-3=0$. The Lagrange condition $\nabla f=\lambda\nabla g$ gives

$$
2x=2\lambda,\qquad 2y=\lambda,\qquad 2z=3\lambda.
$$

Substituting into the constraint gives $7\lambda=3$, so $\lambda=3/7$ and the point is $\boxed{(3/7,\,3/14,\,9/14)}$.

Equivalently, the closest point is the multiple $t(2,1,3)$ of the normal vector that lies in the plane: $14t = 3$ gives $t = 3/14$.
:::
