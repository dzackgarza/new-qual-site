---
schema: qual/card@1
id: P-BKF04-9A
kind: problem
title: UC Berkeley Fall 2004 prelim 9A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f \colon [ 0 , 1 ] \to \mathbb { R }$ be a continuous function. Show that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x = 0 .
$$
:::

::: {.solution}
We can approximate f uniformly by smooth functions in [0, 1], so it suffices to prove the statement when f is smooth.

Choose M such that $| f ( x ) | < M$ for all $x \in [ 0 , 1 ]$ . Let $\epsilon > 0$ . Then

$$
\left| \int _ { 0 } ^ { \epsilon } f ( x ) e ^ { i n x ^ { 3 } } d x \right| \le \epsilon M
$$

On the remaining interval we integrate by parts:

$$
\begin{array} { r c l } { { \displaystyle \int _ { \epsilon } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x } } & { { = } } & { { \displaystyle \int _ { \epsilon } ^ { 1 } \frac { f ( x ) } { x ^ { 2 } } x ^ { 2 } e ^ { i n x ^ { 3 } } d x } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { i n } \left( f ( 1 ) e ^ { i n } - \frac { f ( \epsilon ) } { \epsilon ^ { 2 } } e ^ { i n \epsilon ^ { 3 } } - \int _ { \epsilon } ^ { 1 } \frac { d } { d x } \left( \frac { f ( x ) } { x ^ { 2 } } \right) e ^ { i n x ^ { 3 } } d x \right) } } \end{array}
$$

Letting n tend to infinity, we obtain

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { \epsilon } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x = 0
$$

Adding to this the bound on $[ 0 , \epsilon ]$ , we get

$$
\operatorname* { l i m } _ { n \to \infty } \left| \int _ { 0 } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x \right| \le \epsilon M
$$

The conclusion follows if we let  tend to 0.
:::
