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
<1>1. Proof that $U \setminus A$ is open in $X$:
<2>1. By definition of set difference:
\[
U \setminus A = U \cap (X \setminus A).
\]
<2>2. Since $A$ is closed in $X$, its complement $X \setminus A$ is open in $X$.
<2>3. Because both $U$ and $X \setminus A$ are open in $X$, their finite intersection $U \cap (X \setminus A)$ is open in $X$.
Therefore $U \setminus A$ is open in $X$.

<1>2. Proof that $A \setminus U$ is closed in $X$:
<2>1. By definition of set difference:
\[
A \setminus U = A \cap (X \setminus U).
\]
<2>2. Since $U$ is open in $X$, its complement $X \setminus U$ is closed in $X$.
<2>3. Because both $A$ and $X \setminus U$ are closed in $X$, their intersection $A \cap (X \setminus U)$ is closed in $X$.
Therefore $A \setminus U$ is closed in $X$.

<1>3. Conclusion:
$U \setminus A$ is open and $A \setminus U$ is closed in $X$. Q.E.D.
:::
