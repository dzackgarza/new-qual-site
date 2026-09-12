---
schema: qual/card@1
id: P-BKF04-5A
kind: problem
title: UC Berkeley Fall 2004 prelim 5A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $( a _ { m } ) _ { m \geq 1 }$ be a sequence of real numbers satisfying $a _ { n + m } \leq a _ { n } + a _ { m }$ . Prove that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n } } { n } } = \operatorname* { i n f } _ { n } { \frac { a _ { n } } { n } }
$$

as an element of $[ - \infty , \infty )$
:::

::: {.solution}
If $n = \ell m + r$ for integers $m , \ell \geq 1$ and $r \in [ 0 , m )$ , then $a _ { n } = a _ { \ell m + r } \leq a _ { \ell m } + a _ { r } \leq$ $\ell a _ { m } + a _ { r }$ , and dividing by n yields

$$
\frac { a _ { n } } { n } \leq \frac { \ell m } { n } \frac { a _ { m } } { m } + \frac { a _ { r } } { n } .
$$

After sending $n \to \infty$ (for fixed m, so \` and r vary with n), we obtain

$$
\operatorname* { l i m } \operatorname* { s u p } { \frac { a _ { n } } { n } } \leq { \frac { a _ { m } } { m } } .
$$

This holds for each m, so

$$
\operatorname* { l i m } \operatorname* { s u p } { \frac { a _ { n } } { n } } \leq \operatorname* { i n f } { \frac { a _ { m } } { m } } .
$$

On the other hand,

$$
\operatorname* { l i m } \operatorname* { i n f } { \frac { a _ { n } } { n } } \geq \operatorname* { i n f } { \frac { a _ { m } } { m } }
$$

holds by definition. Thus

$$
\operatorname* { l i m } { \frac { a _ { n } } { n } } = \operatorname* { i n f } { \frac { a _ { m } } { m } } .
$$
:::
