---
schema: qual/card@1
id: P-PRACT20-W6-03
kind: problem
title: "Week 6: Miscellaneous Topics, problem 3"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Which of the following does not define a metric on R?

$$
\begin{array} { r l } & { \mathrm { ( A ) } \ \delta ( x , y ) = \left\{ \begin{array} { l l } { 0 , x = y , } \\ { 2 , x \neq y . } \end{array} \right. \quad \mathrm { ( B ) } \ \rho ( x , y ) = \operatorname* { m i n } \{ | x - y | , 1 \} \quad \mathrm { ( C ) } \ \sigma ( x , y ) = \frac { | x - y | } { 3 } } \\ & { \mathrm { ( D ) } \ \tau ( x , y ) = \frac { | x - y | } { | x - y | + 1 } \quad \mathrm { ( E ) } \ \omega ( x , y ) = ( x - y ) ^ { 2 } } \end{array}
$$
:::

::: {.solution}
(A) is a scaled version of the discrete metric. (B) and (D) are bounded versions of the standard metric (i.e., the generate the standard topology even though they give bounded distance between points). (C) is a scaled version of the standard metric. (E) is not a metric because the triangle inequality is not satisfied. Indeed, let $\scriptstyle x = 0 , y = { \frac { 1 } { 2 } } , z = 1$ . Then

$$
\begin{array} { r } { 1 = \omega ( x , z ) \not \subseteq \omega ( x , y ) + \omega ( y , z ) = \left( { \frac { 1 } { 2 } } \right) ^ { 2 } + \left( { \frac { 1 } { 2 } } \right) ^ { 2 } = { \frac { 1 } { 2 } } } \end{array}
$$
:::
