---
schema: qual/card@1
id: E-AMD-QRCIRKQ7
kind: exercise
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

::: solution
**Goal:** if a prime $\mfp$ were the intersection of two strictly larger ideals, a product of two elements outside $\mfp$ would land in $\mfp$.

<1>1. Recall that $I$ is *irreducible* when $I = J \cap K$ for ideals $J, K$ forces $I = J$ or $I = K$.

<1>2. Let $\mfp$ be prime and suppose $\mfp = J \cap K$ with $\mfp \neq J$ and $\mfp \neq K$.

<1>3. There are $a \in J \sm \mfp$ and $b \in K \sm \mfp$.
*Proof:* $\mfp = J \cap K \subseteq J$, so $\mfp \neq J$ gives an $a \in J$ outside $\mfp$, and likewise for $K$.

<1>4. $ab \in \mfp$.
::: {.proof}
<2>1. $ab \in J$, because $a \in J$ and $J$ is an ideal.
<2>2. $ab \in K$, because $b \in K$ and $K$ is an ideal.
<2>3. So $ab \in J \cap K = \mfp$.

:::
<1>5. Q.E.D. *Proof:* $\mfp$ is prime and $ab \in \mfp$, so $a \in \mfp$ or $b \in \mfp$, contradicting step <1>3. Hence $\mfp = J$ or $\mfp = K$, and $\mfp$ is irreducible.
:::
