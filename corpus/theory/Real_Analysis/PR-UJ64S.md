---
schema: qual/card@1
id: PR-UJ64S
kind: proposition
title: The terms of a uniformly convergent series tend to zero uniformly
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Small Tails
  - Uniform Convergence
relations: []
review: draft
---

::: {.proposition}
Let $S$ be a set and let $f_n\colon S\to\CC$ for $n\geq1$.

(a) If $\sum_{n\geq1}f_n(x)$ converges for every $x\in S$, then $f_n\to0$ pointwise on $S$.

(b) If $\sum_{n\geq1}f_n$ [[D-YZC3C|converges uniformly]] on $S$, then $f_n\to0$ uniformly on $S$.
:::

::: {.example}
Pointwise convergence of the series does not give uniform convergence of the terms: on $S\coloneqq[0,1)$, $\sum_{n\geq0}x^n$ converges for every $x\in S$, but $\sup_{x\in S}\abs{x^n}=1$ for all $n$.
:::
