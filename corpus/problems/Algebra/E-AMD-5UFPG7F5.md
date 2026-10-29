---
schema: qual/card@1
id: E-AMD-5UFPG7F5
kind: problem
title: An ideal is maximal iff the quotient is a field
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source states the claim for an ideal I of an unspecified ring R; it is false for noncommutative rings (the zero ideal of a matrix ring over a field is maximal with non-field quotient). The statement now assumes R commutative with identity.'
---

::: {.exercise}
Let $R$ be a commutative ring with identity. Show that $I\normal R$ is maximal iff $R/I$ is a field.
:::

::: {.solution}
Let $I\subsetneq R$ be a proper ideal. By the correspondence theorem, ideals of $R/I$ are in inclusion-preserving bijection with ideals $J$ of $R$ satisfying
$$
I\subseteq J\subseteq R,
$$
via $J\mapsto J/I$.

If $I$ is maximal, the only such ideals are $I$ and $R$. Hence the only ideals of $R/I$ are $0$ and $R/I$. A nonzero commutative ring with identity having no nontrivial ideals is a field, so $R/I$ is a field.

Conversely, if $R/I$ is a field, its only ideals are $0$ and $R/I$. By correspondence, the only ideals of $R$ containing $I$ are $I$ and $R$. Thus $I$ is maximal.

Therefore
$$
\boxed{I\text{ maximal}\iff R/I\text{ is a field}.}
$$
:::
