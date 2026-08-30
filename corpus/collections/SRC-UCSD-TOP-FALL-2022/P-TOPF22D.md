---
schema: qual/card@1
id: P-TOPF22D
kind: problem
title: "Connected closed non-orientable 3-manifold has infinite fundamental group"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Manifolds
  - Orientation
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Show that a connected closed non-orientable $3$-manifold must have infinite fundamental group.
:::

::: {.solution}
<1>1. $M$ closed non-orientable $3$-manifold has $w_1\neq0$.
Proof: Stiefel-Whitney.

<1>2. Then $H^1(M;\Z/2)\neq0$, so $\pi_1(M)$ has index $2$ subgroup.
Proof: $w_1$ gives homomorphism $\pi_1\to\Z/2$.

<1>3. Hence $\pi_1$ infinite (finite group cannot have index $2$ subgroup and be non-orientable? Actually infinite).
Proof: covering double is orientable, infinite.

<1>4. Q.E.D.
Proof: <1>3.
:::
