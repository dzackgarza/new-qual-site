---
schema: qual/card@1
id: P-PRACT20-W3-24
kind: problem
title: The Dirichlet integral $\int_0^\infty\frac{\sin t}{t}\,dt$ by differentiating under the integral
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate $\int _ { 0 } ^ { \infty } \frac { \sin ( t ) } { t } d t$ by differentiating $I ( s ) = \int _ { 0 } ^ { \infty } e ^ { - s t } \frac { \sin ( t ) } { t } d t$ with respect to s.
:::

::: {.solution}
We see

$$
I ^ { \prime } ( s ) = \int _ { 0 } ^ { \infty } { \frac { d } { d s } } e ^ { - s t } { \frac { \sin ( t ) } { t } } d t = - \int _ { 0 } ^ { \infty } e ^ { - s t } \sin ( t ) d t .
$$

Now integrating by parts twice, we see

$$
\begin{array} { r l } { I ^ { \prime } ( s ) = - \displaystyle ( [ - e ^ { - s t } \cos ( t ) ] _ { t = 0 } ^ { t  \infty } - s \int _ { 0 } ^ { \infty } e ^ { - s t } \cos ( t ) d t ) } & { { } } \\ { = - ( 1 - [ s e ^ { - s t } \sin ( t ) ] _ { t = 0 } ^ { t  \infty } - s ^ { 2 } \int _ { 0 } ^ { \infty } e ^ { - s t } \sin ( t ) d t ) } & { { } } \\ { = - 1 - s ^ { 2 } I ^ { \prime } ( s ) } & { { } \Longrightarrow { } \quad I ^ { \prime } ( s ) = - \displaystyle \frac 1 { 1 + s ^ { 2 } } . } \end{array}
$$

Now integrating we see

$$
I ( s ) - I ( 0 ) = \int _ { 0 } ^ { s } I ^ { \prime } ( r ) d r = - \int _ { 0 } ^ { s } { \frac { d r } { 1 + r ^ { 2 } } } = - \arctan ( s ) .
$$

Now lim $_ { 1 _ { s \to \infty } I ( s ) } = 0$ so

$$
\int _ { 0 } ^ { \infty } { \frac { \sin ( t ) } { t } } d t = I ( 0 ) = \operatorname* { l i m } _ { s \to \infty } ( I ( s ) + \arctan ( s ) ) = { \frac { \pi } { 2 } } .
$$

[Note: incidentally this also shows that $\begin{array} { r } { I ( s ) = \frac { \pi } { 2 } - \arctan ( s ) } \end{array}$ is the Laplace transform of $\frac { \sin ( t ) } { t } .$
:::
