---
schema: qual/card@1
id: P-PRACT20-W4-08
kind: problem
title: The Cauchy--Euler equation $2x^2y''+3xy'-15y=0$ and the repeated-root case
classification:
  areas:
  - applied-algebra
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
(Cauchy-Euler Equations) Consider the equation $2 x ^ { 2 } y ^ { \prime \prime } + 3 x y ^ { \prime } - 1 5 y = 0$ for $x > 0$ . Find the general solution by either (1) making the substitution $x = e ^ { t }$ or (2) searching for a solution of the

form $y ( x ) = x ^ { \lambda }$ . If you try the latter, you will arrive at a quadratic polynomial for λ which has two roots.
If the equation were changed so that the polynomial has only one root, you would only find one solution.
How could you adjust to find another linearly independent solution?
:::

::: {.solution}
We’ll do the problem both ways.
First, guessing $y ( x ) = x ^ { \lambda }$ , we find that

$$
2 \lambda ( \lambda - 1 ) x ^ { \lambda } + 3 \lambda x ^ { \lambda } - 1 5 x ^ { \lambda } = 0 .
$$

Since this must hold for all $x ,$ we need $2 \lambda ^ { 2 } + \lambda - 1 5 = 0 \mathrm { ~ s o ~ } ( 2 \lambda - 5 ) ( \lambda + 3 ) = 0$ . Thus the general solution is given by

$$
\boxed { y ( x ) = C _ { 1 } x ^ { 5 / 2 } + C _ { 2 } x ^ { - 3 } } .
$$

Now we do this using the substitution $x = e ^ { t }$ . Indeed, define $Y ( t ) = y ( e ^ { t } )$ . We will find a differential equation for $Y ( t )$ . We see

$$
\begin{array} { l } { { Y ^ { \prime } ( t ) = e ^ { t } y ^ { \prime } ( e ^ { t } ) , } } \\ { { Y ^ { \prime \prime } ( t ) = e ^ { 2 t } y ^ { \prime \prime } ( e ^ { t } ) + e ^ { t } y ^ { \prime } ( e ^ { t } ) . } } \end{array}
$$

Thus

$$
2 Y ^ { \prime \prime } ( t ) + Y ^ { \prime } ( t ) = 2 ( e ^ { t } ) ^ { 2 } y ( e ^ { t } ) + 3 e ^ { t } y ^ { \prime } ( e ^ { t } ) = 1 5 y ( e ^ { t } ) = 1 5 Y ( t ) .
$$

Now we can solve for $Y ( t )$ by guessing $Y ( t ) = e ^ { r t }$ and we’ll find $r ^ { 2 } + r - 1 5 = 0 \mathrm { ~ s o ~ } r = 5 / 2 , - 3$ just as λ did above.
Thus

$$
Y ( t ) = C _ { 1 } e ^ { \frac { 5 } { 2 } t } + C _ { 2 } e ^ { - 3 t } \implies \Big \lvert \ y ( x ) = Y ( \log ( x ) ) = C _ { 1 } x ^ { 5 / 2 } + C _ { 2 } x ^ { - 3 } . \Big \rvert
$$

This latter method was a bit more complicated, but it helps answer the last question: what if we had a repeated root for $\lambda ?$ In this case, we would transform the equation and find that the differential equation for $Y ( t )$ has a characteristic polynomial $( r - r _ { 1 } ) ^ { 2 } = 0$ and the solution would be

$$
Y ( t ) = C _ { 1 } e ^ { r _ { 1 } t } + C _ { 2 } t e ^ { r _ { 1 } t } \quad \Longrightarrow \quad \left| y ( x ) = Y ( \log ( x ) ) = C _ { 1 } x ^ { r _ { 1 } } + C _ { 2 } x ^ { r _ { 1 } } \log ( x ) . \right|
$$
:::
