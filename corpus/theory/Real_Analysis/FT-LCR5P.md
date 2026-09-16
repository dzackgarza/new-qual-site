---
schema: qual/card@1
id: FT-LCR5P
kind: theorem
title: Dominated convergence theorem
prompts:
- State the dominated convergence theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, and let $f_n\colon X\to\CC$ for $n\geq1$ and $f\colon X\to\CC$ be [[D-DHFN4|measurable]].
Suppose $f_n\to f$ almost everywhere and there exists $g \in L^1(X,\mu)$ with $\abs{f_n} \leq g$ almost everywhere for every $n$.
Then $f\in L^1(X,\mu)$ and
$$
\lim_{n\to\infty} \int_X f_n\dmu = \int_X f\dmu .
$$
:::
