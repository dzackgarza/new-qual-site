---
schema: qual/card@1
id: P-BERK90S-17
kind: problem
title: First-order error bound for left Riemann sums
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
Let $f$ be differentiable on $[0,1]$ and suppose
\[
M=\sup_{0<x<1}|f'(x)|<\infty.
\]
For every positive integer $n$, prove that
\[
\left|
\frac1n\sum_{j=0}^{n-1}f(j/n)
-\int_0^1f(x)\,dx
\right|
\le\frac{M}{2n}.
\]
:::
