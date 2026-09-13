---
schema: qual/card@1
id: PR-FULSEP
kind: proposition
title: Separation for convex polyhedral cones, and the double dual
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cones
  - Convex Geometry
relations:
- kind: uses
  target: D-Q7Q2N
review: draft
prompts:
- State the separation property of a convex polyhedral cone and deduce that the double dual is the cone itself.
- Why does dualising a cone twice return the original cone?
---

::: {.proposition title="Separation"}
Let $\sigma \subseteq N_\RR$ be a convex polyhedral cone and let $v \in N_\RR$ with $v \notin \sigma$.
Then there is a **support vector** $u \in \sigma\dual$ with
\[
\inp{u}{v} < 0 .
\]
That is, $v$ lies strictly on the negative side of a hyperplane that has all of $\sigma$ on its non-negative side.
:::

::: {.proposition title="Double duality"}
\[
(\sigma\dual)\dual = \sigma .
\]
:::

::: {.proof}
The inclusion $\sigma \subseteq (\sigma\dual)\dual$ is the definition: every $v \in \sigma$ pairs non-negatively with every $u \in \sigma\dual$.

For the reverse, take $v \notin \sigma$ and apply separation to get $u \in \sigma\dual$ with $\inp{u}{v} < 0$.
That $u$ witnesses $v \notin (\sigma\dual)\dual$.
:::

::: {.remark title="What separation rests on"}
Separation is the finite-dimensional Hahn--Banach statement, and for a polyhedral cone it is elementary: $\sigma$ is closed and convex, so the point of $\sigma$ nearest to $v$ exists, and the vector from it to $v$ gives the required $u$ after a sign change.
Convexity and closedness are both needed, and polyhedral cones have both for free.

Double duality is the reason the dictionary is a dictionary and not a one-way map.
Every statement about $\sigma$ has a mirror statement about $\sigma\dual$, and no information is lost in passing between them: $\sigma$ lives in $N_\RR$ where the fan and the geometry are, $\sigma\dual$ lives in $M_\RR$ where the semigroup and the ring are, and the two determine each other.
:::
