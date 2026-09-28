---
schema: qual/card@1
id: P-WESRA07-I5
kind: problem
title: Define absolute continuity of measures
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Give the definition of absolute continuity for one measure with respect to another.
:::

::: {.solution}
Let $\mu$ and $\nu$ be measures on the same measurable space $(X,\mathcal A)$.
We say that $\mu$ is absolutely continuous with respect to $\nu$, and write
\[
\mu\ll\nu,
\]
if for every $E\in\mathcal A$,
\[
\boxed{\nu(E)=0\quad\Longrightarrow\quad\mu(E)=0.}
\]
:::
