---
schema: qual/card@1
id: E-NO7PH
kind: exercise
title: Is the lower limit line a Baire space
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Determine whether or not $\mathbb{R}_\ell$ is a Baire space.
:::

::: {.solution}
<1>1. $\mathbb{R}_\ell$ (the Sorgenfrey line, with basis $[a,b)$) is not a Baire space.
Proof: claim.

<1>2. $\mathbb{Q}$ is countable, and each $\{q\}$ is closed in $\mathbb{R}_\ell$ (since $\mathbb{R}_\ell$ is $T_1$).
Proof: singletons are closed.

<1>3. Each $\{q\}$ has empty interior in $\mathbb{R}_\ell$ (it is nowhere dense).
Proof: any basic open $[a,b)$ containing $q$ contains points $\neq q$.

<1>4. $\mathbb{Q} = \bigcup_{q \in \mathbb{Q}} \{q\}$ is a countable union of nowhere dense closed sets.
Proof: <1>2 and <1>3.

<1>5. But $\mathbb{Q}$ is not closed and $\mathbb{R}_\ell \setminus \mathbb{Q}$ is not open dense; more precisely, $\mathbb{R}_\ell$ is the countable union of the closed nowhere dense sets $\{q\}$, so it is of first category in itself.
Proof: <1>4.

<1>6. A Baire space cannot be a countable union of nowhere dense closed sets.
Proof: Baire category theorem.

<1>7. Hence $\mathbb{R}_\ell$ is not Baire.
Proof: <1>5 and <1>6.

<1>8. Q.E.D.
Proof: <1>7.
:::
