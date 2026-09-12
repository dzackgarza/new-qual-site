---
schema: qual/card@1
id: P-RAF18A
kind: problem
title: "L^1 convergence from a.e. convergence with uniformly bounded running maxima"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\{f_n\}_n \subset L^1(\mathbb{R}, m)$ be a sequence of functions such that $f_n \to 0$, $m$-almost everywhere.
Assume that there exists $M < \infty$ such that
$$
\int_{\mathbb{R}} \max(|f_1|, |f_2|, \ldots, |f_n|)\,dm \leq M, \quad \text{for every } n \geq 1.
$$
Prove that $\lim_{n \to \infty} \|f_n\|_1 = 0$.
:::

::: solution
<1>1. Build a single integrable dominating function.
::: proof
Define
\[
g_n:=\max(|f_1|,\ldots,|f_n|).
\]
Then
\[
0\le g_1\le g_2\le\cdots
\]
and by hypothesis
\[
\int_{\mathbb R}g_n\,dm\le M
\qquad\text{for every }n.
\]
Let
\[
g:=\lim_{n\to\infty}g_n=\sup_n|f_n|.
\]
By the Monotone Convergence Theorem,
\[
\int_{\mathbb R}g\,dm
=\lim_{n\to\infty}\int_{\mathbb R}g_n\,dm
\le M.
\]
Thus $g\in L^1(\mathbb R)$.
:::

<1>2. Apply dominated convergence.
::: proof
For every $n$,
\[
|f_n|\le g,
\]
and by assumption $f_n\to0$ almost everywhere. Since $g\in L^1$, the Dominated Convergence Theorem gives
\[
\int_{\mathbb R}|f_n|\,dm\longrightarrow0.
\]
Hence
\[
\boxed{\|f_n\|_1\to0.}
\]
:::
:::
