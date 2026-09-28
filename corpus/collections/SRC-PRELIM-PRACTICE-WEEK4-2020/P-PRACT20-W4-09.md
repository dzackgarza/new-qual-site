---
schema: qual/card@1
id: P-PRACT20-W4-09
kind: problem
title: The Bernoulli equation $y'+\frac4xy=x^3y^2$ and the substitution for $y^\alpha$
classification:
  areas:
  - applied-algebra
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
(Bernoulli Equations) Find the general solution of the differential equation $\begin{array} { r } { y ^ { \prime } + \frac { 4 } { x } y = x ^ { 3 } y ^ { 2 } } \end{array}$ by making the substitution $u = 1 / y$ . Can you generalize this substitution so that it would work if $y ^ { 2 }$ on the right hand side was replaced by $y ^ { \alpha }$ for any $\alpha \neq 0 , 1$?
:::

::: {.solution}
We find a differential equation that $u = 1 / y$ satisfies.
Indeed,

$$
u ^ { \prime } = - { \frac { 1 } { y ^ { 2 } } } y ^ { \prime } = - { \frac { 1 } { y ^ { 2 } } } \left( - { \frac { 4 } { x } } y + x ^ { 3 } y ^ { 2 } \right) = { \frac { 4 } { x y } } - x ^ { 3 } = { \frac { 4 } { x } } u - x ^ { 3 } .
$$

This equation is now linear in u. We use an integrating factor:

$$
u ^ { \prime } - { \frac { 4 } { x } } u = - x ^ { 3 } \quad \Longrightarrow \quad { \frac { 1 } { x ^ { 4 } } } u ^ { \prime } - { \frac { 4 } { x ^ { 5 } } } u = - { \frac { 1 } { x } } \quad \Longrightarrow \quad { \frac { d } { d x } } \left[ { \frac { 1 } { x ^ { 4 } } } u \right] = - { \frac { 1 } { x } } .
$$

Integrating gives the general solution

$$
{ \frac { 1 } { x ^ { 4 } } } u ( x ) = C - \log ( x ) \Longrightarrow u ( x ) = C x ^ { 4 } - x ^ { 4 } \log ( x ) .
$$

Thus inverting gives

$$
\boxed { y ( x ) = \frac { 1 } { u ( x ) } = \frac { 1 } { C x ^ { 4 } - x ^ { 4 } \log ( x ) } } .
$$

To answer the last question, consider the equation

$$
y ^ { \prime } + p ( x ) y = q ( x ) y ^ { \alpha } .
$$

We want to make the substitution $u = y ^ { \beta }$ and solve for $\beta$ to linearize the equation.
Indeed, this will give

$$
u ^ { \prime } = \beta y ^ { \beta - 1 } y ^ { \prime } = \beta y ^ { \beta - 1 } { \bigl ( } - p ( x ) y + q ( x ) y ^ { \alpha } { \bigr ) } = - \beta p ( x ) y ^ { \beta } + \beta q ( x ) y ^ { \alpha + \beta - 1 } = - \beta p ( x ) u + \beta q ( x ) y ^ { \alpha + \beta - 1 } .
$$

To eliminate the power of $y ,$ we choose $\beta = 1 - \alpha$ . Thus $u = y ^ { 1 - \alpha }$ satisfies the linear equation

$$
u ^ { \prime } + ( 1 - \alpha ) p ( x ) u = ( 1 - \alpha ) q ( x ) .
$$
:::
