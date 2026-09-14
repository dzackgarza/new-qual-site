---
schema: qual/card@1
id: P-WESRA07-I2
kind: problem
title: Define convergence in measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Give the definition of convergence in measure for a sequence of functions.
:::

::: solution
Let $(X,\mathcal A,\mu)$ be a measure space and let $f_n,f$ be measurable functions on $X$.
We say that $f_n$ converges to $f$ in measure if for every $\varepsilon>0$,
\[
\boxed{\mu\bigl(\{x\in X:|f_n(x)-f(x)|>\varepsilon\}\bigr)\longrightarrow0.}
\]
:::
