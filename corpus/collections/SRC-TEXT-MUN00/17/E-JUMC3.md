---
schema: qual/card@1
id: E-JUMC3
kind: exercise
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
<1>1. $U-A = U\cap (X\setminus A)$ is open (intersection of two opens).
Proof: $X\setminus A$ open.

<1>2. $A-U = A\cap (X\setminus U)$ is closed (intersection of two closed).
Proof: $X\setminus U$ closed.

<1>3. Q.E.D.
Proof: <1>1 and <1>2.
:::
