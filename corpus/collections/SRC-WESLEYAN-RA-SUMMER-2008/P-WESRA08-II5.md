---
schema: qual/card@1
id: P-WESRA08-II5
kind: problem
title: Absolute convergence of series characterizes completeness
classification:
  areas: [real-analysis]
  topics: [Banach Spaces, Completeness, Series]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose that $(V,\|\cdot\|)$ is a real normed vector space in which every absolutely convergent series converges.
Prove that $V$ is complete.
:::

::: {.solution}
Let $(x_n)$ be a Cauchy sequence in $V$.
We prove that it converges.

Choose inductively indices
\[
n_1<n_2<n_3<\cdots
\]
such that
\[
\|x_{n_{k+1}}-x_{n_k}\|<2^{-k}
\]
for every $k\ge1$.
This is possible because $(x_n)$ is Cauchy.

Then
\[
\sum_{k=1}^\infty
\|x_{n_{k+1}}-x_{n_k}\|
\le \sum_{k=1}^\infty2^{-k}<\infty.
\]
Hence the series
\[
\sum_{k=1}^\infty (x_{n_{k+1}}-x_{n_k})
\]
is absolutely convergent.
By hypothesis it converges in $V$, say to $y$.

Its partial sums telescope:
\[
\sum_{k=1}^{N}(x_{n_{k+1}}-x_{n_k})
=x_{n_{N+1}}-x_{n_1}.
\]
Therefore
\[
x_{n_{N+1}}\longrightarrow x_{n_1}+y=:x\in V.
\]
So the Cauchy sequence has a convergent subsequence.

Finally, a Cauchy sequence with a subsequence converging to $x$ must itself converge to $x$.
Indeed, given $\varepsilon>0$, choose $N_0$ so that
\[
\|x_m-x_n\|<\varepsilon/2
\]
for $m,n\ge N_0$, and then choose $k$ with $n_k\ge N_0$ and
\[
\|x_{n_k}-x\|<\varepsilon/2.
\]
For every $n\ge N_0$,
\[
\|x_n-x\|
\le \|x_n-x_{n_k}\|+\|x_{n_k}-x\|
<\varepsilon.
\]
Thus $x_n\to x$, and $V$ is complete.
:::
