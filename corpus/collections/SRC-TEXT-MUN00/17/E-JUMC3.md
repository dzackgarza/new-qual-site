---
schema: qual/card@1
id: E-JUMC3
kind: problem
title: Differences of open and closed sets
classification:
  areas:
  - topology
  topics:
  - Closed Sets
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Show that if $U$ is open in $X$ and $A$ is closed in $X$, then $U - A$ is open in $X$, and $A - U$ is closed in $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #u-minus-a-open}
$U-A$ is open in $X$.

::: pf-proof
$U-A=U\cap(X-A)$, and $X-A$ is open because $A$ is closed; a finite intersection of open sets is open.
:::

:::

::: {.pf-step #a-minus-u-closed}
$A-U$ is closed in $X$.

::: pf-proof
$A-U=A\cap(X-U)$, and $X-U$ is closed because $U$ is open; an intersection of closed sets is closed.
:::

:::

::: pf-qed
Steps [](#u-minus-a-open){.pf-ref} and [](#a-minus-u-closed){.pf-ref}.
:::

:::

:::
