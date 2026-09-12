---
schema: qual/card@1
id: E-AMD-KGEXBKIW
kind: problem
title: Cyclic groups are solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the proof to cyclic implies abelian implies derived length at most one.
---

::: {.exercise}
Show that every cyclic group is solvable.
:::

::: {.solution}
Every cyclic group is abelian. Hence its commutator subgroup is trivial:
\[
[G,G]=1.
\]
Therefore the derived series reaches the identity after one step, so $G$ is solvable.
:::
