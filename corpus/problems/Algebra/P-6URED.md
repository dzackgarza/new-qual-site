---
schema: qual/card@1
id: P-6URED
kind: problem
title: $S_4$ is solvable and nonabelian
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Permutations
  - Subgroup Series
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
Prove that the symmetric group $S_4$ is a **non-abelian** and **solvable** group.
:::

::: {.solution}
Let $V_4=\{e,(12)(34),(13)(24),(14)(23)\}$.

::: pf

::: pf-step
$S_4$ is nonabelian.

::: pf-proof
$(12)(23)=(123)\ne(132)=(23)(12)$.
:::

:::

::: {.pf-step #series}
$1\triangleleft V_4\triangleleft A_4\triangleleft S_4$ is a normal series.

::: pf-proof
$A_4$ is the kernel of the sign map. $V_4$ is a subgroup consisting of the identity and the whole conjugacy class of double transpositions, so it is normal in $S_4$, hence in $A_4$.
:::

:::

::: pf-step
$S_4$ is solvable.

::: pf-proof
The factors of the series of step [](#series){.pf-ref} are $V_4\cong C_2\times C_2$, $A_4/V_4\cong C_3$ (order $3$) and $S_4/A_4\cong C_2$, and all are abelian.
:::

:::

:::

:::
