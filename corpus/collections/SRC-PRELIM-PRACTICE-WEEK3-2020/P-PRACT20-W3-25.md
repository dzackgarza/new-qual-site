---
schema: qual/card@1
id: P-PRACT20-W3-25
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 25"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
For $a , b > 0$ and $n \in \mathbb { N }$ , define

$$
I _ { n } ( a , b ) = \int _ { 0 } ^ { \pi / 2 } \frac { d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n } } .
$$

Show that

$$
\frac { \partial I _ { n } } { \partial a } + \frac { \partial I _ { n } } { \partial b } + n I _ { n + 1 } = 0 .
$$

Evaluate $I _ { 1 } ( a , b )$ explicitly and use this to evaluate $I _ { 2 } ( a , b )$
:::

::: {.solution}
Differentiating under the integral (legal by Leibniz rule), we find

$$
\frac { \partial I _ { n } } { \partial a } ( a , b ) = - \int _ { 0 } ^ { \pi / 2 } \frac { n \cos ^ { 2 } ( \theta ) d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } } , \quad \frac { \partial I _ { n } } { \partial b } ( a , b ) = - \int _ { 0 } ^ { \pi / 2 } \frac { n \sin ^ { 2 } ( \theta ) d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } }
$$

and so

$$
\frac { \partial I _ { n } } { \partial a } + \frac { \partial I _ { n } } { \partial b } = - n \int _ { 0 } ^ { \pi / 2 } \frac { \cos ^ { 2 } ( x ) + \sin ^ { 2 } ( x ) } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } } d x = - n I _ { n + 1 } .
$$

We can evaluate $I _ { 1 } ( a , b )$ using a u-substitution and trig.
substitution:

$$
\begin{array} { r l } & { I _ { 1 } ( a , b ) = \displaystyle \int _ { 0 } ^ { \pi / 2 } \frac { d u } { \alpha \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) } } \\ & { \quad \quad \quad - \displaystyle \int _ { 0 } ^ { \pi / 2 } \frac { \sec ^ { 2 } ( x ) d x } { \alpha + b \tan ^ { 2 } ( x ) } } \\ & { \quad \quad \quad - \displaystyle \int _ { 0 } ^ { \infty } \frac { d u } { \alpha + b u ^ { 2 } } \qquad [ u - \tan ( x ) ] } \\ & { \quad \quad \quad \quad = \displaystyle \frac { 1 } { \alpha } \int _ { 0 } ^ { \infty } \frac { d u } { 1 + \frac { b } { \alpha } n ^ { 2 } } } \\ & { \quad \quad \quad = \displaystyle \frac { 1 } { \alpha } \cdot \left( \sqrt { \frac { d } { \alpha } } \right) \arctan \left( u \sqrt { \frac { b } { \alpha } } \right) \Big | _ { u = 0 } ^ { n > \infty } } \\ & { \quad \quad \quad = \displaystyle \frac { \pi } { 2 \sqrt { \alpha \delta } } . } \end{array}
$$

Then

$$
I _ { 2 } ( a , b ) = - \frac { \partial I _ { 1 } } { \partial a } ( a , b ) - \frac { \partial I _ { 1 } } { \partial b } ( a , b ) = \frac { \pi } { 4 a \sqrt { a b } } + \frac { \pi } { 4 b \sqrt { a b } } = \frac { \pi } { 4 \sqrt { a b } } \left( \frac { 1 } { a } + \frac { 1 } { b } \right) .
$$
:::
