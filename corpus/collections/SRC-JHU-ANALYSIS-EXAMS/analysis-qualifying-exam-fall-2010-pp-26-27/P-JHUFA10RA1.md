---
schema: qual/card@1
id: P-JHUFA10RA1
kind: problem
title: '$L^2$ convergence with Gaussian weight'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the Fall 2010 JHU analysis qualifying-exam statement preserved in this collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose that $f_j \in L^2(\mathbb{R}^n)$, $j = 1, 2, 3, \ldots$ and that $f_j \to f$ in $L^2$.
Suppose further that there is a constant $M < \infty$ so that

$$\int e^{100|x|^2} |f_j(x)|^2 \, dx \leq M, \quad j = 1, 2, 3, \ldots.$$

Is it true that $\int e^{99|x|^2} |f(x)|^2 \, dx < \infty$?
Give a proof or counterexample.
:::

::: {.solution}
Yes. In fact the stronger estimate
\[
\int_{\mathbb R^n} e^{100|x|^2}|f(x)|^2\,dx\le M
\]
holds.

<1>1. Extract a subsequence converging almost everywhere.
::: {.proof}
Since $f_j\to f$ in $L^2(\mathbb R^n)$, there is a subsequence $f_{j_k}$ such that
\[
f_{j_k}(x)\longrightarrow f(x)
\]
for almost every $x\in\mathbb R^n$.
For instance, choose the subsequence so that
\[
\|f_{j_k}-f\|_2^2\le 2^{-k},
\]
and apply Tonelli to
\[
\sum_{k=1}^\infty |f_{j_k}-f|^2.
\]
Its integral is finite, so the series is finite almost everywhere; hence its terms tend to zero almost everywhere.
:::

<1>2. Apply Fatou's lemma with the Gaussian weight.
::: {.proof}
For almost every $x$,
\[
e^{100|x|^2}|f_{j_k}(x)|^2
\longrightarrow
e^{100|x|^2}|f(x)|^2.
\]
These functions are nonnegative, so Fatou's lemma gives
\[
\int_{\mathbb R^n} e^{100|x|^2}|f(x)|^2\,dx
\le
\liminf_{k\to\infty}
\int_{\mathbb R^n} e^{100|x|^2}|f_{j_k}(x)|^2\,dx
\le M.
\]
Since $e^{99|x|^2}\le e^{100|x|^2}$,
\[
\int_{\mathbb R^n} e^{99|x|^2}|f(x)|^2\,dx\le M<\infty.
\]
:::
:::
