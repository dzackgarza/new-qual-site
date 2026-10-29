---
schema: qual/card@1
id: T-MN6WQ
kind: theorem
title: Interchanging sums and integrals for absolutely summable series
slogan: 'Absolute $L^1$ summability gives almost-everywhere convergence and lets summation commute with integration.'
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f_n\colon X\to\CC$ for $n\geq1$ be [[D-DHFN4|measurable]].

(a) The two quantities
$$
\sum_{n=1}^\infty \int_X \abs{f_n}\dmu \quad\text{and}\quad \int_X\sum_{n=1}^\infty \abs{f_n}\dmu
$$
are equal in $[0,\infty]$.
More generally, $\int_X\sum_n g_n\dmu=\sum_n\int_X g_n\dmu$ in $[0,\infty]$ for any $g_n\in$ [[D-BF5L2|$L^+$]] [@Fol13].

(b) If $\sum_{n}\norm{f_n}_1<\infty$, then $\sum_{n}f_n(x)$ converges absolutely for almost every $x$, its sum $F$, defined almost everywhere, lies in $L^1(X,\mu)$, and
$$
\norm{F-\sum_{n=1}^N f_n}_1 \convergesto{N\to\infty} 0,
\qquad
\int_X F\dmu = \sum_{n=1}^\infty \int_X f_n\dmu .
$$
:::

::: {.remark}
The two sides of (b) are the two iterated integrals of $(x,n)\mapsto f_n(x)$ on $X\times\NN$ with counting measure on $\NN$, so (b) is also an instance of [[T-DTXIA|Fubini's theorem]].
With counting measure on $\NN\times\NN$, the condition $\sum_{m,n} \int_X \abs{f_{m,n}}\dmu < \infty$ likewise justifies interchanging a double sum with the integral.
:::
