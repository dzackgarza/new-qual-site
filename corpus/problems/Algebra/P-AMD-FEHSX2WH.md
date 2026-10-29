---
schema: qual/card@1
id: P-AMD-FEHSX2WH
kind: problem
title: The nilradical is contained in the Jacobson radical
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Nilpotence
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
The nilradical is contained in the Jacobson radical, i.e.
$$
\nilrad{R} \subseteq J(R).
$$
:::

::: {.solution}
Let $R$ be a commutative ring with identity.

::: pf

::: {.pf-step #nil-in-prime}

Every nilpotent element lies in every prime ideal.

::: pf-proof

If $x^n=0$ and $\mathfrak p$ is prime, then $x^n\in\mathfrak p$, and primality gives $x\in\mathfrak p$.

:::

:::

::: pf-step

$\nilrad{R}\subseteq J(R)$.

::: pf-proof

Every maximal ideal is prime, so by step [](#nil-in-prime){.pf-ref} every nilpotent element lies in every maximal ideal, that is, in
$$
\bigcap_{\mathfrak m\in\mspec R}\mathfrak m=J(R).
$$

:::

:::

:::

:::
