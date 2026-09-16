---
schema: qual/card@1
id: P-PRACT20-W3-22
kind: problem
title: Integrating $e^{y^2}$ over a triangle by reversing the order of integration
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the integral of $f ( x , y ) = e ^ { y ^ { 2 } }$ over the triangular region bounded by the graph of $y = | x |$ for $x \in [ - 2 , 2 ]$ and the line $y = 2$
:::

::: {.solution}
We should integrate in x first since $e ^ { y ^ { 2 } }$ doesn’t have an elementary antiderivative.
The integral is given by

$$
\int _ { 0 } ^ { 2 } \int _ { - y } ^ { y } e ^ { y ^ { 2 } } d x d y = \int _ { 0 } ^ { 2 } 2 y e ^ { y ^ { 2 } } d y = e ^ { y ^ { 2 } } { \biggl | } _ { y = 0 } ^ { y = 2 } = e ^ { 4 } - 1 .
$$
:::
