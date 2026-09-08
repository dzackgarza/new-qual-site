---
schema: qual/card@1
id: P-JHUFA05AND
kind: problem
title: Weak Lower Semicontinuity of the Norm and Strong Convergence
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the JHU Analysis Qualifying Exam, September 2005, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_n)$ be a sequence in a Hilbert space $X$ such that $f_n\rightharpoonup f$, meaning
\[
\langle f_n,g\rangle\to\langle f,g\rangle
\qquad(g\in X).
\]

(a) Prove that
\[
\|f\|\le \liminf_{n\to\infty}\|f_n\|,
\]
and give an example where the inequality is strict.

(b) If in addition $\|f_n\|\to\|f\|$, prove that $f_n\to f$ in norm.
:::

::: {.solution}
<1>1. The norm is weakly lower semicontinuous.
::: {.proof}
If $f=0$, the claimed inequality is immediate. Assume $f\ne0$ and set
\[
g=\frac{f}{\|f\|}.
\]
Then $\|g\|=1$, so by Cauchy--Schwarz
\[
|\langle f_n,g\rangle|\le\|f_n\|.
\]
Weak convergence gives
\[
\langle f_n,g\rangle\longrightarrow\langle f,g\rangle=\|f\|.
\]
Therefore
\[
\|f\|
=\lim_{n\to\infty}|\langle f_n,g\rangle|
\le\liminf_{n\to\infty}\|f_n\|.
\]
:::

<1>2. Strict inequality can occur.
::: {.proof}
Take $X=\ell^2(\mathbb N)$ and let $e_n$ be the standard orthonormal basis. For every $g=(g_k)\in\ell^2$, one has $g_n\to0$, hence
\[
\langle e_n,g\rangle=g_n\longrightarrow0.
\]
Thus $e_n\rightharpoonup0$. But
\[
\|e_n\|=1
\qquad\text{for all }n,
\]
so
\[
0=\|0\|<1=\liminf_n\|e_n\|.
\]
:::

<1>3. Weak convergence plus convergence of norms implies norm convergence.
::: {.proof}
Since $f_n\rightharpoonup f$, taking the test vector $g=f$ gives
\[
\langle f_n,f\rangle\longrightarrow\langle f,f\rangle=\|f\|^2.
\]
Using the Hilbert-space identity,
\[
\|f_n-f\|^2
=\|f_n\|^2+\|f\|^2-2\operatorname{Re}\langle f_n,f\rangle.
\]
By hypothesis, $\|f_n\|\to\|f\|$, so the right-hand side tends to
\[
\|f\|^2+\|f\|^2-2\|f\|^2=0.
\]
Hence
\[
\|f_n-f\|\longrightarrow0,
\]
which is exactly strong convergence.
:::
:::
