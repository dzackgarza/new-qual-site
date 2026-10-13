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
Let $N_\RR$ be a finite-dimensional real vector space, let $M_\RR=N_\RR^\vee$, let $\sigma\subseteq N_\RR$ be a convex polyhedral cone, and let $v\in N_\RR\sm\sigma$.
Then there is a linear functional $u\in\sigma\dual\subseteq M_\RR$ such that
$$
\inner{u}{v} < 0 .
$$
Equivalently, the hyperplane $u^\perp$ places $\sigma$ in the closed half-space $\inner{u}{\wait}\geq0$ and $v$ in the opposite open half-space.
:::

::: {.proof}
Choose an inner product on $N_\RR$ and let $p\in\sigma$ be the point minimizing the distance to $v$; it exists because a polyhedral cone is closed and convex. The characterization of the metric projection gives
$$
\langle v-p,x-p\rangle\leq0
\qquad\text{for every }x\in\sigma.
$$
Taking $x=0$ and $x=2p$ shows $\langle v-p,p\rangle=0$. Hence
$$
\langle p-v,x\rangle\geq0
\qquad\text{for every }x\in\sigma,
$$
while
$$
\langle p-v,v\rangle=-\norm{v-p}^2<0.
$$
The functional $u=\langle p-v,\wait\rangle\in M_\RR$ therefore has the required properties.
:::

::: {.proposition title="Double duality"}
$$
(\sigma\dual)\dual = \sigma .
$$
:::

::: {.proof}
The inclusion $\sigma \subseteq \dualof{(\dualof{\sigma})}$ is the definition: every $v \in \sigma$ pairs non-negatively with every $u \in \dualof{\sigma}$.

For the reverse, take $v \notin \sigma$ and apply separation to get $u \in \dualof{\sigma}$ with $\inner{u}{v} < 0$.
That $u$ witnesses $v \notin \dualof{(\dualof{\sigma})}$.
:::

::: {.remark}
The proof uses only finite dimensionality, convexity, and closedness; polyhedrality guarantees closedness. The equality $(\sigma^\vee)^\vee=\sigma$ therefore holds more generally for every closed convex cone in a finite-dimensional real vector space.
:::
