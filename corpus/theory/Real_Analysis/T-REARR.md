---
schema: qual/card@1
id: T-REARR
kind: theorem
title: Riemann's rearrangement theorem
slogan: 'a conditionally convergent series rearranges to any prescribed pair of limit points'
classification:
  areas:
  - real-analysis
  topics:
  - Series
  - Conditional Convergence
relations: []
review: draft
---

::: {.theorem}
Let $\sum_n a_n$ be a series of real numbers that converges but does not converge absolutely, and let $-\infty\leq\alpha\leq\beta\leq\infty$.
Then there is a rearrangement $\sum_n a'_n$ of $\sum_n a_n$, with partial sums $s'_n = a'_1+\cdots+a'_n$, such that
$$
\liminf_{n\to\infty} s'_n = \alpha, \qquad \limsup_{n\to\infty} s'_n = \beta .
$$
Taking $\alpha=\beta=x$ gives a rearrangement converging to $x$; the two limits are the extremes of the set of values of the convergent rearrangements.
:::
