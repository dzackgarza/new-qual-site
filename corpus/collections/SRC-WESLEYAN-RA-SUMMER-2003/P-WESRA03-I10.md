---
schema: qual/card@1
id: P-WESRA03-I10
kind: problem
title: Define the $L^p$ norm
classification:
  areas: [real-analysis]
  topics: [Function Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 10 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
What is meant by the $L^p$ norm of a function on a measure space $(Y,\tau(Y),\mu)$?
:::

::: solution
For $1\le p<\infty$, the $L^p$ norm of a measurable function $f$ is
\[
\boxed{\|f\|_p=\left(\int_Y|f|^p\,d\mu\right)^{1/p}.}
\]
The space $L^p(Y,\mu)$ consists of almost-everywhere equivalence classes for which this quantity is finite.

For $p=\infty$,
\[
\boxed{\|f\|_\infty=\operatorname*{ess\,sup}_{y\in Y}|f(y)|.}
\]
:::
