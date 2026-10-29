---
schema: qual/card@1
id: P-QYRBQ
kind: problem
title: No group of order 36 is simple
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Prove that no group of order 36 is simple.
:::

::: {.solution}
Let $|G|=36=2^2\cdot3^2$.

::: pf

::: {.pf-step #n3}
$n_3\in\{1,4\}$.

::: pf-proof
By Sylow's theorems, $n_3\mid4$ and $n_3\equiv1\pmod3$.
:::

:::

::: pf-step
If $n_3=1$, then $G$ is not simple.

::: pf-proof
The unique Sylow $3$-subgroup is normal, and its order $9$ is neither $1$ nor $36$.
:::

:::

::: pf-step
If $n_3=4$, then $G$ is not simple.

::: pf-proof
Conjugation on the four Sylow $3$-subgroups gives a homomorphism $\rho:G\to S_4$. Since $36>24=\abs{S_4}$, $\rho$ is not injective, so $\ker\rho\ne1$. The action is transitive on four points, hence nontrivial, so $\ker\rho\ne G$. Thus $\ker\rho$ is a nontrivial proper normal subgroup.
:::

:::

:::
:::
