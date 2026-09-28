---
schema: qual/card@1
id: P-WESRA03-I7
kind: problem
title: Define absolute continuity of one measure with respect to another
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 7 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Define what it means for a measure $\mu$ to be absolutely continuous with respect to a measure $\nu$ on $(X,\tau(X))$.
:::

::: {.solution}
One writes
\[
\mu\ll\nu
\]
and says that $\mu$ is absolutely continuous with respect to $\nu$ if every $\nu$-null measurable set is also $\mu$-null:
\[
\boxed{\nu(E)=0\Longrightarrow\mu(E)=0\qquad(E\in\tau(X)).}
\]
:::
