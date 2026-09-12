---
schema: qual/card@1
id: P-PRACT20-W3-01
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 1"
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
