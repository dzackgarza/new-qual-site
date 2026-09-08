---
schema: qual/card@1
id: P-JHUMAY11ANG
kind: problem
title: '$L^p$ norms converge to the $L^\infty$ norm on a probability space'
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
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^\infty([0,1])$.

(a) Prove that for $1<p<\infty$,
\[
\|f\|_p\le\|f\|_\infty.
\]

(b) Prove that
\[
\lim_{p\to\infty}\|f\|_p=\|f\|_\infty.
\]
:::

::: {.solution}
Let $M=\|f\|_\infty$. Since $[0,1]$ has measure $1$,
\[
\|f\|_p^p=\int_0^1|f|^p\le M^p,
\]
so
\[
\|f\|_p\le M.
\]
This proves part (a) and gives
\[
\limsup_{p\to\infty}\|f\|_p\le M.
\]

Fix $\varepsilon>0$. By the definition of essential supremum,
\[
A_\varepsilon=\{x:|f(x)|>M-\varepsilon\}
\]
has positive measure whenever $M>0$. Therefore
\[
\|f\|_p^p\ge (M-\varepsilon)^p m(A_\varepsilon),
\]
so
\[
\|f\|_p\ge (M-\varepsilon)m(A_\varepsilon)^{1/p}.
\]
Letting $p\to\infty$ gives
\[
\liminf_{p\to\infty}\|f\|_p\ge M-\varepsilon.
\]
Since $\varepsilon>0$ is arbitrary,
\[
\liminf_{p\to\infty}\|f\|_p\ge M.
\]
Combining the liminf and limsup bounds yields
\[
\boxed{\lim_{p\to\infty}\|f\|_p=\|f\|_\infty}.
\]
The case $M=0$ is immediate.
:::
