---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW4
kind: problem
title: Select a convergent subseries from a sequence tending to zero (warm-up)
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Sequences of Numbers
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
([KRD10, #3.1.D]) Let $\{a_n\}$ be a sequence such that $\lim_{n\to\infty}|a_n|=0$.
Prove that there is a subsequence $\{a_{n_k}\}$ of $\{a_n\}$ such that $\sum_{k=1}^{\infty}a_{n_k}$ converges.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Extract a rapidly decaying subsequence.
Proof: since $|a_n| \to 0$, for each $k \ge 1$ we may choose an index $n_k$ with $n_1 < n_2 < \cdots$ and $|a_{n_k}| \le 2^{-k}$ (indeed $|a_n| < 2^{-k}$ for all sufficiently large $n$, so pick any $n_k$ larger than $n_{k-1}$ with this property).
<1>2. The subseries converges absolutely.
Proof: $\sum_{k=1}^\infty |a_{n_k}| \le \sum_{k=1}^\infty 2^{-k} = 1 < \infty$, so $\sum_k a_{n_k}$ converges absolutely, hence converges.
<1>3. Q.E.D.
:::
