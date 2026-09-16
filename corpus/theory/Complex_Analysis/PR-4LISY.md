---
schema: qual/card@1
id: PR-4LISY
kind: proposition
title: Uniform convergence of a series through its tails
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

::: {.proof}
Let $S(x)\coloneqq\sum_{k\ge1}f_k(x)$ and $S_n(x)\coloneqq\sum_{k=1}^nf_k(x)$.
Then $\sum_{k\ge n}f_k(x)=S(x)-S_{n-1}(x)$, so the displayed condition says exactly that $\sup_{x\in X}\abs{S(x)-S_{n-1}(x)}\to0$, which is uniform convergence of the partial sums $S_n$ to $S$.
:::
