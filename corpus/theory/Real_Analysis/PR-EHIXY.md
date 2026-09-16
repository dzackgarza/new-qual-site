---
schema: qual/card@1
id: PR-EHIXY
kind: proposition
title: Absolutely summable series in $L^1$ converge almost everywhere and in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - L¹
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] and let $f_k\in L^1(\mu)$ for $k\geq1$ satisfy $\sum_{k=1}^\infty \norm{f_k}_1 < \infty$.
Then $\sum_{k=1}^\infty f_k(x)$ converges absolutely for $\mu$-almost every $x\in X$, its sum $F$ lies in $L^1(\mu)$, and
$$
\norm{F-\sum_{k=1}^N f_k}_1 \convergesto{N\to\infty} 0,
\qquad
\int_X F\dmu = \sum_{k=1}^\infty \int_X f_k\dmu .
$$
:::
