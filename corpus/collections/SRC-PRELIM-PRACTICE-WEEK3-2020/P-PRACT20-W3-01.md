---
schema: qual/card@1
id: P-PRACT20-W3-01
kind: problem
title: Closed form for the derivative of $\sum_{n\ge1}(-1)^nx^{3n}$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose $\textstyle f ( x ) = \sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } x ^ { 3 n }$ for $x \in ( - 1 , 1 )$ . Find a closed form for $f ^ { \prime } ( x )$
:::

::: {.solution}
This is a geometric series (with the first term missing).
Thus

$$
f ( x ) + 1 = \sum _ { n = 0 } ^ { \infty } ( - x ^ { 3 } ) ^ { n } = { \frac { 1 } { 1 + x ^ { 3 } } } \quad \Longrightarrow \quad f ^ { \prime } ( x ) = - { \frac { 3 x ^ { 2 } } { ( 1 + x ^ { 3 } ) ^ { 2 } } } .
$$
:::
