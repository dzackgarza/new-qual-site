---
schema: qual/card@1
id: P-5SNWD
kind: problem
title: $H\operatorname{char} K\operatorname{char} G$ implies $H\operatorname{char}
  G$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Subgroups
  - Normal Subgroups
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
Let $G$ be a group, and let $H \le K \le G$ be subgroups.
Prove that if $H$ is a characteristic subgroup of $K$ ($H \operatorname{char} K$) and $K$ is a characteristic subgroup of $G$ ($K \operatorname{char} G$), then $H$ is a characteristic subgroup of $G$ ($H \operatorname{char} G$).
:::

::: {.solution}
Let $\varphi\in\Aut(G)$.

::: pf

::: {.pf-step #restriction}
The restriction $\varphi\restrict_K$ is an automorphism of $K$.

::: pf-proof
Since $K\operatorname{char}G$, both $\varphi$ and $\varphi^{-1}$ map $K$ onto $K$, so $\varphi\restrict_K\colon K\to K$ is a bijective homomorphism.
:::

:::

::: pf-step
$\varphi(H)=H$, so $H\operatorname{char}G$.

::: pf-proof
Since $H\operatorname{char}K$ and $\varphi\restrict_K\in\Aut(K)$ by step [](#restriction){.pf-ref}, $\varphi(H)=(\varphi\restrict_K)(H)=H$. This holds for every $\varphi\in\Aut(G)$.
:::

:::

:::

:::
