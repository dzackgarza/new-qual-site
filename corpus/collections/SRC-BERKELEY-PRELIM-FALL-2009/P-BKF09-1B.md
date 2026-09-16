---
schema: qual/card@1
id: P-BKF09-1B
kind: problem
title: Convergence of the improper integral $\int_1^\infty x^2\cos(x^\beta)\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the real values of $\beta$for which the following limit exists and is finite:$$\operatorname* { l i m } _ { R \to \infty } \int _ { 1 } ^ { R } x ^ { 2 } \cos ( x ^ { \beta } ) d x .$$
:::

::: {.solution}
When $\beta \leq 0$, cos(xβ) tends to a positive limit as$x \to \infty$, and hence$$\operatorname* { l i m } _ { R \to \infty } \int _ { 1 } ^ { R } x ^ { 2 } \cos ( x ^ { \beta } ) d x = \infty .$$When$\beta > 0$, write the integral as$\begin{array} { r } { I ( R ) : = \beta ^ { - 1 } \int _ { 1 } ^ { R } x ^ { 3 - \beta } d \sin ( x ^ { \beta } ) } \end{array}$.
When$0 < \beta \le 3$, the limit does not exist, since the differences$I ( ( 2 \pi k + \pi / \bar { 2 } ) ^ { 1 / \beta } ) - I ( ( 2 \pi k - \pi / 2 ) ^ { 1 / \beta } )$do not tend to 0 as$k \to \infty$.
When$\beta > 3$, integration by parts shows that$$I ( R ) = \mathrm { c o n s t } + \mathrm { c o n s t } R ^ { 3 - \beta } \mathrm { s i n } ( R ^ { \beta } ) + \mathrm { c o n s t } \int _ { 1 } ^ { R } x ^ { 2 - \beta } \mathrm { s i n } ( x ^ { \beta } ) d x .$$The integral on the right has a limit since$\sin ( x ^ { \beta } )$is bounded, and$\int _ { 1 } ^ { \infty } x ^ { 2 - \beta } d x$converges absolutely when$2 - \beta < - 1$.
The finite terms have a limit since$R ^ { 3 - \beta } \stackrel { \circ } { \to } 0$.
Therefore, when$\beta > 3$, the limit of$I ( R )$ exists and is finite.
:::
