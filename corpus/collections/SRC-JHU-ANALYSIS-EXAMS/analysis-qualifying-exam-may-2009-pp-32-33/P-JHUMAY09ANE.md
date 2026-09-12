---
schema: qual/card@1
id: P-JHUMAY09ANE
kind: problem
title: 'Convolution of two $L^2$ functions is bounded and continuous'
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, May 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f,g\in L^2(\mathbb R)$. Prove that
\[
(f*g)(x)=\int_{\mathbb R}f(y)g(x-y)\,dy
\]
defines a bounded continuous function on $\mathbb R$.
:::

::: {.solution}
For each $x$, Cauchy--Schwarz and translation invariance of the $L^2$ norm give
\[
|(f*g)(x)|\le \|f\|_2\,\|g(x-\cdot)\|_2=\|f\|_2\|g\|_2.
\]
Hence
\[
\|f*g\|_\infty\le\|f\|_2\|g\|_2.
\]

For continuity, let $h\to0$. Then
\[
(f*g)(x+h)-(f*g)(x)
=\int_{\mathbb R}f(y)\bigl(g(x+h-y)-g(x-y)\bigr)\,dy.
\]
Therefore, uniformly in $x$,
\[
|(f*g)(x+h)-(f*g)(x)|
\le\|f\|_2\,\|g(\cdot+h)-g\|_2.
\]
Translations are continuous in $L^2(\mathbb R)$, so the right-hand side tends to $0$ as $h\to0$. Thus $f*g$ is in fact uniformly continuous, and in particular continuous.
:::
