---
schema: qual/card@1
id: P-PRACT20-W6-20
kind: problem
title: Standard deviation of the density $\frac34(1-x^2)$ on $[-1,1]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let X be a random variable with density function $\textstyle f ( x ) = { \frac { 3 } { 4 } } ( 1 - x ^ { 2 } )$ , for $x \in [ - 1 , 1 ]$ (and $f ( x ) = 0$ elsewhere).
What is the standard deviation of $X ?$
:::

::: {.solution}
Recall, the variance of X if given by

$$
\operatorname { V a r } ( X ) = E ( X ^ { 2 } ) - E ( X ) ^ { 2 }
$$

and since X has distribution function $f ,$ we see that

$$
E ( g ( X ) ) = \int _ { \mathbb { R } } g ( x ) f ( x ) d x .
$$

Thus

$$
E ( X ) = \int _ { \mathbb { R } } x f ( x ) d x = { \frac { 3 } { 4 } } \int _ { - 1 } ^ { 1 } ( x - x ^ { 3 } ) d x = 0 { \mathrm { ~ s i n c e ~ t h e ~ i n t e g r a n d ~ i s ~ o d d } } .
$$

Next,

$$
E ( X ^ { 2 } ) = \int _ { \mathbb { R } } x ^ { 2 } f ( x ) d x = { \frac { 3 } { 4 } } \int _ { - 1 } ^ { 1 } ( x ^ { 2 } - x ^ { 4 } ) = { \frac { 3 } { 4 } } \left( { \frac { 2 } { 3 } } - { \frac { 2 } { 5 } } \right) = { \frac { 3 } { 4 } } \cdot { \frac { 4 } { 1 5 } } = { \frac { 1 } { 5 } } .
$$

The standard deviation is the square root of the variance so $\begin{array} { r } { \mathrm { S t D e v } ( X ) = \frac { 1 } { \sqrt { 5 } } } \end{array}$
:::
