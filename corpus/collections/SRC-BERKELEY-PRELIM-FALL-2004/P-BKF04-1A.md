---
schema: qual/card@1
id: P-BKF04-1A
kind: problem
title: UC Berkeley Fall 2004 prelim 1A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Show that there is a unique piecewise continuous function $y ( x )$ on R satisfying the two conditions

$$
\begin{array} { l l l } { { y ( x ) = \displaystyle \int _ { 0 } ^ { \infty } e ^ { - 2 s } y ( x - s ) d s ~ } } & { { \qquad } } & { { \mathrm { f o r ~ } x > 0 , \mathrm { a n d ~ } } } \\ { { y ( x ) = e ^ { x } , ~ } } & { { \qquad } } & { { \mathrm { f o r ~ } x \le 0 , } } \end{array}
$$

and find an explicit formula for $y ( x )$ for $x > 0$
:::

::: {.solution}
Suppose that $y ( x )$ is a solution. For $x > 0$ , the substitution $s = x - t$ yields

$$
\begin{array} { c } { { y ( x ) = \displaystyle \int _ { - \infty } ^ { x } e ^ { - 2 ( x - t ) } y ( t ) d t } } \\ { { e ^ { 2 x } y ( x ) = \displaystyle \int _ { - \infty } ^ { x } e ^ { 2 t } y ( t ) d t . } } \end{array}\tag{1}
$$

The right hand side is continuous as a function of x, so $e ^ { 2 x } y ( x )$ is continuous on $\mathbb { R } _ { > 0 }$ , and multiplying by $e ^ { - 2 x }$ shows that $y ( x )$ is continuous on $\mathbb { R } _ { > 0 }$ . This in turn implies that the right hand side is differentiable, and the same argument now shows that $y ( x )$ is differentiable on ${ \mathbb R } _ { > 0 }$ . Differentiating both sides for $x > 0$ yields

$$
\begin{array} { c } { { e ^ { 2 x } ( y ^ { \prime } + 2 y ) = e ^ { 2 x } y } } \\ { { y ^ { \prime } + 2 y = y } } \\ { { y ^ { \prime } = - y } } \\ { { y = c e ^ { - x } } } \end{array}
$$

for some $c \in \mathbb { R }$ . Substituting this back into (1) yields, for $x > 0$

$$
\begin{array} { c } { { c e ^ { x } = \displaystyle \int _ { - \infty } ^ { 0 } e ^ { 3 t } d t + \int _ { 0 } ^ { x } c e ^ { t } d t } } \\ { { } } \\ { { c e ^ { x } = \displaystyle \frac { 1 } { 3 } + c ( e ^ { x } - 1 ) } } \\ { { } } \\ { { c = \displaystyle \frac { 1 } { 3 } } } \\ { { } } \\ { { y ( x ) = \displaystyle \frac { 1 } { 3 } e ^ { - x } . } } \end{array}
$$

Thus if there is a solution, it must be

$$
y ( x ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { 3 } } e ^ { - x } } & { { \mathrm { i f ~ } } x > 0 } \\ { e ^ { x } } & { { \mathrm { i f ~ } } x \leq 0 } \end{array} \right. }
$$

Because (1) is equivalent to the integral equation in the original problem, this function indeed satisfies the conditions of the problem.
:::
