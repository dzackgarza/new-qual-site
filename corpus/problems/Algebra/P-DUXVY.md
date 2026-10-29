---
schema: qual/card@1
id: P-DUXVY
kind: problem
title: Degree of a field extension
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
What is the degree of a field extension?
What does it mean to be a finite extension?
:::

::: {.solution}
Let $F/K$ be a field extension.

::: pf

::: {.pf-step #vs}
$F$ is a vector space over $K$.

::: pf-proof
Addition in $F$ and multiplication by elements of $K$ satisfy the vector space axioms, because $F$ is a field containing $K$.
:::

:::

::: pf-step
The \dfn{degree} of $F$ over $K$ is $\boxed{[F:K]\coloneqq\dim_KF}$, the dimension of the vector space of step [](#vs){.pf-ref}, and $F/K$ is a \dfn{finite extension} if $[F:K]<\infty$.

::: pf-proof
For example, $[\CC:\RR]=2$, since $1,i$ is a basis of $\CC$ over $\RR$.
:::

:::

:::

:::
