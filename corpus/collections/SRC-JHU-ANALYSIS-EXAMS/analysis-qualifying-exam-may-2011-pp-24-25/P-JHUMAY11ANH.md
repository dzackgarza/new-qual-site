---
schema: qual/card@1
id: P-JHUMAY11ANH
kind: problem
title: 'Weak $L^2$ convergence: lower semicontinuity and strong convergence from norm convergence'
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
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $f_j\rightharpoonup f$ weakly in $L^2(\mathbb R^n)$.

(a) Prove
\[
\|f\|_2\le\liminf_j\|f_j\|_2,
\]
and give an example of strict inequality.

(b) If $\|f_j\|_2\to\|f\|_2$, prove $\|f_j-f\|_2\to0$.
:::

::: {.solution}
If $f\ne0$, test weak convergence against $g=f/\|f\|_2$. Then
\[
\|f\|_2=\lim_j|\langle f_j,g\rangle|\le\liminf_j\|f_j\|_2.
\]
The case $f=0$ is immediate.

Strict inequality occurs for any orthonormal sequence $(e_j)$: one has $e_j\rightharpoonup0$ by Bessel's inequality, while $\|e_j\|_2=1$.

For part (b), weak convergence gives
\[
\langle f_j,f\rangle\to\|f\|_2^2.
\]
Hence
\[
\|f_j-f\|_2^2
=\|f_j\|_2^2+\|f\|_2^2-2\operatorname{Re}\langle f_j,f\rangle\longrightarrow0.
\]
Thus $f_j\to f$ strongly in $L^2$.
:::
