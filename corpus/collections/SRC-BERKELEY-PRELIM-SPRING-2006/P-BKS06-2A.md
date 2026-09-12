---
schema: qual/card@1
id: P-BKS06-2A
kind: problem
title: UC Berkeley Spring 2006 prelim 2A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Find (with proof) all real numbers c such that the differential equation with boundary conditions

$$
f ^ { \prime \prime } - c f ^ { \prime } + 1 6 f = 0 , \qquad f ( 0 ) = f ( 1 ) = 1
$$

has no solution.
:::

::: {.solution}
First suppose that the characteristic equation $x ^ { 2 } - c x + 1 6 = 0$ has a repeated root. This happens when $c = \pm 8$ . If $c = 8$ , the repeated root is 4, and the general solution to the differential equation without boundary conditions has the form

$$
f ( t ) = ( a t + b ) e ^ { 4 t } .
$$

The boundary conditions impose

$$
\begin{array} { r } { b = 1 } \\ { ( a + b ) e ^ { 4 } = 1 , } \end{array}
$$

and this system has a solution. Similarly, there is a solution in the case $c = - 8$

From now on, we suppose that the complex roots $\alpha , \beta$ of $x ^ { 2 } - c x + 1 6 = 0$ are distinct. Then the general solution is

$$
f ( t ) = a e ^ { \alpha t } + b e ^ { \beta t } ,
$$

where a, $b \in \mathbb { C }$ , and the boundary conditions impose

$$
\begin{array} { r } { a + b = 1 } \\ { a e ^ { \alpha } + b e ^ { \beta } = 1 . } \end{array}\tag{1}
$$

This system is guaranteed to have a solution if $e ^ { \alpha } \neq e ^ { \beta }$ . So assume $e ^ { \alpha } = e ^ { \beta }$ . Then $\alpha - \beta =$ 2πik for some $k \in \mathbb { Z }$ . By interchanging $\alpha , \beta ,$ , we may assume $k > 0$ . On the other hand, by the quadratic formula,

$$
( \alpha - \beta ) ^ { 2 } = c ^ { 2 } - 6 4 .
$$

Thus $4 \pi ^ { 2 } k ^ { 2 } = 6 4 - c ^ { 2 } \leq 6 4$ . The only possibility is $k = 1$ , which leads to $c = \pm { \sqrt { 6 4 - 4 \pi ^ { 2 } } }$ In this case $e ^ { \alpha } = e ^ { \beta }$ , but the common value is not 1, since $e ^ { \alpha } e ^ { \beta } = e ^ { \alpha + \beta } = e ^ { c } \neq e ^ { 0 } = 1$ . So the system (1) has no solution.

Thus the set of values c for which the differential equation with boundary conditions has√ no solution is $\{ \pm { \sqrt { 6 4 - 4 \pi ^ { 2 } } } \}$
:::
