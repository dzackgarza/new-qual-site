---
schema: qual/card@1
id: PR-WUZSG
kind: proposition
title: Sup-norm test for uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Norms
relations: []
review: draft
---

::: {.proposition}
Let $S$ be a set and let $f_n,f\colon S\to\CC$ for $n\geq1$.
Then $f_n\to f$ [[D-YZC3C|uniformly]] on $S$ if and only if there are real numbers $M_n$ with
$$
\sup_{x\in S}\abs{f_n(x) - f(x)} \leq M_n \text{ for all } n \quad\text{and}\quad M_n\convergesto{n\to\infty}0 .
$$
:::
