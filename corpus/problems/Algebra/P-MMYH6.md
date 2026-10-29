---
schema: qual/card@1
id: P-MMYH6
kind: problem
title: $S_3$ is not nilpotent
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Permutations
  - Counterexamples
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
Show that $S_3$ is not nilpotent.
:::

::: {.solution}
::: pf

::: {.pf-step #sylow}
$S_3$ has three Sylow $2$-subgroups, so none of them is normal.

::: pf-proof
The Sylow $2$-subgroups have order $2$ and are $\langle(12)\rangle$, $\langle(13)\rangle$, $\langle(23)\rangle$.
A normal Sylow subgroup is the unique Sylow subgroup for its prime.
:::

:::

::: pf-step
$S_3$ is not nilpotent.

::: pf-proof
Every Sylow subgroup of a finite nilpotent group is normal, which fails by step [](#sylow){.pf-ref}.
:::

:::

:::

:::

::: {.remark}
The lower central series gives a second proof: $[S_3,S_3]=A_3$ and $[A_3,S_3]=A_3$, so the series stabilizes at $A_3\ne1$.
:::
