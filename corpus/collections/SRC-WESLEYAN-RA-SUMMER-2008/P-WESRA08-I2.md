---
schema: qual/card@1
id: P-WESRA08-I2
kind: problem
title: Define Lebesgue outer measure on the real line
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Outer Measure]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Theorems and Definitions item 2 of the Wesleyan Real Analysis Preliminary Examination, July 8, 2008, in analysis_2008-2013.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Give a precise definition of Lebesgue outer measure on the real line.
:::

::: solution
For $E\subseteq\mathbb R$, the **Lebesgue outer measure** of $E$ is
\[
m^*(E)
:=\inf\left\{
\sum_{k=1}^\infty |I_k|:
E\subseteq\bigcup_{k=1}^\infty I_k,
\ I_k\text{ open intervals}
\right\},
\]
where $|I_k|$ denotes the length of the interval $I_k$.

The infimum is taken over all countable open-interval covers of $E$; it may be $+\infty$.
:::
