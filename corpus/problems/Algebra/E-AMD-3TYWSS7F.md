---
schema: qual/card@1
id: E-AMD-3TYWSS7F
kind: problem
title: Nilpotent groups are solvable
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Solvable Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that $G$ nilpotent $\implies G$ solvable.
:::

::: {.solution}
Let $G$ be nilpotent.

::: pf

::: {.pf-step #central-series}
$G$ has a finite central series $1=Z_0\trianglelefteq Z_1\trianglelefteq\cdots\trianglelefteq Z_c=G$ with $Z_i\trianglelefteq G$ and $Z_{i+1}/Z_i\le Z(G/Z_i)$ for every $i$.

::: pf-proof
This is the definition of a nilpotent group; the upper central series is such a series.
:::

:::

::: pf-step
$G$ is solvable.

::: pf-proof
Each $Z_{i+1}/Z_i$ in step [](#central-series){.pf-ref} lies in the abelian group $Z(G/Z_i)$, so it is abelian. Hence the series is a finite subnormal series with abelian factors.
:::

:::

:::

:::
