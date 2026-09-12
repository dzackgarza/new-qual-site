---
schema: qual/card@1
id: P-BKS06-3B
kind: problem
title: UC Berkeley Spring 2006 prelim 3B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate the integral

$$
\int _ { - \infty } ^ { \infty } { \frac { e ^ { i t x } } { e ^ { x } + e ^ { - x } } } d x
$$

for $t > 0$
:::

::: {.solution}
The integral converges absolutely, since the numerator has absolute value 1, while the denominator decays exponentially in both directions.

Use a rectangular contour C bounded by $x = R , x = - R , y = 0$ and $y = \pi$ . As $R \to \infty$ the integrals along the vertical parts of the contour tend to 0, since

$$
\left| \int _ { 0 } ^ { \pi } { \frac { e ^ { i t ( R + i y ) } } { e ^ { R + i y } + e ^ { - R - i y } } } d y \right| \leq \int _ { 0 } ^ { \pi } { \frac { 1 } { e ^ { R } - e ^ { - R } } } d y = { \frac { \pi } { e ^ { R } - e ^ { - R } } } .
$$

The integral along the horizontal path $y = \pi$ equals

$$
\int _ { R } ^ { - R } \frac { e ^ { i t ( x + \pi i ) } } { e ^ { ( x + \pi i ) } + e ^ { - ( x + \pi i ) } } d x = \int _ { R } ^ { - R } \frac { e ^ { - \pi t } e ^ { i t x } } { - e ^ { x } - e ^ { - x } } d x = e ^ { - \pi t } \int _ { - R } ^ { R } \frac { e ^ { i t x } } { e ^ { x } + e ^ { - x } } d x .
$$

Let I denote the integral we have to find. Then

$$
\operatorname* { l i m } _ { R  \infty } \oint _ { C } { \frac { e ^ { i t z } } { e ^ { z } + e ^ { - z } } } d z = ( 1 + e ^ { - \pi t } ) I .
$$

On the other hand,

$$
\oint _ { C } { \frac { e ^ { i t z } } { e ^ { z } + e ^ { - z } } } d z = 2 \pi i \operatorname { R e s } _ { \frac { \pi i } { 2 } } ,
$$

since the only singular point inside the contour is $\textstyle { \frac { \pi i } { 2 } }$ . Now

$$
\mathrm { R e s } _ { \frac { \pi i } { 2 } } = \frac { e ^ { - \frac { \pi t } { 2 } } } { 2 i } ,
$$

so

$$
\oint _ { C } { \frac { e ^ { i t z } } { e ^ { z } + e ^ { - z } } } d z = \pi e ^ { - { \frac { \pi t } { 2 } } } ,
$$

$$
I = \pi \frac { e ^ { - \frac { \pi t } { 2 } } } { 1 + e ^ { - \pi t } } = \frac { \pi } { e ^ { \frac { \pi t } { 2 } } + e ^ { - \frac { \pi t } { 2 } } } .
$$
:::
