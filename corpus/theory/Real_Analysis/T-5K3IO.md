---
schema: qual/card@1
id: T-5K3IO
kind: theorem
title: Monotone convergence theorem
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, and let $f_n$ for $n\geq1$ and $f$ be functions in [[D-BF5L2|$L^+(X,\mcm)$]] such that, for almost every $x\in X$, $f_n(x)\leq f_{n+1}(x)$ for all $n$ and $f_n(x)\to f(x)$.
Then
$$
\lim_{n\to\infty} \int_X f_n\dmu = \int_X f\dmu .
$$
:::
