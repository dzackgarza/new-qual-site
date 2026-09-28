---
schema: qual/card@1
id: PR-FULSEP
kind: proposition
title: Separation for convex polyhedral cones, and the double dual
slogan: 'A point outside a polyhedral cone is detected by a negative dual pairing; that separation is exactly why double duality returns the cone.'
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
Then there is a **support vector** $u \in \dualof{\sigma}$ with
\[
\inp{u}{v} < 0 .
\]
That is, $v$ lies strictly on the negative side of a hyperplane that has all of $\sigma$ on its non-negative side.
:::

::: {.proposition title="Double duality"}
\[
\dualof{(\dualof{\sigma})} = \sigma .
\]
:::

::: {.proof}
The inclusion $\sigma \subseteq \dualof{(\dualof{\sigma})}$ is the definition: every $v \in \sigma$ pairs non-negatively with every $u \in \dualof{\sigma}$.

For the reverse, take $v \notin \sigma$ and apply separation to get $u \in \dualof{\sigma}$ with $\inp{u}{v} < 0$.
That $u$ witnesses $v \notin \dualof{(\dualof{\sigma})}$.
:::

::: {.remark title="What separation rests on"}
Separation is the finite-dimensional Hahn--Banach statement, and for a polyhedral cone it is elementary: $\sigma$ is closed and convex, so the point of $\sigma$ nearest to $v$ exists, and the vector from it to $v$ gives the required $u$ after a sign change.
Convexity and closedness are both needed, and polyhedral cones have both for free.

Double duality makes the cone-dual correspondence reversible.
The equality $(\sigma^\vee)^\vee=\sigma$ means that $\sigma\subseteq N_\RR$ and $\sigma^\vee\subseteq M_\RR$ determine each other.
:::
