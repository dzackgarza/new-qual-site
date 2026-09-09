---
schema: qual/card@1
id: P-JHUMAY11ANJ
kind: problem
title: 'Characteristic-function convolution is continuous and yields differentiation averages'
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $E,F\subset\mathbb R$ be measurable sets of finite measure.

(a) Prove that $\chi_E*\chi_F$ is continuous.

(b) Prove that
\[
n(\chi_E*\chi_{[0,1/n]})(x)\longrightarrow\chi_E(x)
\]
for almost every $x$.
:::

::: {.solution}
Since $|E|,|F|<\infty$, one has $\chi_E,\chi_F\in L^2(\mathbb R)$. For $h\to0$,
\[
\begin{aligned}
|((\chi_E*\chi_F)(x+h)-(\chi_E*\chi_F)(x))|
&\le \|\chi_E\|_2\,\|\chi_F(\cdot+h)-\chi_F\|_2.
\end{aligned}
\]
The right-hand side tends to $0$ by continuity of translations in $L^2$, uniformly in $x$. Hence the convolution is continuous.

For part (b),
\[
\begin{aligned}
n(\chi_E*\chi_{[0,1/n]})(x)
&=n\int_{\mathbb R}\chi_E(y)\chi_{[0,1/n]}(x-y)\,dy\\
&=n\int_{x-1/n}^{x}\chi_E(y)\,dy.
\end{aligned}
\]
This is the left-sided average of $\chi_E$ over an interval shrinking to $x$. By the Lebesgue differentiation theorem, it converges to $\chi_E(x)$ for almost every $x$.
:::
