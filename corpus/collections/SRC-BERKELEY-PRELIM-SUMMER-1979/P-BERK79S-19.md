---
schema: qual/card@1
id: P-BERK79S-19
kind: problem
title: Compactness of an integral transform of an $L^2$-bounded sequence
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
Let $f_n:[0,1]\to\mathbb R$ be continuous and suppose
\[
\int_0^1f_n(y)^2\,dy\le5
\]
for every $n$.
Define
\[
g_n(x)=\int_0^1\sqrt{x+y}\,f_n(y)\,dy,
\qquad 0\le x\le1.
\]

1. Find a constant $K\ge0$ such that $|g_n(x)|\le K$ for every $n$ and every $x\in[0,1]$.

2. Prove that some subsequence of $\{g_n\}$ converges uniformly on $[0,1]$.
:::
