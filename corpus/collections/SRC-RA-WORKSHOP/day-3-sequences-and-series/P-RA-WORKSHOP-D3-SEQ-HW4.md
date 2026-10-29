---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW4
kind: problem
title: Select a convergent subseries from a sequence tending to zero
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
([KRD10, #3.1.D]) Let $\{a_n\}$ be a sequence such that $\lim_{n\to\infty}|a_n|=0$.
Prove that there is a subsequence $\{a_{n_k}\}$ of $\{a_n\}$ such that $\sum_{k=1}^{\infty}a_{n_k}$ converges.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is a strictly increasing sequence of indices $(n_k)_{k\geq1}$ satisfying $|a_{n_k}|<2^{-k}$ for every $k$.

::: pf-proof

For $k=1$, use $|a_n|\to0$ to choose $n_1$ with $|a_{n_1}|<1/2$. Once $n_{k-1}$ has been chosen, convergence gives an integer $N_k$ such that $|a_n|<2^{-k}$ for every $n\geq N_k$. Choose $n_k>\max(n_{k-1},N_k)$. This inductively constructs the required subsequence.

:::

:::

::: {.pf-step #s2}

The selected subseries $\sum_{k=1}^{\infty}a_{n_k}$ converges absolutely.

::: pf-proof

Step [](#s1){.pf-ref} and comparison with the geometric series give
\[
\sum_{k=1}^{\infty}|a_{n_k}|
\leq\sum_{k=1}^{\infty}2^{-k}=1<\infty.
\]
Thus the subseries is absolutely convergent, hence convergent.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} constructs a subsequence, and step [](#s2){.pf-ref} establishes convergence of its series.

:::

:::

:::
