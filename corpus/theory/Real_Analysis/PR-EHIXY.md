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

::: {.proof}
Put $G\coloneqq\sum_{k=1}^\infty\abs{f_k}\colon X\to[0,\infty]$.
By the monotone convergence theorem, $\int_X G\dmu=\sum_k\norm{f_k}_1<\infty$, so $G<\infty$ almost everywhere, and at each such point $\sum_k f_k(x)$ converges absolutely.
Define $F$ as this sum where $G<\infty$ and $0$ elsewhere.
Then $\abs{F}\leq G$ and $\abs{F-\sum_{k=1}^N f_k}\leq \sum_{k>N}\abs{f_k}$ almost everywhere, so $F\in L^1(\mu)$ and, by the monotone convergence theorem applied to $\sum_{k>N}\abs{f_k}$,
$$
\norm{F-\sum_{k=1}^N f_k}_1\leq\sum_{k>N}\norm{f_k}_1\convergesto{N\to\infty}0 .
$$
The equality of integrals follows since $\abs{\int_X F\dmu-\sum_{k\leq N}\int_X f_k\dmu}\leq\norm{F-\sum_{k\leq N}f_k}_1$.
:::
