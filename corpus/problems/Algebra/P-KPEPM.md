---
schema: qual/card@1
id: P-KPEPM
kind: problem
title: Pairs $(n,p)$ for which $\SL_n(\FF_p)$ is solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Matrix Groups
  - Finite Fields
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
Let $p$ be prime and $n\ge1$. Determine all pairs $(n,p)$ for which
$$
\SL_n(\FF_p)
$$
is solvable.
:::

::: {.solution}

::: pf

::: {.pf-step #n-one}
If $n=1$, then $\SL_1(\FF_p)$ is solvable.

::: pf-proof
$\SL_1(\FF_p)=1$.
:::

:::

::: {.pf-step #small}
$\SL_2(\FF_2)$ and $\SL_2(\FF_3)$ are solvable.

::: pf-proof
$\SL_2(\FF_2)\cong S_3$, which is solvable. The center of $\SL_2(\FF_3)$ is $\{\pm I\}\cong C_2$ and $\PSL_2(\FF_3)\cong A_4$, so $\SL_2(\FF_3)$ is an extension of the solvable group $A_4$ by the abelian group $C_2$, hence solvable.
:::

:::

::: {.pf-step #rest}
For every other pair with $n\ge2$, $\SL_n(\FF_p)$ is not solvable.

::: pf-proof
By the simplicity theorem for projective special linear groups, $\PSL_n(\FF_p)$ is nonabelian simple for $n\ge2$ except for $(n,p)=(2,2),(2,3)$. A nonabelian simple group is not solvable, and $\PSL_n(\FF_p)$ is a quotient of $\SL_n(\FF_p)$, so $\SL_n(\FF_p)$ is not solvable.
:::

:::

::: pf-step
$\SL_n(\FF_p)$ is solvable exactly for $\boxed{n=1 \text{ and every prime } p,\ \text{or } (n,p)=(2,2),(2,3)}$.

::: pf-proof
Steps [](#n-one){.pf-ref}, [](#small){.pf-ref} and [](#rest){.pf-ref} cover every pair.
:::

:::

:::

:::
