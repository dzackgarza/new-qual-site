---
schema: qual/card@1
id: P-JX3FO
kind: problem
title: The kernel of a homomorphism is a normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Homomorphisms
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
Prove that the kernel of a homomorphism is a normal subgroup.
:::

::: {.solution}
Let $\phi:G\to H$ be a group homomorphism, with kernel $\ker\phi=\{g\in G:\phi(g)=1_H\}$.

::: pf

::: pf-step

$\ker\phi$ is a subgroup of $G$.

::: pf-proof

$\phi(1_G)=1_H$, so $1_G\in\ker\phi$. If $x,y\in\ker\phi$, then $\phi(xy^{-1})=\phi(x)\phi(y)^{-1}=1_H$.

:::

:::

::: pf-step

$\ker\phi\trianglelefteq G$.

::: pf-proof

For $g\in G$ and $k\in\ker\phi$, $\phi(gkg^{-1})=\phi(g)\phi(k)\phi(g)^{-1}=\phi(g)\phi(g)^{-1}=1_H$, so $gkg^{-1}\in\ker\phi$.

:::

:::

:::

:::
