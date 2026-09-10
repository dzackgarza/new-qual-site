---
schema: qual/card@1
id: P-WESRA03-I2
kind: problem
title: Define a measure on a measurable space
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Short Answer Question 2 of the Wesleyan Preliminary Exam in Analysis, August 4, 2003, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Define a measure on a measurable space $(Y,\tau(Y))$.
:::

::: solution
A measure on $(Y,\tau(Y))$ is a function
\[
\mu:\tau(Y)\to[0,\infty]
\]
such that
\[
\mu(\varnothing)=0
\]
and, for every pairwise disjoint sequence $(E_n)$ in $\tau(Y)$,
\[
\boxed{\mu\!\left(\bigcup_{n=1}^\infty E_n\right)=\sum_{n=1}^\infty\mu(E_n).}
\]
:::
