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
<1>1. $U-A$ is open in $X$.

::: {.proof}
$U-A=U\cap(X-A)$, and $X-A$ is open because $A$ is closed; a finite intersection of open sets is open.
:::

<1>2. $A-U$ is closed in $X$.

::: {.proof}
$A-U=A\cap(X-U)$, and $X-U$ is closed because $U$ is open; an intersection of closed sets is closed.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2.
:::
:::
