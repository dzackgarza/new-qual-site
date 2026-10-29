---
schema: qual/card@1
id: P-6FFAX
kind: problem
title: Groups of order $45$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that all groups of order 45 are abelian.
:::

::: {.solution}
Let $\abs G=45=3^2\cdot5$.

::: pf

::: {.pf-step #sylow-normal}
$G$ has a unique Sylow $3$-subgroup $P$, of order $9$, and a unique Sylow $5$-subgroup $Q$, of order $5$; both are normal.

::: pf-proof
Sylow's theorems give $n_5\mid9$ and $n_5\equiv1\pmod5$, so $n_5=1$, and $n_3\mid5$ and $n_3\equiv1\pmod3$, so $n_3=1$. A unique Sylow subgroup is normal.
:::

:::

::: {.pf-step #direct-product}
$G\cong P\times Q$.

::: pf-proof
The orders of $P$ and $Q$ are coprime, so $P\cap Q=1$ and $\abs{PQ}=\abs P\abs Q=45$, hence $G=PQ$. Both are normal by step [](#sylow-normal){.pf-ref}, so $[P,Q]\subseteq P\cap Q=1$, and the elements of $P$ and $Q$ commute.
:::

:::

::: pf-step
$G$ is abelian, and $G\cong C_{45}$ or $G\cong C_3\times C_{15}$.

::: pf-proof
Every group of order $p^2$ is abelian, so $P\cong C_9$ or $P\cong C_3\times C_3$, and $Q\cong C_5$. By step [](#direct-product){.pf-ref}, $G\cong C_9\times C_5\cong C_{45}$ or $G\cong C_3\times C_3\times C_5\cong C_3\times C_{15}$.
:::

:::

:::

:::
