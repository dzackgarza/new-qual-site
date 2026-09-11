---
schema: qual/card@1
id: P-PRACT20-W3-09
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 9"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find $f ^ { ( 1 0 0 ) } ( 2 )$ for $\textstyle f ( x ) = { \frac { 3 } { x ^ { 2 } + 5 x + 4 } }$
:::

::: {.solution}
Using partial fractions, we find

$$
f ( x ) = { \frac { 1 } { 1 + x } } - { \frac { 1 } { 4 + x } } .
$$

At this point you can just start taking derivatives and notice a pattern, or you can expand each term in a Taylor Series about $x = 2$ . I’ll do the latter:

$$
\begin{array} { c } { { f ( x ) = \displaystyle \frac { 1 } { 3 + ( x - 2 ) } - \displaystyle \frac { 1 } { 6 + ( x - 2 ) } = \displaystyle \frac { 1 } { 3 } \left( \displaystyle \frac { 1 } { 1 + \displaystyle \frac { ( x - 2 ) } { 3 } } \right) - \displaystyle \frac { 1 } { 6 } \left( \displaystyle \frac { 1 } { 1 + \displaystyle \frac { ( x - 2 ) } { 6 } } \right) } } \\ { { \displaystyle \qquad = \displaystyle \frac { 1 } { 3 } \sum _ { n = 0 } ^ { \infty } \frac { ( - 1 ) ^ { n } ( x - 2 ) ^ { n } } { 3 ^ { n } } - \displaystyle \frac { 1 } { 6 } \sum _ { n = 0 } ^ { \infty } \frac { ( - 1 ) ^ { n } ( x - 2 ) ^ { n } } { 6 ^ { n } } . } } \end{array}
$$

The $1 0 0 ^ { \mathrm { t h } }$ coefficient is $f ^ { ( 1 0 0 ) } ( 2 ) / 1 0 0 !$ and so $\begin{array} { r } { f ^ { ( 1 0 0 ) } ( 2 ) = 1 0 0 ! \left( \frac { 1 } { 3 ^ { 1 0 1 } } - \frac { 1 } { 6 ^ { 1 0 1 } } \right) \approx 6 . 0 3 6 1 \times 1 0 ^ { 1 0 9 } } \end{array}$
:::
