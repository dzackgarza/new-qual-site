---
schema: qual/card@1
id: P-JHUU45RA3
kind: problem
title: Banach space characterization via absolutely convergent series
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 3 of the undated JHU Real and Complex Analysis exam on pp. 4–5 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Prove that a normed vector space $(X,\|\cdot\|)$ is Banach if and only if every series
\[
\sum_{n=1}^\infty x_n
\]
with
\[
\sum_{n=1}^\infty\|x_n\|<\infty
\]
converges in $X$.
:::

::: {.solution}
<1>1. If $X$ is Banach, every absolutely convergent series converges.
::: {.proof}
Suppose
\[
\sum_{n=1}^\infty\|x_n\|<\infty
\]
and let
\[
s_N=\sum_{n=1}^N x_n.
\]
If $M>N$, then
\[
\|s_M-s_N\|
=\left\|\sum_{n=N+1}^M x_n\right\|
\le\sum_{n=N+1}^M\|x_n\|.
\]
Because the scalar series of norms converges, the right-hand side tends to $0$ uniformly in $M>N$ as $N\to\infty$. Thus $(s_N)$ is Cauchy. Since $X$ is complete, $(s_N)$ converges in $X$.
:::

<1>2. If every absolutely convergent series converges, then $X$ is Banach.
::: {.proof}
Let $(y_n)$ be a Cauchy sequence in $X$. Choose a subsequence $(y_{n_k})$ such that
\[
\|y_{n_{k+1}}-y_{n_k}\|<2^{-k}
\qquad(k\ge1).
\]
Then
\[
\sum_{k=1}^\infty\|y_{n_{k+1}}-y_{n_k}\|
\le\sum_{k=1}^\infty2^{-k}<\infty.
\]
By hypothesis, the series
\[
\sum_{k=1}^\infty (y_{n_{k+1}}-y_{n_k})
\]
converges in $X$. Its partial sums telescope:
\[
\sum_{k=1}^{N}(y_{n_{k+1}}-y_{n_k})=y_{n_{N+1}}-y_{n_1}.
\]
Hence the subsequence $(y_{n_k})$ converges to some $y\in X$.

Since the original sequence $(y_n)$ is Cauchy, convergence of one subsequence forces the whole sequence to converge to the same limit: given $\varepsilon>0$, choose $N$ so that
\[
\|y_n-y_m\|<\varepsilon/2
\qquad(n,m\ge N),
\]
and then choose $k$ with $n_k\ge N$ and
\[
\|y_{n_k}-y\|<\varepsilon/2.
\]
For every $n\ge N$,
\[
\|y_n-y\|
\le\|y_n-y_{n_k}\|+\|y_{n_k}-y\|<\varepsilon.
\]
Thus every Cauchy sequence in $X$ converges, so $X$ is Banach.
:::
:::
