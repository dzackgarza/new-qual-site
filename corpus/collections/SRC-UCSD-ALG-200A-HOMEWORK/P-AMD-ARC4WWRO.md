---
schema: qual/card@1
id: P-AMD-ARC4WWRO
kind: problem
title: 'Given: $K = \langle k \rangle \normal G$'
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cyclic Groups
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Given: $K = \langle k \rangle \normal G$

Show: $H \leq K \implies H \normal G$
:::

::: {.solution}
<1>1. $K = \langle k \rangle$ is cyclic, so every subgroup of $K$ is characteristic in $K$.
Proof: a cyclic group has a unique subgroup of each order dividing $|K|$, so any subgroup is determined by its order and is preserved by every automorphism of $K$.

<1>2. $H$ is characteristic in $K$.
Proof: $H \le K$ and <1>1.

<1>3. $K$ is normal in $G$.
Proof: hypothesis.

<1>4. A characteristic subgroup of a normal subgroup is normal.
Proof: for $g \in G$, conjugation by $g$ restricts to an automorphism of $K$ (since $K \trianglelefteq G$); since $H$ is characteristic in $K$, this automorphism preserves $H$, so $gHg^{-1} = H$.

<1>5. Hence $H \trianglelefteq G$.
Proof: <1>2, <1>3, and <1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
