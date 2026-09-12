---
schema: qual/card@1
id: P-PRACT20-W3-26
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 26"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let C be the ellipse given by $( x / a ) ^ { 2 } + ( y / b ) ^ { 2 } = 1$ (where $a , b > 0 )$ . Calculate

$$
\oint _ { \mathcal { C } } ( - y ) d x + x d y .
$$
:::

::: {.solution}
This is a classic Green’s theorem problem.
Rather than try to perform the line integral, we should translate this into an area integral over the shape bounded by the curve and then integrate with the polar transform $x = a r \cos ( \theta ) , y = b r \sin ( \theta )$

$$
\oint _ { \mathcal { C } } ( - y ) d x + x d y = \int _ { D } 2 d x d y = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 1 } 2 a b r d r d \theta = 2 \pi a b .
$$
:::
