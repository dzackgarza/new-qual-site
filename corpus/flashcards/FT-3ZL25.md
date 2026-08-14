---
schema: qual/card@1
id: FT-3ZL25
kind: theorem
title: 'Dirichlet''s Test'
classification:
  areas:
  - complex-analysis
  topics:
  - convergence-tests
  - series-of-numbers
relations: []
review: draft
---

::: {.theorem title="Dirichlet's Test"}
If $\theset{a_n}, \theset{b_n}$ satisfy

- $a_{n+1} \leq a_n$ and $a_n \to 0$ (i.e. $a_n \searrow 0$),

- The partial sums are uniformly bounded: there exists an $M$ such that $\abs{\sum_{n=1}^N b_n} \leq M$ for all $N$,

then $\sum_{n=1}^\infty a_n b_n < \infty$.
:::
