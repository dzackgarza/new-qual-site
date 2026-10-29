---
schema: qual/card@1
id: E-NXHG6
kind: problem
title: Every non-unit of $R$ is contained in a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source did not assume R commutative; in M_2(k) the non-unit E_11 lies in no proper two-sided ideal, so the statement now assumes R commutative with identity.'
---

::: {.exercise}
Let $R$ be a commutative ring with identity. Show that every non-unit of $R$ is contained in a maximal ideal.
:::

::: {.solution}
Let $x\in R\sm \units{R}$.

::: pf

::: {.pf-step #quotient-nonzero}
$R/Rx\neq0$.

::: pf-proof
If $Rx=R$, then $1=rx$ for some $r\in R$, and $x$ is a unit since $R$ is commutative. Hence $Rx$ is a proper ideal.
:::

:::

::: pf-step
Some $\mfm\in\mspec R$ contains $x$.

::: pf-proof
By step [](#quotient-nonzero){.pf-ref} and Zorn's lemma, the nonzero ring $R/Rx$ has a maximal ideal $\bar\mfm$. By the correspondence theorem, its preimage $\mfm$ in $R$ is a maximal ideal containing $Rx$, hence containing $x$.
:::

:::

:::

:::
