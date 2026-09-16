---
schema: qual/card@1
id: P-WESRA04-E2
kind: problem
title: A continuous bounded-variation function that is not absolutely continuous
classification:
  areas: [real-analysis]
  topics: [Absolute Continuity, Bounded Variation]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.2, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Give an example of a continuous function of bounded variation that is not absolutely continuous.
:::

::: {.solution}
The Cantor--Lebesgue function $F:[0,1]\to[0,1]$ is such an example.
It is continuous and nondecreasing, hence has bounded variation, with
\[
V_0^1(F)=F(1)-F(0)=1.
\]

Let $C$ be the middle-thirds Cantor set.
Then $m(C)=0$, while
\[
F(C)=[0,1].
\]
An absolutely continuous function maps Lebesgue-null sets to Lebesgue-null sets.
Since
\[
m(F(C))=1,
\]
$F$ cannot be absolutely continuous.
:::
