---
schema: qual/card@1
id: E-AMD-SD3PTZ4O
kind: problem
title: The union of two ideals need not be an ideal
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Kept the minimal counterexample in Z and removed redundant scaffolding.
---

::: {.exercise}
Show that the union of two ideals need not be an ideal.
:::

::: {.solution}
In $\mathbb Z$, let
\[
I=2\mathbb Z,\qquad J=3\mathbb Z.
\]
Then $2\in I\subseteq I\cup J$ and $3\in J\subseteq I\cup J$, but
\[
2+3=5\notin I\cup J.
\]
Thus $I\cup J$ is not closed under addition and hence is not an ideal.
:::
