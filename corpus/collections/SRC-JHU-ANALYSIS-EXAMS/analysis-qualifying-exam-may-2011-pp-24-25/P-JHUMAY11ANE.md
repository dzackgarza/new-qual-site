---
schema: qual/card@1
id: P-JHUMAY11ANE
kind: problem
title: "The running maximum of a bounded C1 sequence converges uniformly"
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f_n\in C^1([0,1])$ satisfy
\[
f_n(t)\le5,
\qquad
|f_n'(t)|\le1
\]
for all $n,t$. Define
\[
g_n(t)=\max\{f_1(t),\ldots,f_n(t)\}.
\]
Prove that $(g_n)$ converges uniformly on $[0,1]$.
:::

::: {.solution}
Each $f_n$ is $1$-Lipschitz. The maximum of finitely many $1$-Lipschitz functions is again $1$-Lipschitz, so every $g_n$ is continuous and
\[
|g_n(s)-g_n(t)|\le|s-t|.
\]
Also
\[
g_n(t)\le g_{n+1}(t)\le5
\]
for every $t$. Hence the pointwise limit
\[
g(t)=\sup_n g_n(t)=\sup_n f_n(t)
\]
exists and is finite. Moreover, taking suprema in the Lipschitz estimate gives
\[
|g(s)-g(t)|\le|s-t|,
\]
so $g$ is continuous.

Thus $(g_n)$ is a monotone increasing sequence of continuous functions on the compact interval $[0,1]$ converging pointwise to the continuous function $g$. By Dini's theorem, the convergence is uniform.
:::
