---
schema: qual/card@1
id: P-WESRA07-I6
kind: problem
title: State the Radon--Nikodym theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Part I, item 6 of the Real Analysis section of the Wesleyan University Analysis Qualifier, Summer 2007, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Give a precise statement of the Radon--Nikodym theorem.
:::

::: solution
Let $(X,\mathcal A)$ be a measurable space, and let $\mu$ and $\nu$ be sigma-finite positive measures on it. If
\[
\mu\ll\nu,
\]
then there exists a measurable function $h:X\to[0,\infty]$ such that
\[
\mu(E)=\int_E h\,d\nu
\qquad\text{for every }E\in\mathcal A.
\]
The function $h$ is unique up to $\nu$-almost-everywhere equality and is denoted
\[
\boxed{h=\frac{d\mu}{d\nu}.}
\]
:::
