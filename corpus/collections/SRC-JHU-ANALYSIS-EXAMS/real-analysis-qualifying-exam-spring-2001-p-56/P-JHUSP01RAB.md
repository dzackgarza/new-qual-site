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
Let $f\in L^1(\mathbb R^n)$. Prove that for every $\varepsilon>0$ there exists $\delta>0$ such that if $A$ is measurable and $|A|<\delta$, then
\[
\left|\int_A f\right|<\varepsilon.
\]
:::

::: {.solution}
Fix $\varepsilon>0$. Since $f\in L^1$, choose $M>0$ so that
\[
\int_{\{|f|>M\}}|f|<\frac{\varepsilon}{2}.
\]
Set
\[
\delta=\frac{\varepsilon}{2M}.
\]
If $|A|<\delta$, then
\[
\begin{aligned}
\left|\int_A f\right|
&\le\int_A|f|\\
&\le\int_{A\cap\{|f|\le M\}}|f|+\int_{\{|f|>M\}}|f|\\
&\le M|A|+\frac{\varepsilon}{2}\\
&<\varepsilon.
\end{aligned}
\]
Thus the Lebesgue integral is absolutely continuous with respect to Lebesgue measure.
:::
