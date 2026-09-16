---
schema: qual/card@1
id: PR-O2XFF
kind: proposition
title: Weierstrass $M$-test
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: {.proposition}
Let $A$ be a set and let $f_n\colon A\to\CC$ for $n\geq1$.
If there are real numbers $M_n$ with $\sup_{x\in A} \abs{f_n(x)} \leq M_n$ for each $n$ and $\sum_{n\geq1} M_n < \infty$, then $\sum_{n=1}^\infty f_n(x)$ converges absolutely for each $x\in A$, and the series [[D-YZC3C|converges uniformly]] on $A$.
:::

::: {.remark}
Conversely, if $\sum_n f_n$ converges uniformly on $A$, then $\sup_{x\in A}\abs{f_n(x)}\to0$; this necessary condition does not imply $\sum_n\sup_{x\in A}\abs{f_n(x)}<\infty$, as the constant functions $f_n\coloneqq(-1)^n/n$ show.
:::
