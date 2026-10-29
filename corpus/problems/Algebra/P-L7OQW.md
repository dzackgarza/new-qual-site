---
schema: qual/card@1
id: P-L7OQW
kind: problem
title: Normality of subgroups is not transitive
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Counterexamples
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Give an example of subgroups
$$
H\trianglelefteq K\trianglelefteq G
$$
with $H$ not normal in $G$.
:::

::: {.solution}
Take $G=A_4$, $K=V_4=\{e,(12)(34),(13)(24),(14)(23)\}$, and $H=\langle(12)(34)\rangle$.

::: pf

::: pf-step
$K\trianglelefteq G$.

::: pf-proof
$K$ consists of the identity and all three double transpositions in $A_4$, and conjugation preserves cycle type.
:::

:::

::: pf-step
$H\trianglelefteq K$.

::: pf-proof
$K\cong C_2\times C_2$ is abelian, so every subgroup of $K$ is normal in $K$.
:::

:::

::: pf-step
$H$ is not normal in $G$.

::: pf-proof
$(123)(12)(34)(123)^{-1}=(14)(23)\notin H$.
:::

:::

:::

:::
