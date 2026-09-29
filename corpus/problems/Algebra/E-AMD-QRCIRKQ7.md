---
schema: qual/card@1
id: E-AMD-QRCIRKQ7
kind: problem
title: Prime ideals are irreducible
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
  - Primary Decomposition
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that every prime ideal is irreducible.
:::

::: {.hint}
If $\mfp = J\cap K$ with $a\in J\sm\mfp$ and $b\in K\sm\mfp$, then $ab\in J\cap K=\mfp$.
:::

::: {.solution}

::: pf

::: pf-step
Recall that $I$ is *irreducible* when $I = J \cap K$ for ideals $J, K$ forces $I = J$ or $I = K$.
:::

::: pf-step
Let $\mfp$ be prime and suppose $\mfp = J \cap K$ with $\mfp \neq J$ and $\mfp \neq K$.
:::

::: {.pf-step #exists-a-and-b-outside-p}
There are $a \in J \sm \mfp$ and $b \in K \sm \mfp$.

::: pf-proof
$\mfp = J \cap K \subseteq J$, so $\mfp \neq J$ gives an $a \in J$ outside $\mfp$, and likewise for $K$.
:::

:::

::: pf-step
$ab \in \mfp$.

::: pf-proof

::: pf-step
$ab \in J$, because $a \in J$ and $J$ is an ideal.
:::

::: pf-step
$ab \in K$, because $b \in K$ and $K$ is an ideal.
:::

::: pf-step
So $ab \in J \cap K = \mfp$.
:::

:::

:::

::: pf-qed
$\mfp$ is prime and $ab \in \mfp$, so $a \in \mfp$ or $b \in \mfp$, contradicting step [](#exists-a-and-b-outside-p){.pf-ref}. Hence $\mfp = J$ or $\mfp = K$, and $\mfp$ is irreducible.
:::

:::

:::
