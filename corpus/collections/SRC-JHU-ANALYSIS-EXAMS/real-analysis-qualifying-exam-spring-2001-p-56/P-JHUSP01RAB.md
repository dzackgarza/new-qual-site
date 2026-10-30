---
schema: qual/card@1
id: P-JHUSP01RAB
kind: problem
title: "Absolute continuity of the Lebesgue integral"
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^1(\RR^n)$. Prove that for every $\varepsilon>0$ there exists $\delta>0$ such that if $A$ is measurable and $\setmeasure{A}<\delta$, then
$$
\abs{\int_A f}<\varepsilon.
$$
:::

::: {.solution}
Fix $\varepsilon>0$. Since $f\in L^1$, choose $M>0$ so that
$$
\int_{\{\abs{f}>M\}}\abs{f}<\frac{\varepsilon}{2}.
$$
Set
$$
\delta=\frac{\varepsilon}{2M}.
$$
If $\setmeasure{A}<\delta$, then
$$
\begin{aligned}
\abs{\int_A f}
&\le\int_A\abs{f}\\
&\le\int_{A\cap\{\abs{f}\le M\}}\abs{f}+\int_{\{\abs{f}>M\}}\abs{f}\\
&\le M\setmeasure{A}+\frac{\varepsilon}{2}\\
&<\varepsilon.
\end{aligned}
$$
Thus the Lebesgue integral is absolutely continuous with respect to Lebesgue measure.
:::
