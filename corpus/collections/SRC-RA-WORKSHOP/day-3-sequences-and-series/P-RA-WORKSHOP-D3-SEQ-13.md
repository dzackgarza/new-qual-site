---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-13
kind: problem
title: The ratio test follows from the root test
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Assume that Theorem 2.4 (the root test) is true and prove the ratio test (Theorem 2.5).
:::

::: {.solution}
Let $(a_n)$ be a sequence of nonzero real or complex numbers and put $c_n=|a_n|>0$.

::: pf

::: {.pf-step #s1}

If $\limsup_{n\to\infty}c_{n+1}/c_n<1$, then $\sum_n a_n$ converges absolutely.

::: pf-proof

Choose $q$ strictly between $\limsup c_{n+1}/c_n$ and $1$. For some $N$, $c_{n+1}\leq q c_n$ whenever $n\geq N$, and hence $c_n\leq c_Nq^{n-N}$ for every $n\geq N$. Taking $n$-th roots yields
\[
\limsup_{n\to\infty}c_n^{1/n}\leq q<1.
\]
The convergent case of the root test now proves absolute convergence.

:::

:::

::: {.pf-step #s2}

If $\liminf_{n\to\infty}c_{n+1}/c_n>1$, then $\sum_n a_n$ diverges.

::: pf-proof

Choose $q$ strictly between $1$ and $\liminf c_{n+1}/c_n$. For some $N$, $c_{n+1}\geq q c_n$ whenever $n\geq N$, so $c_n\geq c_Nq^{n-N}$. Consequently
\[
\liminf_{n\to\infty}c_n^{1/n}\geq q>1.
\]
The divergent case of the root test applies, since $\limsup c_n^{1/n}>1$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} establish the convergence and divergence assertions of the ratio test; when the ratio limit exists, the conclusions apply according as it is less than or greater than $1$.

:::

:::

:::
