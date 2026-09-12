---
schema: qual/card@1
id: E-AMD-BKDDOBZG
kind: problem
title: An ideal containing a unit is the whole ring
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if an ideal $I\normal R$ contains a unit then $I = R$.
:::

::: {.solution}
Let \(u\in I\) be a unit. Then \(u^{-1}\in R\), and the ideal property gives
\[
1=u^{-1}u\in I
\]
(for a left ideal; equivalently \(1=uu^{-1}\in I\) for a right ideal).

Once \(1\in I\), every \(r\in R\) satisfies
\[
r=r\cdot1\in I.
\]
Hence \(I=R\).
:::
