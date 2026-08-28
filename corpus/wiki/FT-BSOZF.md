---
schema: qual/card@1
id: FT-BSOZF
kind: theorem
title: Dirichlet's Test
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
If $\theset{a_n}, \theset{b_n}$ satisfy

- $a_n \searrow 0$

- For every $N$, there exists an $M_N$ such that $\abs{\sum_{n=1}^N b_n} \leq M_N$

Then $$ \sum_{n=1}^\infty a_n b_n < \infty .$$
:::
