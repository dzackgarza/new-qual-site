---
schema: qual/card@1
id: FT-BSOZF
kind: theorem
title: Dirichlet's test
prompts:
- What hypotheses does Dirichlet's test put on $\theset{a_n}$ and $\theset{b_n}$?
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Series of Numbers
relations:
- kind: variant-of
  target: FT-3ZL25
review: draft
---

::: {.theorem}
Let $(a_n)_{n\ge1}$ be a sequence of real numbers and $(b_n)_{n\ge1}$ a sequence of complex numbers such that

- $(a_n)$ is nonincreasing and $a_n\to0$, and

- there exists $M\ge0$ such that $\abs{\sum_{n=1}^N b_n} \leq M$ for every $N\ge1$.

Then the series $\sum_{n=1}^\infty a_n b_n$ converges.
:::
