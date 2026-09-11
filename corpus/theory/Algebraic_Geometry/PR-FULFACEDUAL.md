---
schema: qual/card@1
id: PR-FULFACEDUAL
kind: proposition
title: Faces of a cone and faces of its dual correspond contravariantly
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cones
  - Convex Geometry
relations:
- kind: uses
  target: PR-FULFACET
- kind: uses
  target: PR-FULSEP
review: draft
prompts:
- Describe the bijection between the faces of a cone and the faces of its dual.
- How do dimensions behave under that bijection?
---

::: {.proposition}
Let $\sigma \subseteq N_\RR$ be a full-dimensional convex polyhedral cone, $\dim N_\RR = n$.
The assignment
\[
\tau \longmapsto \tau^\star \da \sigma\dual \intersect \tau^\perp
\]
is an inclusion-reversing bijection from the faces of $\sigma$ to the faces of $\sigma\dual$, with inverse of the same shape, and
\[
\dim \tau + \dim \tau^\star = n .
\]
:::

::: {.remark title="The two ends, and what they pin down"}
The bijection sends $\sigma$ itself to $\ts{0}$ and $\ts{0}$ to $\sigma\dual$, and in between it exchanges the two extremes of the face lattice:

| face of $\sigma$ | image in $\sigma\dual$ |
| --- | --- |
| facet $\tau$, $\dim = n-1$ | ray spanned by the facet normal $u_\tau$ |
| ray $\rho$, $\dim = 1$ | facet of $\sigma\dual$, $\dim = n-1$ |

So the rays of $\sigma\dual$ are the facet normals of $\sigma$ and vice versa, which is exactly what makes the plane computation work: in $N_\RR = \RR^2$ facets and rays coincide, so dualising a two-dimensional cone is rotating its two generators a quarter turn.

Strong convexity is visible here too.
$\sigma$ contains no line exactly when $\ts{0}$ is a face of $\sigma$, which under the bijection says $\sigma\dual$ is full-dimensional, that is $\dim \sigma\dual = n$.
That is the condition needed for $S_\sigma$ to generate $M$ and for $U_\sigma$ to have the right dimension.
:::
