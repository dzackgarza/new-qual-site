---
schema: qual/card@1
id: P-BERK89S-01
kind: problem
title: Unbounded weights preserving convergence of a positive series
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Chose successive tail cutoffs with summable weighted tail bounds and used
    the block number as the weight on each interval of indices.
---

::: {.problem}
Let $(a_n)$ be positive and suppose
\[
\sum_{n=1}^\infty a_n<\infty.
\]
Prove that there are positive numbers $c_n$ such that
\[
c_n\to\infty
\]
and
\[
\sum_{n=1}^\infty c_na_n<\infty.
\]
:::

::: {.solution}
For $N\geq1$, write $T_N\coloneqq\sum_{n=N}^\infty a_n$.

::: pf

::: {.pf-step #block-cutoffs}
There is a strictly increasing sequence $(N_k)_{k\geq1}$ such that
$$
T_{N_k}<\frac{2^{-k}}{k}
$$
for every $k\geq1$.

::: pf-proof
Convergence of $\sum_{n=1}^\infty a_n$ gives $T_N\to0$. Choose $N_1$ with
$T_{N_1}<2^{-1}$. Inductively, after choosing $N_k$, choose $N_{k+1}>N_k$
so large that $T_{N_{k+1}}<2^{-(k+1)}/(k+1)$.
:::

:::

::: {.pf-step #weights-defined}
Define $c_n=1$ for $1\leq n<N_1$ and
$$
c_n=k\qquad(N_k\leq n<N_{k+1}).
$$
Then every $c_n$ is positive and $c_n\to\infty$.

::: pf-proof
The intervals $[N_k,N_{k+1})$ partition the integers $n\geq N_1$. Given
$M>0$, choose an integer $K>M$. For $n\geq N_K$, the index $n$ belongs to
a block numbered $k\geq K$, so $c_n=k\geq K>M$.
:::

:::

::: {.pf-step #series-converges}
The series $\sum_{n=1}^\infty c_na_n$ converges.

::: pf-proof
All terms are nonnegative, so by step [](#weights-defined){.pf-ref} we may group them by blocks:
$$
\sum_{n=1}^\infty c_na_n
=\sum_{n=1}^{N_1-1}a_n
+\sum_{k=1}^\infty k\sum_{n=N_k}^{N_{k+1}-1}a_n.
$$
For each $k$, step [](#block-cutoffs){.pf-ref} gives
$$
k\sum_{n=N_k}^{N_{k+1}-1}a_n\leq kT_{N_k}<2^{-k}.
$$
Hence
$$
\sum_{n=1}^\infty c_na_n
\leq\sum_{n=1}^{N_1-1}a_n+\sum_{k=1}^\infty2^{-k}<\infty.
$$
:::

:::

::: pf-qed
Step [](#weights-defined){.pf-ref} gives positive weights tending to infinity, and step [](#series-converges){.pf-ref} gives
convergence of the corresponding weighted series.
:::

:::
:::
