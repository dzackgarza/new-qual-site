---
schema: qual/card@1
id: P-BKF04-8B
kind: problem
title: UC Berkeley Fall 2004 prelim 8B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
$\mathrm { ~ A ~ } C ^ { 2 }$ function $y ( x )$ for $0 \leq x \leq 1$ , a positive continuous function $a ( x )$ for $0 \leq x \leq 1$ and a real number λ satisfy

$$
\begin{array} { r } { y ^ { \prime \prime } ( x ) + \lambda a ( x ) y ( x ) = 0 , } \\ { y ( 0 ) = 0 , } \\ { y ^ { \prime } ( 1 ) = 0 . } \end{array}
$$

Suppose that $y ( x )$ is not identically zero. Prove that $\lambda > 0$
:::

::: {.solution}
Multiply the ODE by $y ( x )$ and integrate from 0 to 1 to get

$$
\begin{array} { r l r } {  { \lambda \int _ { 0 } ^ { 1 } a y ^ { 2 } d x = - \int _ { 0 } ^ { 1 } y y ^ { \prime \prime } d x } } \\ & { } & \\ & { = - y y ^ { \prime } | _ { 0 } ^ { 1 } + \int _ { 0 } ^ { 1 } y ^ { \prime 2 } d x \quad } & { \mathrm { ( i n t e g r a t i o n ~ b y ~ p a r t s , ~ w i t h ~ } u = y , d v = y ^ { \prime \prime } d x \mathrm { ) } } \\ & { } & \\ & { = \displaystyle \int _ { 0 } ^ { 1 } y ^ { \prime 2 } d x } \\ & { } & \\ & { > 0 , } \end{array}
$$

since if $y ^ { \prime }$ were identically zero on [0, 1], then y would be constant on $[ 0 , 1 ]$ , making y identically zero (since $y ( 0 ) = 0 )$ Since $a ~ > ~ 0$ and y is not identically zero, we also have $\begin{array} { r } { \int _ { 0 } ^ { 1 } a y ^ { 2 } d x > 0 } \end{array}$ . Thus λ is a ratio of positive numbers, so $\lambda > 0$
:::
