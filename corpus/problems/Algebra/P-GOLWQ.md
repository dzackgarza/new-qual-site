---
schema: qual/card@1
id: P-GOLWQ
kind: problem
title: A field homomorphism is zero or injective
classification:
  areas:
  - algebra
  topics:
  - Fields
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

Show that any field morphism is either 0 or injective.

:::

::: {.solution}

Let $\phi:F\to R$ be a ring homomorphism with $F$ a field.

::: pf

::: {.pf-step #kernel}

Either $\ker\phi=(0)$ or $\ker\phi=F$.

::: pf-proof

The kernel is an ideal of $F$, and a field has only the ideals $(0)$ and $F$.

:::

:::

::: pf-step

$\phi$ is injective or $\phi=0$.

::: pf-proof

By step [](#kernel){.pf-ref}, either $\ker\phi=(0)$, so $\phi$ is injective, or $\ker\phi=F$, so $\phi(x)=0$ for every $x\in F$.

:::

:::

:::

:::

::: {.remark}

If ring homomorphisms are required to preserve $1$, the zero case occurs only when $R=0$.

:::
