---
schema: qual/card@1
id: FT-3ZL25
kind: theorem
title: Dirichlet's test
prompts:
- State Dirichlet's test for convergence of a series.
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Series of Numbers
relations: []
review: draft
---

::: {.theorem}
Let $(a_n)_{n\ge1}$ be a sequence of real numbers and $(b_n)_{n\ge1}$ a sequence of complex numbers such that

- $a_{n+1} \leq a_n$ for all $n$ and $a_n \to 0$, and

- there exists $M\ge0$ such that $\abs{\sum_{n=1}^N b_n} \leq M$ for all $N\ge1$.

Then the series $\sum_{n=1}^\infty a_n b_n$ converges.
:::
