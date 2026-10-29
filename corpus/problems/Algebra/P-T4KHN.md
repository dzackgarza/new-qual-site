---
schema: qual/card@1
id: P-T4KHN
kind: problem
title: The nilradical is $\sqrt{(0)}$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Show that the nilradical is $\sqrt{(0)}$." and names no ring; the statement declares a commutative ring $R$.'
---

::: {.problem}
Let $R$ be a commutative ring. Show that the nilradical of $R$ is $\sqrt{(0)}$.
:::

::: {.solution}

::: pf

::: pf-step
The nilradical of $R$ equals $\sqrt{(0)}$.

::: pf-proof
By definition, $\sqrt{(0)}=\{x\in R : x^n=0 \text{ for some } n\ge 1\}$, which is the set of nilpotent elements of $R$, that is, the nilradical.
:::

:::

:::

:::
