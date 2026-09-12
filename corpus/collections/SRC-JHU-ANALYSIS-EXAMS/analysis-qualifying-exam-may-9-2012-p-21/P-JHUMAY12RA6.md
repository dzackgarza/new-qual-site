---
schema: qual/card@1
id: P-JHUMAY12RA6
kind: problem
title: 'Absolutely convergent series of $L^1$ functions converges a.e. and in $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, May 9, 2012, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(g_k)\subset L^1(\mathbb R^n)$ and suppose
\[
\sum_{k=1}^\infty\|g_k\|_1<\infty.
\]

(a) Show that $\sum_{k=1}^\infty g_k$ converges almost everywhere to some $g\in L^1$.

(b) Show that the partial sums converge to $g$ in $L^1$.
:::

::: {.solution}
By Tonelli's theorem,
\[
\int_{\mathbb R^n}\sum_{k=1}^\infty|g_k(x)|\,dx
=\sum_{k=1}^\infty\|g_k\|_1<\infty.
\]
Therefore
\[
\sum_{k=1}^\infty|g_k(x)|<\infty
\]
for almost every $x$. Hence $\sum g_k(x)$ converges absolutely almost everywhere; define its sum there to be $g(x)$ and set $g=0$ on the null exceptional set. Moreover,
\[
|g(x)|\le\sum_{k=1}^\infty|g_k(x)|,
\]
so $g\in L^1$.

If $S_N=\sum_{k=1}^Ng_k$, then almost everywhere
\[
|g-S_N|\le\sum_{k>N}|g_k|.
\]
Thus
\[
\|g-S_N\|_1
\le\sum_{k>N}\|g_k\|_1\longrightarrow0.
\]
Therefore the series converges both almost everywhere and in $L^1$.
:::
