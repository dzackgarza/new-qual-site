---
schema: qual/card@1
id: P-2EMAW
kind: problem
title: Maximal subgroups of $p$-groups are normal
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Subgroups
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

::: problem
- Show that every maximal subgroup of a $p$-group is normal.
:::


::: {.solution}
Let $G$ be a finite $p$-group and let $M<G$ be maximal.

<1>1. One has $M<N_G(M)$.
::: {.proof}
By the normalizer condition for finite $p$-groups, every proper subgroup is properly contained in its normalizer. Since $M<G$,
\[
M<N_G(M).
\]
:::

<1>2. Hence $N_G(M)=G$.
::: {.proof}
We have
\[
M<N_G(M)\le G.
\]
Because $M$ is maximal, there is no subgroup strictly between $M$ and $G$. Therefore $N_G(M)=G$.
:::

<1>3. Therefore $M\trianglelefteq G$.
::: {.proof}
The equality $N_G(M)=G$ says precisely that every element of $G$ normalizes $M$. Hence $M$ is normal.
:::
:::
