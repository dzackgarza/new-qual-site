---
schema: qual/card@1
id: P-N5QRJ
kind: problem
title: Every nonzero ring has a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source reads "Show that every nonzero ring has a maximal ideal."; without an identity the claim fails (the rational numbers with zero multiplication have no maximal ideal), so the statement assumes a commutative ring with identity.
---

::: {.problem}
Show that every nonzero commutative ring with identity has a maximal ideal.
:::

::: {.solution}
::: pf

::: pf-step
A nonzero commutative ring $R$ with identity has a maximal ideal.

::: pf-proof
Since $1\ne0$ in $R$, the ideal $(0)$ is proper, and by [[P-USAQT]] every proper ideal is contained in a maximal ideal.
:::

:::

:::

:::
