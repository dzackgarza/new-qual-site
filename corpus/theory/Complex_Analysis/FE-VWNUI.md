---
schema: qual/card@1
id: FE-VWNUI
kind: example
title: A power series of radius $1$ converging at every point of $S^1$
prompts:
- Give an analytic function of convergence radius 1 that converges at every point of $S^1$.
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Series of Functions
  - Counterexamples
relations: []
review: draft
---

::: {.example}
The power series $\sum_{n=1}^\infty \frac{z^n}{n^2}$ has radius of convergence $1$ and converges at every $z$ with $\abs{z}=1$.
Its radius is $1$ because $\limsup_n(1/n^2)^{1/n}=1$.
For $\abs{z}=1$, $\abs{z^n/n^2}=1/n^2$ and $\sum_n 1/n^2<\infty$, so the series converges absolutely.
:::
