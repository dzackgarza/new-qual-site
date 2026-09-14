---
schema: qual/card@1
id: P-WESRA03-I4
kind: problem
title: State the Lebesgue dominated convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
State the Lebesgue Dominated Convergence Theorem.
:::

::: solution
Let $(X,\mathcal A,\mu)$ be a measure space and let $f_n$ be measurable functions such that
\[
f_n\to f\quad\text{almost everywhere}.
\]
Suppose there is $g\in L^1(\mu)$ with
\[
|f_n|\le g\quad\text{almost everywhere for every }n.
\]
Then $f\in L^1(\mu)$,
\[
\|f_n-f\|_1\to0,
\]
and in particular
\[
\boxed{\int_X f_n\,d\mu\longrightarrow\int_X f\,d\mu.}
\]
:::
