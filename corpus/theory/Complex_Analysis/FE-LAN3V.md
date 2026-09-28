---
schema: qual/card@1
id: FE-LAN3V
kind: example
title: A power series of radius $1$ converging on $S^1$ except at $z=1$
prompts:
- Give an analytic function of convergence radius 1 that converges on $S^1$ except at $z=1$.
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
The power series $\sum_{n=1}^\infty \frac{z^n}{n}$ has radius of convergence $1$, diverges at $z=1$, and converges at every other point of $S^1$.
Its radius is $1$ because $\limsup_n(1/n)^{1/n}=1$.
At $z=1$ it is the harmonic series, which diverges.
For $\abs{z}=1$ with $z\neq1$, the partial sums satisfy $\abs{\sum_{n=1}^N z^n}=\abs{\frac{z(1-z^N)}{1-z}}\le\frac{2}{\abs{1-z}}$, and $1/n$ decreases to $0$, so the series converges by Dirichlet's test.
:::
