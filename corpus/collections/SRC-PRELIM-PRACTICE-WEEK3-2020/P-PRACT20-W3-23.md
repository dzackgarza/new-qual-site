---
schema: qual/card@1
id: P-PRACT20-W3-23
kind: problem
title: The Gaussian integral via polar coordinates
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $D = \{ (x, y) \in \RR^{2} : x \geq 0, y \geq 0 \}$. Calculate
$$
\iint_{D} e^{-(x^{2} + y^{2})}\, dx\, dy.
$$
Use this to evaluate the Gaussian integral $\int_{-\infty}^{\infty} e^{-x^{2}}\, dx$.
:::

::: {.solution}
In polar coordinates,

$$
\iint _ { D } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y = \int _ { 0 } ^ { \pi / 2 } \int _ { 0 } ^ { \infty } e ^ { - r ^ { 2 } } r d r d \theta = { \frac { \pi } { 2 } } ( - { \frac { 1 } { 2 } } e ^ { - r ^ { 2 } } { \evalfrom } _ { r = 0 } ^ { r \to \infty } ) = { \frac { \pi } { 4 } } .
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
