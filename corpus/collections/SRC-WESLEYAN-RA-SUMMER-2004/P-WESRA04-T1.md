---
schema: qual/card@1
id: P-WESRA04-T1
kind: problem
title: State the Lebesgue monotone convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Real Analysis section 2.1, item 1 of the Wesleyan Preliminary Examination, August 2, 2004, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
State the Lebesgue monotone convergence theorem.
:::

::: solution
Let $(X,\mathcal A,\mu)$ be a measure space and let
\[
0\le f_1\le f_2\le\cdots
\]
be measurable functions. If
\[
f(x)=\lim_{n\to\infty}f_n(x)
\]
pointwise, with values allowed in $[0,\infty]$, then
\[
\boxed{
\int_X f\,d\mu
=
\lim_{n\to\infty}\int_X f_n\,d\mu.}
\]
Both sides are allowed to equal $+\infty$.
:::
