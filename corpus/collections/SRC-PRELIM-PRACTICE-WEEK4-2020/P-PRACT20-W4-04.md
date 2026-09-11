---
schema: qual/card@1
id: P-PRACT20-W4-04
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 4"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the solution of $x d y + ( y - x e ^ { x } ) d x = 0$ which passes through the point (1, 0).
:::

::: {.solution}
This problem can be re-phrased

$$
x { \frac { d y } { d x } } + y = x e ^ { x } .
$$

The left-hand side is already a perfect derivative:

$$
{ \frac { d } { d x } } \left[ x y ( x ) \right] = x e ^ { x } \Longrightarrow x y ( x ) = x e ^ { x } - e ^ { x } + C \Longrightarrow y ( x ) = e ^ { x } - { \frac { e ^ { x } } { x } } + { \frac { C } { x } } .
$$

Now y(1) = 0 gives C = 0 and so $\boxed { y ( x ) = e ^ { x } - e ^ { x } / x . }$
:::
