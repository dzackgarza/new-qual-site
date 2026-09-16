---
schema: qual/card@1
id: P-TRIV-CA10
kind: problem
title: Image of a disk under the principal branch of $\log z$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Added a remark that Complex Analysis Problem 10 on page 14 of the source PDF does not state the center of the disk.
---

::: {.problem}
Take a disk of radius $R$ with a branch cut on the negative real axis; what does $\log z$ map this onto?
Where is the origin mapped onto?
:::

::: {.remark}
The source does not state the center of the disk.
The question about the image of the origin suggests the disk $\{z : |z| < R\}$ centered at $0$, with the cut along $(-R, 0]$; the source does not say so, and $\log z$ is not defined at the branch point $z = 0$.
:::
