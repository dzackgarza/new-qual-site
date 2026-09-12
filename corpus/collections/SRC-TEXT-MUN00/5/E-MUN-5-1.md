---
schema: qual/card@1
id: E-MUN-5-1
kind: problem
title: Bijection between $A \times B$ and $B \times A$
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show there is a bijective correspondence of $A \times B$ with $B \times A$ .
:::

::: {.solution}
Define
\[
\tau:A\times B\longrightarrow B\times A,
\qquad
\tau(a,b)=(b,a).
\]
Then \(\tau\) is its own inverse:
\[
\tau(\tau(a,b))=(a,b).
\]
Hence \(\tau\) is bijective.
:::
