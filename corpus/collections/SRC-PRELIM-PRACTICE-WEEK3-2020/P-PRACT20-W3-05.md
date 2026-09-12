---
schema: qual/card@1
id: P-PRACT20-W3-05
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 5"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the value of $\textstyle \sum _ { n = 1 } ^ { \infty } n ^ { 2 } x ^ { n }$ wherever the series converges.
:::

::: {.solution}
The geometric series converges for $| x | < 1 ;$ we can differentiate the series term-by-term without affecting the radius of convergence.
We see

$$
{ \frac { 1 } { 1 - x } } = \sum _ { n = 0 } ^ { \infty } x ^ { n } ,\tag{1}
$$

$$
\implies \frac { 1 } { ( 1 - x ) ^ { 2 } } = \sum _ { n = 1 } ^ { \infty } n x ^ { n - 1 } ,\tag{2}
$$

$$
\implies \frac { 2 } { ( 1 - x ) ^ { 3 } } = \sum _ { n = 2 } ^ { \infty } n ( n - 1 ) x ^ { n - 2 } .\tag{3}
$$

Our original series can be rewritten

$$
\sum _ { n = 1 } ^ { \infty } n ^ { 2 } x ^ { n } = \left( \sum _ { n = 2 } ^ { \infty } n ( n - 1 ) x ^ { n } \right) + \left( \sum _ { n = 1 } ^ { \infty } n x ^ { n } \right) .
$$

These two sums can be evaluated by multiplying (3) by $x ^ { 2 }$ and multiplying (2) by x. Thus

$$
\sum _ { n = 1 } ^ { \infty } n ^ { 2 } x ^ { n } = { \frac { 2 x ^ { 2 } } { ( 1 - x ) ^ { 3 } } } + { \frac { x } { ( 1 - x ) ^ { 2 } } } = { \frac { x + x ^ { 2 } } { ( 1 - x ) ^ { 3 } } } .
$$
:::
