---
schema: qual/card@1
id: PR-4LISY
kind: proposition
title: Uniform convergence of a series through its tails
slogan: 'A pointwise-convergent series is uniformly convergent exactly when its tails vanish uniformly.'
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: {.proposition}
Let $X$ be a set and let $f_n\colon X\to\CC$ for $n\ge1$ be functions such that $\sum_{n=1}^\infty f_n(x)$ converges for every $x\in X$.
Then $\sum_{n=1}^\infty f_n$ converges uniformly on $X$ if and only if
$$
\lim_{n\to \infty} \sup_{x\in X}\abs{ \sum_{k\geq n} f_k(x) } = 0.
$$
:::
