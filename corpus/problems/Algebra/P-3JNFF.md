---
schema: qual/card@1
id: P-3JNFF
kind: problem
title: Normal subgroups of $A_4$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Find all normal subgroups of $A_4$.
:::

::: {.solution}
The conjugacy classes of $A_4$ have sizes
\[
1,\qquad 3,\qquad 4,\qquad 4.
\]
The class of size $3$ is
\[
\{(12)(34),(13)(24),(14)(23)\}.
\]
A normal subgroup is a union of conjugacy classes containing the identity, and its order must divide $12$.

The only possible class-unions with order dividing $12$ are therefore
\[
\{e\},\qquad
V_4=\{e,(12)(34),(13)(24),(14)(23)\},\qquad
A_4.
\]
The set $V_4$ is a subgroup (indeed the Klein four-group), and it is normal because it is a union of conjugacy classes. Hence these are exactly the normal subgroups of $A_4$.
:::
