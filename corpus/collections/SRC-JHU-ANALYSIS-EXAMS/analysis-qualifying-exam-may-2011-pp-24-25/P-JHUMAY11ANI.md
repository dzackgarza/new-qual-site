---
schema: qual/card@1
id: P-JHUMAY11ANI
kind: problem
title: Gaussian-weighted $L^2$ bounds pass to an $L^2$ limit
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 1 of the May 2011 JHU analysis qualifying exam in the preserved compiled source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Suppose $f_j\in L^2(\mathbb R^n)$ and $f_j\to f$ in $L^2(\mathbb R^n)$. Suppose further that there is a constant $M<\infty$ such that
\[
\int_{\mathbb R^n} e^{100|x|^2}|f_j(x)|^2\,dx\le M
\qquad(j=1,2,\dots).
\]
Is it true that
\[
\int_{\mathbb R^n} e^{99|x|^2}|f(x)|^2\,dx<\infty?
\]
Give a proof or counterexample.
:::

::: solution
Yes. In fact the stronger $100$-weighted estimate passes to the limit.

<1>1. Extract an almost-everywhere convergent subsequence.
::: proof
Since $f_j\to f$ in $L^2(\mathbb R^n)$, there is a subsequence $f_{j_k}$ such that
\[
f_{j_k}(x)\to f(x)
\]
for almost every $x\in\mathbb R^n$.
:::

<1>2. Apply Fatou's lemma to the nonnegative weighted squares.
::: proof
For almost every $x$,
\[
e^{100|x|^2}|f_{j_k}(x)|^2\longrightarrow e^{100|x|^2}|f(x)|^2.
\]
Hence Fatou's lemma gives
\[
\int_{\mathbb R^n}e^{100|x|^2}|f(x)|^2\,dx
\le
\liminf_{k\to\infty}
\int_{\mathbb R^n}e^{100|x|^2}|f_{j_k}(x)|^2\,dx
\le M.
\]
Since $e^{99|x|^2}\le e^{100|x|^2}$,
\[
\boxed{
\int_{\mathbb R^n}e^{99|x|^2}|f(x)|^2\,dx\le M<\infty.}
\]
:::
:::
