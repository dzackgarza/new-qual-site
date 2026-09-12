---
schema: qual/card@1
id: P-TQGAM
kind: problem
title: Stabilizers need not be normal
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Normal Subgroups
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
- Show that the stabilizer of an element need not be a normal subgroup?
:::

::: {.solution}
Let $S_3$ act naturally on $\{1,2,3\}$. The stabilizer of $1$ is
\[
G_1=\{e,(23)\}.
\]
But
\[
(12)(23)(12)^{-1}=(13)\notin G_1.
\]
Hence $G_1$ is not invariant under conjugation, so
\[
G_1\not\trianglelefteq S_3.
\]
Thus stabilizers need not be normal subgroups.
:::
