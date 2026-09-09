---
schema: qual/card@1
id: P-JHUSP08ANA
kind: problem
title: "Convolutions of characteristic functions of finite-measure sets"
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Analysis Qualifying Exam, Spring 2008, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $E,F\subset\mathbb R$ be measurable sets of finite measure.

(a) Show that $\chi_E*\chi_F$ is continuous.

(b) Show that
\[
n\bigl(\chi_E*\chi_{[0,1/n]}\bigr)\to\chi_E
\]
pointwise almost everywhere.
:::

::: {.solution}
<1>1. The convolution is continuous.
::: {.proof}
Since $E$ and $F$ have finite measure,
\[
\chi_E,\chi_F\in L^2(\mathbb R).
\]
For $h\in\mathbb R$,
\[
\begin{aligned}
| (\chi_E*\chi_F)(x+h)-(\chi_E*\chi_F)(x) |
&\le \|\chi_E\|_2\,\|\chi_F(\cdot+h)-\chi_F\|_2.
\end{aligned}
\]
The right-hand side is independent of $x$ and tends to $0$ as $h\to0$ by continuity of translations in $L^2$. Hence $\chi_E*\chi_F$ is uniformly continuous, in particular continuous.
:::

<1>2. The normalized interval convolutions converge almost everywhere to $\chi_E$.
::: {.proof}
For every $x$,
\[
\begin{aligned}
n(\chi_E*\chi_{[0,1/n]})(x)
&=n\int_{\mathbb R}\chi_E(y)\chi_{[0,1/n]}(x-y)\,dy\\
&=n\int_{x-1/n}^{x}\chi_E(y)\,dy.
\end{aligned}
\]
Thus this is the average of $\chi_E$ over the interval $[x-1/n,x]$. By the one-sided Lebesgue differentiation theorem, for almost every $x$,
\[
n\int_{x-1/n}^{x}\chi_E(y)\,dy\longrightarrow\chi_E(x).
\]
This proves the claim.
:::
:::
