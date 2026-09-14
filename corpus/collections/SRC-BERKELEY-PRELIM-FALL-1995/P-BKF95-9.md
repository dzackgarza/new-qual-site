---
schema: qual/card@1
id: P-BKF95-9
kind: problem
title: A nonlinear recurrence stays bounded away from zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md; Flash garbles the placement of $\liminf$ and $n\to\infty$, restored from the deterministic sentence.
---

::: {.problem}
Let $0<x_1<1$ and define
\[
x_{n+1}=x_n-x_n^{n+1}.
\]
Show that
\[
\liminf_{n\to\infty}x_n>0.
\]
:::
