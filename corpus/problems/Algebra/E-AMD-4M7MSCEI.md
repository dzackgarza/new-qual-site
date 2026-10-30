---
schema: qual/card@1
id: E-AMD-4M7MSCEI
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
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that $H \operatorname{char} K \operatorname{char} G \implies H \operatorname{char} G$.

> So "characteristic" is a transitive relation for subgroups.
:::

::: {.solution}
Let $\phi\in\Aut(G)$.

::: pf

::: {.pf-step #restriction}
The restriction $\phi\restrict_K$ is an automorphism of $K$.

::: pf-proof
Since $K\operatorname{char}G$, both $\phi$ and $\phi^{-1}$ map $K$ onto $K$, so $\phi\restrict_K\colon K\to K$ is a bijective homomorphism.
:::

:::

::: pf-step
$\phi(H)=H$, so $H\operatorname{char}G$.

::: pf-proof
Since $H\operatorname{char}K$ and $\phi\restrict_K\in\Aut(K)$ by step [](#restriction){.pf-ref}, $\phi(H)=(\phi\restrict_K)(H)=H$. This holds for every $\phi\in\Aut(G)$.
:::

:::

:::

:::
