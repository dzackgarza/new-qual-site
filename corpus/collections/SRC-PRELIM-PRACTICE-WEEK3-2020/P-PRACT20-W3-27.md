---
schema: qual/card@1
id: P-PRACT20-W3-27
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 27"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let C be the triangle with vertices (0, 0), (1, 0), (1, 2). Find the path integral of $\mathbf { F } ( x , y ) = ( x y , x ^ { 2 } y ^ { 3 } )$ around this curve.
:::

::: {.solution}
This is another classic Green’s theorem problem.
We see

$$
\int _ { \mathcal { C } } \mathbf { F } \cdot d \mathbf { r } = \int _ { D } ( 2 x y ^ { 3 } - x ) d x d y = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 2 x } ( 2 x y ^ { 3 } - x ) d y d x = \int _ { 0 } ^ { 1 } ( 8 x ^ { 5 } - 2 x ^ { 2 } ) d x = { \frac { 4 } { 3 } } - { \frac { 2 } { 3 } } = { \frac { 2 } { 3 } } .
$$
:::
