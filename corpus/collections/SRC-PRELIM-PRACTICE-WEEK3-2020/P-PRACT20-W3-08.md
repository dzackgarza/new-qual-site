---
schema: qual/card@1
id: P-PRACT20-W3-08
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 8"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Assume that $\textstyle f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ converges on $( - 1 , 1 )$ . Find the Maclaurin series for $g ( x ) = f ( x ) / ( 1 - x )$
:::

::: {.solution}
Let $\textstyle g ( x ) = \sum _ { n = 0 } ^ { \infty } b _ { n } x ^ { n }$ . Then

$$
f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n } = ( 1 - x ) \sum _ { n = 0 } ^ { \infty } b _ { n } x ^ { n } = b _ { 0 } + \sum _ { n = 1 } ^ { \infty } ( b _ { n } - b _ { n - 1 } ) x ^ { n } .
$$

Thus $b _ { 0 } = a _ { 0 }$ and $b _ { n } = a _ { n } + b _ { n - 1 }$ . From this we see $b _ { 1 } = a _ { 1 } + a _ { 0 } , b _ { 2 } = a _ { 2 } + ( a _ { 1 } + a _ { 0 } )$ and by a quick induction $b _ { k } = a _ { k } + \cdot \cdot \cdot + a _ { 1 } + a _ { 0 }$ . Hence

$$
g ( x ) = \sum _ { n = 0 } ^ { \infty } \left( \sum _ { k = 0 } ^ { n } a _ { k } \right) x ^ { n } .
$$

Note: more generally, if two power series converge in the same interval, their product will also converge on that interval and you can multiply them using the Cauchy formula for the product of infinite sums:

$$
\left( \sum _ { n = 0 } ^ { \infty } c _ { n } x ^ { n } \right) \left( \sum _ { n = 0 } ^ { \infty } d _ { n } x ^ { n } \right) = \sum _ { n = 0 } ^ { \infty } \left( \sum _ { k = 0 } ^ { n } c _ { k } d _ { n - k } \right) x ^ { n } .
$$

This formula (along with the binomial formula) is used in proving that $e ^ { x + y } = e ^ { x } e ^ { y }$ for $x , y \in \mathbb { R }$
:::
