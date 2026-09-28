---
schema: qual/card@1
id: P-PRACT20-W3-04
kind: problem
title: Binomial series for $(1+x)^\alpha$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\alpha \in \mathbb { R }$ . Find the Taylor Series for $( 1 + x ) ^ { \alpha }$ around $x = 0$
:::

::: {.solution}
We see

$$
f ^ { ( k ) } ( x ) = \alpha ( \alpha - 1 ) \cdots ( \alpha - ( k - 1 ) ) ( 1 + x ) ^ { \alpha - k }
$$

and so the Taylor series is given by

$$
f ( x ) = 1 + \alpha x + { \frac { \alpha ( \alpha - 1 ) } { 2 } } x ^ { 2 } + { \frac { \alpha ( \alpha - 1 ) ( \alpha - 2 ) } { 6 } } x ^ { 3 } + \cdots = \sum _ { k = 0 } ^ { \infty } \left( \prod _ { \ell = 0 } ^ { k - 1 } ( \alpha - \ell ) \right) { \frac { x ^ { k } } { k ! } }
$$

where the empty product is 1 by convention.
[Notice that if $\alpha \in \mathbb { N }$ , the coefficients are eventually zero; this fits our intuition because in this case f is a polynomial whose Taylor series should have a finite number of non-zero terms.]
:::
