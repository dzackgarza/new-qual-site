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

Plugging these into the constraint, we find $\lambda = 3 / 7$ and so the point is given by $( 6 / 1 4 , 3 / 1 4 , 9 / 1 4 )$ [Note: as a shortcut, you could reason that the closest point to the origin is found by travelling from the origin in the direction normal to the plane until you hit the plane. The normal direction here is (2, 1, 3) so you simply need to scale this vector to lie in the plane.]
:::
