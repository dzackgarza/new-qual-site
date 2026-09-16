---
schema: qual/card@1
id: T-IJQQG
kind: theorem
title: Dominated convergence theorem
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, and let $f_n\colon X\to\CC$ for $n\geq1$ and $f\colon X\to\CC$ be [[D-DHFN4|measurable]] with $f_n\to f$ almost everywhere.
Suppose there is an [[D-R5DL3|integrable]] $g\colon X\to[0,\infty)$ with $\abs{f_n} \leq g$ almost everywhere for every $n$.
Then $f$ is integrable and
$$
\lim_{n\to\infty}\int_X \abs{f_n - f}\dmu = 0 ;
$$
consequently
$$
\lim_{n\to\infty} \int_X f_n\dmu = \int_X f\dmu .
$$
:::

::: {.remark}
The functions $f_n$ may be complex-valued and of arbitrary sign; the only sign condition is $g\geq0$ on the dominating function.
:::
