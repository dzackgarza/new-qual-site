---
schema: qual/card@1
id: P-RQN6N
kind: problem
title: Fixed points of continuous maps $S^2\to S^2$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Degree
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Spring 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the antipodal self-map is continuous and has no fixed point on S^2.
---

::: {.problem}
Prove or disprove:

Every continuous map from $S^2$ to $S^2$ has a fixed point.
:::

::: {.solution}
The statement is false.

::: pf

::: {.pf-step #s1}

Define the antipodal map
\[
a:S^2\longrightarrow S^2,
\qquad
a(x)=-x.
\]
Then $a$ is continuous.

::: pf-proof

The map
\[
\RR^3\longrightarrow\RR^3,
\qquad x\longmapsto -x
\]
is linear and hence continuous, and it preserves the unit sphere $S^2$.
Its restriction to $S^2$ is therefore continuous.

:::

:::

::: {.pf-step #s2}

The map $a$ has no fixed point.

::: pf-proof

If $x\in S^2$ were fixed, then
\[
x=a(x)=-x,
\]
so $2x=0$ and hence $x=0$.
But $0\notin S^2$.
Thus no point of $S^2$ is fixed by $a$.

:::

:::

::: pf-step

Therefore not every continuous self-map of $S^2$ has a fixed point.

::: pf-proof

The antipodal map from step [](#s1){.pf-ref} is a continuous self-map of $S^2$ and, by step [](#s2){.pf-ref}, is fixed-point-free.

:::

:::

:::

:::
