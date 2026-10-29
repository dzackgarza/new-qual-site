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
Assume the root test: for a series $\sum a_n$ with $\alpha=\limsup_{n\to\infty}\sqrt[n]{\abs{a_n}}$, the series converges if $\alpha<1$ and diverges if $\alpha>1$. Prove the ratio test: for a series $\sum a_n$ of nonzero terms,

(a) $\sum a_n$ converges if $\limsup_{n\to\infty}\abs{a_{n+1}/a_n}<1$;

(b) $\sum a_n$ diverges if $\abs{a_{n+1}/a_n}\geq1$ for all $n\geq n_0$.
:::

::: {.solution}
Let $(a_n)$ be a sequence of nonzero real or complex numbers and put $c_n=\abs{a_n}>0$.

::: pf

::: pf-step

(a) If $\limsup_{n\to\infty}c_{n+1}/c_n<1$, then $\sum_n a_n$ converges absolutely.

::: pf-proof

Choose $q$ strictly between $\limsup c_{n+1}/c_n$ and $1$. For some $N$, $c_{n+1}\leq q c_n$ whenever $n\geq N$, and hence $c_n\leq c_Nq^{n-N}$ for every $n\geq N$. Taking $n$-th roots, and using $(c_Nq^{-N})^{1/n}\to1$, yields
$$
\limsup_{n\to\infty}c_n^{1/n}\leq q<1.
$$
The convergent case of the root test now proves absolute convergence.

:::

:::

::: pf-step

(b) If $c_{n+1}/c_n\geq1$ for all $n\geq n_0$, then $\sum_n a_n$ diverges.

::: pf-proof

By induction $c_n\geq c_{n_0}>0$ for all $n\geq n_0$, so $a_n\not\to0$ and the series diverges by the $n$th-term test. The root test does not decide this case: for $a_n=1$ the ratios equal $1$ and $\alpha=1$.

:::

:::

:::

:::
