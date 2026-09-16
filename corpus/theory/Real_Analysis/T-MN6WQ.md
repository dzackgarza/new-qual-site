---
schema: qual/card@1
id: T-MN6WQ
kind: theorem
title: Interchanging sums and integrals for absolutely summable series
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Series of Functions
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f_n\colon X\to\CC$ be [[D-R5DL3|integrable]] for $n\geq1$.
The two quantities
$$
\sum_{n=1}^\infty \int_X \abs{f_n}\dmu \quad\text{and}\quad \int_X\sum_{n=1}^\infty \abs{f_n}\dmu
$$
are equal, and if they are finite, then $\sum_{n}f_n(x)$ converges absolutely for almost every $x$, its sum is integrable, and
$$
\int_X\sum_{n=1}^\infty f_n\dmu = \sum_{n=1}^\infty \int_X f_n\dmu .
$$
:::
