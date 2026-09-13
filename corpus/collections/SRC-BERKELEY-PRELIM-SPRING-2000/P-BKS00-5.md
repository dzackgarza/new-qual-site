---
schema: qual/card@1
id: P-BKS00-5
kind: problem
title: Convergence of the Babylonian iteration for $\sqrt a$
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

::: {.problem}
Let $a>0$ and $x_0>0$. Define recursively
\[
x_n=\frac12\left(x_{n-1}+\frac{a}{x_{n-1}}\right),
\qquad n\ge1.
\]
Prove that $(x_n)$ converges, and find its limit.
:::
