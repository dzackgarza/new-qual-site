---
schema: qual/card@1
id: P-BKS04-7A
kind: problem
title: UC Berkeley Spring 2004 prelim 7A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Evaluate $\int _ { 0 } ^ { \infty } { \frac { \sin { x } } { x } } d x .$
:::

::: {.solution}
For $R > 1$ , let $\gamma _ { 1 }$ be the straight line path from $1 / R$ to $R _ { : }$ , let $\gamma _ { 2 }$ be the straight line path from R to $R + R i$ , let $\gamma _ { 3 }$ be the straight line path from $R + R i { \mathrm { ~ t o ~ } } { - R + R i }$ , let $\gamma _ { 4 }$ be the straight line path from $- R + R i$ to $- R ,$ , let $\gamma _ { 5 }$ be the straight line path from $- R$ to

$- 1 / R$ , and let $\gamma _ { 6 }$ be the upper semicircle from $- 1 / R$ to $1 / R$ given by the parameterization $\gamma _ { 6 } ( t ) = e ^ { i t }$ for t running from $\pi$ to 0. Let $\gamma$ be the closed loop formed by concatenating these six paths.
Cauchy’s Theorem implies that $\begin{array} { r } { \int _ { \gamma } \frac { e ^ { i z } } { z } d z = 0 } \end{array}$

We have

$$
| \int _ { \gamma _ { 2 } } { \frac { e ^ { i z } } { z } } d z | \leq \int _ { 0 } ^ { R } { \frac { e ^ { - t } } { R } } d t = { \frac { 1 - e ^ { - R } } { R } }  0
$$

as $R \to \infty$ . Similarly $\textstyle \int _ { \gamma _ { 4 } } { \frac { e ^ { i z } } { z } } d z \to 0$ , and

$$
| \int _ { \gamma _ { 3 } } { \frac { e ^ { i z } } { z } } d z | \leq \int _ { - R } ^ { R } { \frac { e ^ { - R } } { R } } d t = 2 e ^ { - R }  0 .
$$

On the other hand, $e ^ { i z } z$ differs from $1 / z \ \mathrm { b y }$ a holomorphic function, and $\gamma _ { 6 }$ is shrinking to a point, so

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { \gamma _ { 6 } } \frac { e ^ { i z } } { z } d z = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { \gamma _ { 6 } } \frac { 1 } { z } d z } \\ { = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { \pi } ^ { 0 } \frac { 1 } { ( 1 / R ) e ^ { i t } } ( 1 / R ) i e ^ { i t } d t } \\ { = - \pi i . } \end{array}
$$

Thus

$$
\int _ { \gamma _ { 1 } } { \frac { e ^ { i z } } { z } } d z + \int _ { \gamma _ { 5 } } { \frac { e ^ { i z } } { z } } d z  \pi i
$$

as $R \to \infty$ . Taking imaginary parts and using the fact that $( \sin z ) / z$ is an even function, we find that

$$
2 \int _ { 1 / R } ^ { R } { \frac { \sin z } { z } } d z \to \pi
$$

as $R \to \infty$ . Since $( \sin z ) / z$ is holomorphic, it does not hurt to replace the lower limit $1 / R$ by 0, so $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sin x } { x } } d x = \pi / 2$
:::
