---
schema: qual/card@1
id: P-BOSWW
kind: problem
title: $A_n$ is normal in $S_n$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
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
Prove that $A_n$ is normal in $S_n$.
:::

::: {.solution}

::: pf

::: pf-step

$A_n$ is the kernel of the sign homomorphism $\sgn:S_n\to\{\pm1\}$.

::: pf-proof

$A_n$ is by definition the set of even permutations, those with $\sgn\sigma=1$.

:::

:::

::: pf-step

$A_n\trianglelefteq S_n$.

::: pf-proof

The kernel of a group homomorphism is normal: if $\sgn\sigma=1$, then $\sgn(\tau\sigma\tau^{-1})=\sgn\tau\,\sgn\sigma\,\sgn\tau^{-1}=1$.

:::

:::

:::

:::
