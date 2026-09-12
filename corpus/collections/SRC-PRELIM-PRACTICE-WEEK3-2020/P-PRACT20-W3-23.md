---
schema: qual/card@1
id: P-PRACT20-W3-23
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 23"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $D = \{ ( x , y ) \in \mathbb { R } ^ { 2 } : x \geq 0 , y \geq 0 \}$ . Calculate

$$
\int \int _ { D } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y
$$

Use this to evaluate the Gaussian integral $\int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x .$
:::

::: {.solution}
We can calculate the double integral uing polar coordinates:

$$
\iint _ { D } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y = \int _ { 0 } ^ { \pi / 2 } \int _ { 0 } ^ { \infty } e ^ { - r ^ { 2 } } r d r d \theta = { \frac { \pi } { 2 } } ( - { \frac { 1 } { 2 } } e ^ { - r ^ { 2 } } { \bigg | } _ { r = 0 } ^ { r  \infty } ) = { \frac { \pi } { 4 } } .
$$

Now notice that by Fubini’s theorem,

$$
\iint _ { D } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y = \left( \int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x \right) \left( \int _ { 0 } ^ { \infty } e ^ { - y ^ { 2 } } d y \right) = \left( \int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x \right) ^ { 2 }
$$

so

$$
\int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \frac { \sqrt { \pi } } { 2 } } \quad { \mathrm { a n d ~ b y ~ e v e n n e s s } } \quad \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \sqrt { \pi } } .
$$
:::
