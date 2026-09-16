---
schema: qual/card@1
id: PR-6WMSR
kind: proposition
title: Weak $M$-test
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Convergence of Functions
relations: []
review: draft
---

::: {.proposition}
Let $S$ be a set and let $f_n\colon S\to\CC$ for $n\geq1$.
Suppose that for each $x\in S$ there are constants $M_n(x)\geq0$ with $\abs{f_n(x)} \leq M_n(x)$ for all $n$ and $\sum_{n} M_n(x) < \infty$.
Then the series $f(x) \coloneqq \sum_{n} f_n(x)$ converges absolutely at every $x\in S$.
:::

::: {.remark}
The constants $M_n(x)$ may depend on $x$, and the conclusion is only pointwise convergence.
When one sequence $M_n$ serves every $x\in S$, the [[FS-5FKPD|Weierstrass $M$-test]] gives uniform convergence on $S$.
:::
