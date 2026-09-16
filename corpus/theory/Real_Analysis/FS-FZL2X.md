---
schema: qual/card@1
id: FS-FZL2X
kind: strategy
title: Showing uniform convergence of a sequence of functions
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
---

::: {.strategy}
Let $S$ be a set, and let $f_n\colon S\to\CC$ for $n\geq1$ and $f\colon S\to\CC$ be functions.
Find constants $M_n$, independent of $x$, such that
$$
\abs{f_n(x) - f(x)} \leq M_n \quad\text{for all } x\in S \text{ and } n\geq1, \qquad M_n \to 0.
$$
Then $(f_n)$ [[D-YZC3C|converges uniformly]] to $f$ on $S$.
:::
