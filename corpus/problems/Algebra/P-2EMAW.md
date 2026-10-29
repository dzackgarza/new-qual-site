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
  - event: statement-corrected
    by: Claude Opus 5.5
    date: "2026-10-29"
    note: Source prints "a $p$-group"; added "finite", since the normalizer condition and the claim fail for some infinite $p$-groups.
---

::: {.problem}
Show that every maximal subgroup of a finite $p$-group is normal.
:::

::: {.solution}
Let $G$ be a finite $p$-group and let $M<G$ be maximal.

::: pf

::: pf-step

One has $M<N_G(M)$.

::: pf-proof

By the normalizer condition for finite $p$-groups, every proper subgroup is properly contained in its normalizer. Since $M<G$,
$$
M<N_G(M).
$$

:::

:::

::: pf-step

Hence $N_G(M)=G$.

::: pf-proof

We have
$$
M<N_G(M)\le G.
$$
Because $M$ is maximal, there is no subgroup strictly between $M$ and $G$. Therefore $N_G(M)=G$.

:::

:::

::: pf-step

Therefore $M\trianglelefteq G$.

::: pf-proof

The equality $N_G(M)=G$ says precisely that every element of $G$ normalizes $M$. Hence $M$ is normal.

:::

:::

:::

:::
