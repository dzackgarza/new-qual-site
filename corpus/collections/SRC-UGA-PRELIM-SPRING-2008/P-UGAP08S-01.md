---
schema: qual/card@1
id: P-UGAP08S-01
kind: problem
title: Left cancellation by an injective function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction drops the subject of “is injective”; the surrounding statement uniquely forces this to be f, since f∘g=f∘h is left-cancelled.
---

::: {.problem}
Suppose $f,g,h:A\to A$ are functions. Prove that if $f$ is injective and
\[
f\circ g=f\circ h,
\]
then $g=h$.
:::
