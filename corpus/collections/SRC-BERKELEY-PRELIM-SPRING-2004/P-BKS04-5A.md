---
schema: qual/card@1
id: P-BKS04-5A
kind: problem
title: UC Berkeley Spring 2004 prelim 5A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose $f \colon  { \mathbb { R } } \to  { \mathbb { C } }$ satisfies $f ^ { \prime } ( t ) + 2 i t f ( t ) = e ^ { 2 i t }$ and $f ( 0 ) = 0$ . Compute

$$
\operatorname* { l i m } _ { t \to + \infty } e ^ { i t ^ { 2 } } ( f ( t ) - f ( - t ) ) .
$$

You may assume $\textstyle \int _ { 0 } ^ { \infty } e ^ { - t ^ { 2 } } d t = { \sqrt { \pi } } / 2$
:::

::: {.solution}
Multiply the ODE by the integrating factor $e ^ { i t ^ { 2 } }$ , and integrate to get

$$
e ^ { i t ^ { 2 } } f ( t ) = \int _ { 0 } ^ { t } e ^ { i x ^ { 2 } + 2 i x } d x
$$

(The hypothesis $f ( 0 ) = 0$ implies that there is no constant of integration.) Substituting −t for t and subtracting, we get

$$
\begin{array} { l } { { \displaystyle e ^ { i t ^ { 2 } } ( f ( t ) - f ( - t ) ) = \int _ { - t } ^ { t } e ^ { i x ^ { 2 } + 2 i x } d x } \ ~ } \\ { { \displaystyle ~ = e ^ { - i } \int _ { - t } ^ { t } e ^ { i ( x + 1 ) ^ { 2 } } d x } \ ~ } \\ { { \displaystyle ~ = e ^ { - i } \int _ { - t + 1 } ^ { t + 1 } e ^ { i z ^ { 2 } } d z } . } \end{array}
$$

Since $e ^ { i z ^ { 2 } }$ is an even function, the limit as $t \to + \infty$ equals $2 e ^ { - i } I$ , where $\begin{array} { r } { I : = \operatorname* { l i m } _ { R \to + \infty } \int _ { 0 } ^ { R } e ^ { i z ^ { 2 } } d z } \end{array}$ (assuming for now that the latter limit exists). Apply Cauchy’s Theorem to the triangular contour from 0 to R to $R + R i$ and back to 0. The vertical part contributes

$$
\int _ { R } ^ { R + R i } e ^ { i z ^ { 2 } } d z = \int _ { 2 } ^ { R } e ^ { i ( R + t i ) ^ { 2 } } i d t ,
$$

whose absolute value is bounded by

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { R } { \lvert e ^ { i ( R + t i ) ^ { 2 } } \rvert d t } = \int _ { 0 } ^ { R } e ^ { - 2 R t } d t } \\ { \displaystyle \qquad = \frac { 1 } { 2 R } \int _ { 0 } ^ { 2 R ^ { 2 } } e ^ { - u } d u , } \end{array}
$$

which goes to 0 as $R \to \infty$ . Thus

$$
{ \begin{array} { r l r l } & { I = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { 0 } ^ { R + R i } e ^ { i z ^ { 2 } } d z \qquad } & & { { \mathrm { ( i f ~ t h e ~ l i m i t ~ e x i s t s ) } } } \\ & { = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { 0 } ^ { R } e ^ { i ( e ^ { i \pi / 4 } t ) ^ { 2 } } e ^ { i \pi / 4 } d t \qquad } & & { { \mathrm { ( i f ~ t h e ~ l i m i t ~ e x i s t s ) } } } \\ & { = e ^ { i \pi / 4 } \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { 0 } ^ { R } e ^ { - t ^ { 2 } } d t \qquad } & & { { \mathrm { ( i f ~ t h e ~ l i m i t ~ e x i s t s ) } } } \\ & { = e ^ { i \pi / 4 } { \frac { \sqrt { \pi } } { 2 } } . } \end{array} }
$$

Thus we now know that all the limits exist, and the answer is 2e $^ { - i } I = e ^ { - i + i \pi / 4 } \sqrt { \pi } .$
:::
