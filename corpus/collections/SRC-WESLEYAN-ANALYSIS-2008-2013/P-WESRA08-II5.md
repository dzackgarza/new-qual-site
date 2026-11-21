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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the card's own argument into Lamport steps; the argument is correct and is
    kept in full. Two repairs to the statement and one to the hypothesis-use. Statement: the
    card had "Prove that V is complete", while the printed problem, retained extraction of the
    Wesleyan Real Analysis Preliminary Examination of July 8 2008, problem 5, line 728 of
    assets/attachments/analysis_2008-2013_extracted.md, reads "is complete with respect to its
    norm"; the phrase is restored. The extraction prints the space as garbled
    notation ("(V, parallel)" for the normed space and "(vec V, parallel parallel)" for the
    completion claim), which the card states in standard notation without loss. In the proof,
    the inductive choice of the subsequence is now shown to need strictly increasing indices
    as well as the small-difference bound, and the final step is split so that "a Cauchy
    sequence with a convergent subsequence converges to that limit" is proved rather than
    asserted.
---

::: {.problem}
Suppose that $(V,\norm{\cdot})$ is a real normed vector space in which every absolutely convergent series converges.
Prove that $V$ is complete with respect to its norm.
:::

::: {.solution}
No retained published solution set covers this problem — the collection's provenance is the MinerU extraction of the Wesleyan preliminary examinations, `assets/attachments/analysis_2008-2013_extracted.md`, which holds the question papers — so the argument is the card's own, in the standard form: a Cauchy sequence is thinned to one whose successive differences are summable, and the telescoped series converges by hypothesis.

Throughout, $(V,\norm\cdot)$ is a real normed vector space in which every absolutely convergent series converges, and $(x_n)_{n\ge1}$ is a Cauchy sequence in $V$.

::: pf

::: {.pf-step #subsequence}
There are indices $n_1<n_2<n_3<\cdots$ with $\norm{x_{n_{k+1}}-x_{n_k}}<2^{-k}$ for every $k\ge1$.

::: pf-proof
By the recursion theorem, define $n_1=1$ and, given $n_k$, choose $n_{k+1}$ by the Cauchy condition: with $\varepsilon=2^{-k}>0$ there is $N$ such that $\norm{x_p-x_q}<\varepsilon$ whenever $p,q\ge N$, and then any $n_{k+1}>\max\{n_k,N\}$ satisfies both $n_{k+1}>n_k$ and $\norm{x_{n_{k+1}}-x_{n_k}}<2^{-k}$. The indices are therefore strictly increasing, as the summation over $k$ below uses.
:::

:::

::: {.pf-step #summable}
$\sum_{k\ge1}\norm{x_{n_{k+1}}-x_{n_k}}\le\sum_{k\ge1}2^{-k}=1<\infty$, so the series $\sum_{k\ge1}(x_{n_{k+1}}-x_{n_k})$ is absolutely convergent, and by hypothesis it converges to some $y\in V$.

::: pf-proof
The terms are positive reals bounded by the geometric series, which converges with sum $1$; hence the series of norms converges, which is the definition of absolute convergence of the series of vectors. The hypothesis of the problem, applied to this series, produces $y\in V$ with $\sum_{k=1}^{N}(x_{n_{k+1}}-x_{n_k})\to y$ as $N\to\infty$.
:::

:::

::: {.pf-step #telescope}
The partial sums telescope: $\sum_{k=1}^{N}(x_{n_{k+1}}-x_{n_k})=x_{n_{N+1}}-x_{n_1}$. Hence $x_{n_{N+1}}\to x:=x_{n_1}+y$.

::: pf-proof
The sum expands as $(x_{n_2}-x_{n_1})+(x_{n_3}-x_{n_2})+\cdots+(x_{n_{N+1}}-x_{n_N})$, in which every interior term cancels, leaving $x_{n_{N+1}}-x_{n_1}$. By step [](#summable){.pf-ref} these partial sums tend to $y$, so $x_{n_{N+1}}=x_{n_1}+\big(x_{n_{N+1}}-x_{n_1}\big)\to x_{n_1}+y$ by continuity of addition; $x$ lies in $V$ because $V$ is a vector space.
:::

:::

::: {.pf-step #cauchysub}
A Cauchy sequence with a subsequence converging to $x$ converges to $x$.

::: pf-proof
Let $(z_m)$ be Cauchy and $z_{m_j}\to x$. Given $\varepsilon>0$, choose $N_0$ with $\norm{z_p-z_q}<\varepsilon/2$ for $p,q\ge N_0$, and $j$ with $m_j\ge N_0$ and $\norm{z_{m_j}-x}<\varepsilon/2$, possible because $m_j\to\infty$ and the subsequence converges. Then for every $p\ge N_0$,
$\norm{z_p-x}\le\norm{z_p-z_{m_j}}+\norm{z_{m_j}-x}<\varepsilon/2+\varepsilon/2=\varepsilon$,
so $z_p\to x$.
:::

:::

::: {.pf-step #complete}
Every Cauchy sequence in $V$ converges; hence $V$ is complete with respect to its norm.

::: pf-proof
Steps [](#subsequence){.pf-ref} and [](#telescope){.pf-ref} produce a subsequence of the given Cauchy sequence converging to $x\in V$, and step [](#cauchysub){.pf-ref} then gives $x_n\to x$. As the Cauchy sequence was arbitrary, every Cauchy sequence in $V$ converges, which is completeness of the normed space.
:::

:::

:::
:::
