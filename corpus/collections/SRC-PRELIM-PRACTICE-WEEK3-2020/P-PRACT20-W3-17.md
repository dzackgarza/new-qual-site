---
schema: qual/card@1
id: P-PRACT20-W3-17
kind: problem
title: Point on the plane $2x+y+3z=3$ closest to the origin
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the point on the plane $2 x + y + 3 z = 3$ which is closest to the origin.
:::

::: {.solution}
We need to minimize $f ( x , y , z ) = x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ subject to $g ( x , y , z ) : = 2 x + y + 3 z - 3 = 0$ A Lagrange multiplier suggests the relationships

$$
2 x = 2 \lambda , 2 y = \lambda , 2 z = 3 \lambda .
$$

Plugging these into the constraint, we find $\lambda = 3 / 7$ and so the point is $\boxed{(6/14, 3/14, 9/14)}$.

Equivalently, the closest point is the multiple $t(2,1,3)$ of the normal vector that lies in the plane: $14t = 3$ gives $t = 3/14$.
:::
