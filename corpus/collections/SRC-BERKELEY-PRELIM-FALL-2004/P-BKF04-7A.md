---
schema: qual/card@1
id: P-BKF04-7A
kind: problem
title: UC Berkeley Fall 2004 prelim 7A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let D be the open unit disk in C, and $f \colon D \to D$ a holomorphic function. Suppose that $f ( - \frac { 1 } { 2 } ) = 0$ and $\begin{array} { r } { f ( 0 ) = \frac { 1 } { 2 } } \end{array}$ . Prove that there is only one possible value for $f ( { \frac { 1 } { 2 } } )$ , and find it.
:::

::: {.solution}
We first solve for a linear fractional transformation g of D mapping

$$
g ( - { \frac { 1 } { 2 } } ) = 0 , \qquad g ( 0 ) = { \frac { 1 } { 2 } }
$$

and find that the function

$$
g ( z ) = { \frac { z + { \frac { 1 } { 2 } } } { 1 + { \frac { z } { 2 } } } } = { \frac { 2 z + 1 } { 2 + z } }
$$

satisfies these conditions. Then the composition $h = f \circ g ^ { - 1 }$ satisfies

$$
h \colon D \to D , \qquad h ( 0 ) = 0 , \qquad h ( \frac 1 2 ) = \frac 1 2
$$

By Schwarz’s lemma we must have $| h ( z ) | \leq | z |$ in $D .$ . But equality holds for $\begin{array} { r } { z = \frac { 1 } { 2 } } \end{array}$ 1 , so $h ( z )$ must equal z. Hence $f = g$ , and

$$
f ( { \frac { 1 } { 2 } } ) = { \frac { 4 } { 5 } } .
$$
:::
