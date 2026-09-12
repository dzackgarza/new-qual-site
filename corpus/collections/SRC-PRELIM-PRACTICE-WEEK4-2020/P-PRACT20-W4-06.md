---
schema: qual/card@1
id: P-PRACT20-W4-06
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 6"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the general solution of $y ^ { \prime \prime \prime } - 3 y ^ { \prime \prime } + 3 y ^ { \prime } - y = 0$
:::

::: {.solution}
Guessing $y ( x ) = e ^ { r x }$ , we have $r ^ { 3 } - 3 r ^ { 2 } + 3 r - 1 = 0$ which implies $( r - 1 ) ^ { 3 } = 0$ . This equation has a triple root at $r = 1$ , so the general solution is

$$
\boxed { y ( x ) = C _ { 0 } e ^ { x } + C _ { 1 } x e ^ { x } + C _ { 2 } x ^ { 2 } e ^ { x } . }
$$
:::
