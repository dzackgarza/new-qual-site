---
schema: qual/card@1
id: T-DS4VW
kind: theorem
title: Term-by-term differentiation of series of functions
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Differentiation
  - Uniform Convergence
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, and let $f_n\colon[a,b]\to\RR$ be differentiable for $n\geq1$.
Assume that

- there is a function $g\colon[a,b]\to\RR$ such that $\sum_{n}f_n'$ [[D-YZC3C|converges uniformly]] to $g$ on $[a,b]$, that is, $\sup_{x\in[a,b]}\abs{\sum_{n\leq N}f_n'(x)-g(x)}\to0$ as $N\to\infty$, and

- there exists $x_0\in[a,b]$ such that $\sum_n f_n(x_0)$ converges.

Then there exists a differentiable function $F\colon[a,b]\to\RR$ such that $\sum_n f_n$ converges uniformly to $F$ on $[a,b]$ and $F'=g$ on $[a,b]$.[^theorem_referfence_6.4.3_Abbott]
:::

[^theorem_referfence_6.4.3_Abbott]: See Abbott theorem 6.4.3, pp 168.
