---
schema: qual/card@1
id: P-CQR3X
kind: problem
title: A finite group is solvable iff its composition factors have prime order
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Let $G$ be a finite group.
Prove that $G$ is solvable if and only if all of its composition factors are of prime order (i.e. cyclic groups $\ZZ_p$).
:::

::: {.solution}

::: pf

::: {.pf-step #forward}
If $G$ is solvable, then every composition factor of $G$ has prime order.

::: pf-proof
Every subquotient of a solvable group is solvable, so every composition factor $S$ of $G$ is simple and solvable.
Since $S$ is solvable and nontrivial, $[S,S]\ne S$.
Since $[S,S]\trianglelefteq S$ and $S$ is simple, $[S,S]=1$, so $S$ is abelian.
A finite simple abelian group is cyclic of prime order.
:::

:::

::: pf-qed
Step [](#forward){.pf-ref} proves one implication.
Conversely, suppose every composition factor of $G$ has prime order, and let $1=G_0\triangleleft G_1\triangleleft\cdots\triangleleft G_r=G$ be a composition series.
Each factor $G_{i+1}/G_i$ has prime order, so it is cyclic and therefore abelian.
Thus this series is a subnormal series with abelian factors, and $G$ is solvable.
:::

:::

:::
