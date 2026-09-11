---
schema: qual/card@1
id: P-PRACT20-W3-07
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 7"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the Taylor Series for $\begin{array} { r } { f ( x ) = \int _ { 0 } ^ { x } \frac { \sin ( t ) } { t } d t } \end{array}$ about $x = 0$
:::

::: {.solution}
Starting with the Taylor Series for sin(t), dividing by t and then integrating, we have

$$
\sin ( t ) = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } t ^ { 2 n + 1 } } { ( 2 n + 1 ) ! } } \quad \Longrightarrow \quad { \frac { \sin ( t ) } { t } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } t ^ { 2 n } } { ( 2 n + 1 ) ! } } \quad \Longrightarrow \quad f ( x ) = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } x ^ { 2 n + 1 } } { ( 2 n + 1 ) ! ( 2 n + 1 ) } } .
$$
:::
