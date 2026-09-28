---
schema: qual/card@1
id: FD-WN55Z
kind: definition
title: Completeness of a normed space via absolutely convergent series
prompts:
- What two conditions each characterise completeness?
classification:
  areas:
  - real-analysis
  topics:
  - Completeness
  - Series of Numbers
relations: []
review: draft
---

::: {.definition}
Let $(V,\norm{\cdot})$ be a normed vector space.
The following are equivalent:

- $V$ is [[D-G5N6I|complete]]: every Cauchy sequence in $V$ converges.

- Every absolutely convergent series in $V$ converges: if $x_n\in V$ and $\sum_{n=1}^\infty\norm{x_n}<\infty$, then $\sum_{n=1}^\infty x_n$ converges in $V$.
:::

::: {.proof}
Assume $V$ is complete and $\sum_n\norm{x_n}<\infty$.
For $M>N$ the partial sums $s_N\coloneqq\sum_{n=1}^N x_n$ satisfy $\norm{s_M-s_N}\leq\sum_{n=N+1}^M\norm{x_n}$, so $(s_N)$ is Cauchy and converges.

Conversely, assume every absolutely convergent series converges, and let $(y_m)$ be a Cauchy sequence.
Choose $m_1<m_2<\cdots$ with $\norm{y_p-y_q}<2^{-k}$ for all $p,q\geq m_k$.
The series $y_{m_1}+\sum_{k\geq 1}(y_{m_{k+1}}-y_{m_k})$ is absolutely convergent, so it converges; its partial sums are $y_{m_{k}}$, so the subsequence $(y_{m_k})$ converges to some $y\in V$.
A Cauchy sequence with a convergent subsequence converges to the same limit, so $y_m\to y$.
:::
