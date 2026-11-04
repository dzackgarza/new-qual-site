---
schema: qual/card@1
id: P-TAMURAS15-02
kind: problem
title: An $L^1$-convergent sequence has an a.e.-convergent subsequence
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Convergence of Functions
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $\{g_n\}_{n=1}^\infty$ and $g$ be in $L^1(\RR)$ and satisfy
$$
\lim_{n\to\infty}\norm{g_n-g}_1=0.
$$
Prove that there is a subsequence of $\{g_n\}_{n=1}^\infty$ that converges pointwise almost everywhere to $g$.
:::

::: {.solution}
Convergence in $L^1$ controls the sum of the distances along a sparse subsequence, and a summable sequence of functions is finite almost everywhere.

::: pf

::: {.pf-step #subsequence}
There are indices $n_1<n_2<\cdots$ with $\norm{g_{n_k}-g}_1<2^{-k}$.

::: pf-proof
Since $\norm{g_n-g}_1\to0$, for each $k$ the set of $n$ with $\norm{g_n-g}_1<2^{-k}$ contains all sufficiently large $n$.
Choosing $n_k$ recursively, each larger than $n_{k-1}$ and large enough for the $k$-th bound, gives the required increasing sequence.
:::

:::

::: {.pf-step #summable}
$\sum_{k\ge1}\abs{g_{n_k}(x)-g(x)}<\infty$ for almost every $x$.

::: pf-proof
Put $F(x)=\sum_{k\ge1}\abs{g_{n_k}(x)-g(x)}$, a measurable function with values in $[0,\infty]$.
By the monotone convergence theorem and step [](#subsequence){.pf-ref},
$$
\int F\,d\mu=\sum_{k\ge1}\int\abs{g_{n_k}-g}\,d\mu\le\sum_{k\ge1}2^{-k}=1<\infty.
$$
A nonnegative measurable function with finite integral is finite almost everywhere, so $F(x)<\infty$ almost everywhere.
:::

:::

::: {.pf-step #converges}
$g_{n_k}(x)\to g(x)$ for almost every $x$.

::: pf-proof
Where $F(x)$ is finite the terms $\abs{g_{n_k}(x)-g(x)}$ are the terms of a convergent series, so they tend to $0$; by step [](#summable){.pf-ref} this holds almost everywhere.
:::

:::

:::
:::
