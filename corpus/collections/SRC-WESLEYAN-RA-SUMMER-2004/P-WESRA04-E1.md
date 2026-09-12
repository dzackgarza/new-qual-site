---
schema: qual/card@1
id: P-WESRA04-E1
kind: problem
title: A positive-measure subset of $[0,1]$ with empty interior
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Real Analysis section 2.2, item 1 of the Wesleyan Preliminary Examination, August 2, 2004, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Give an example of a subset of $[0,1]$ with positive Lebesgue measure whose closure contains no nonempty open interval.
:::

::: solution
Take the Smith--Volterra--Cantor set $S\subset[0,1]$. It is closed and nowhere dense, and
\[
m(S)=\frac12.
\]
Since $S$ is closed,
\[
\overline S=S,
\]
and nowhere density means that $S$ contains no nonempty open interval. Thus $S$ has the required properties.
:::
