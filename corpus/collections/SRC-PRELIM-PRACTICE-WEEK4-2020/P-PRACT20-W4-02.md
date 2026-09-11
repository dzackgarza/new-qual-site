---
schema: qual/card@1
id: P-PRACT20-W4-02
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 2"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Solve the initial value problem $y ^ { \prime } + x y = x , y ( 0 ) = - 1$
:::

::: {.solution}
The integrating factor here is $\mu ( x ) = e ^ { \int x d x } = e ^ { x ^ { 2 } / 2 }$ . We see

$$
e ^ { x ^ { 2 } / 2 } y ^ { \prime } + x e ^ { x ^ { 2 } / 2 } y = x e ^ { x ^ { 2 } / 2 } \implies \frac { d } { d x } \left[ e ^ { x ^ { 2 } / 2 } y ( x ) \right] = x e ^ { x ^ { 2 } / 2 } \implies e ^ { x ^ { 2 } / 2 } y ( x ) - y ( 0 ) = e ^ { x ^ { 2 } / 2 } - 1 .
$$

Thus

$$
\boxed { y ( x ) = 1 - 2 e ^ { - x ^ { 2 } / 2 } . }
$$
:::
