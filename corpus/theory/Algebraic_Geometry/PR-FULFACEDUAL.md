---
schema: qual/card@1
id: PR-FULFACEDUAL
kind: proposition
title: Faces of a cone and faces of its dual correspond contravariantly
slogan: 'Duality reverses the face lattice: a $d$-face of an $n$-cone corresponds to an $(n-d)$-face of the dual.'
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
\tau \longmapsto \tau^\star \definedas \dualof{\sigma} \intersect \tau^\perp
\]
is an inclusion-reversing bijection from the faces of $\sigma$ to the faces of $\dualof{\sigma}$, with inverse of the same shape, and
\[
\dim \tau + \dim \tau^\star = n .
\]
:::

::: {.remark title="The two ends, and what they pin down"}
The bijection sends $\sigma$ itself to $\theset{0}$ and $\theset{0}$ to $\dualof{\sigma}$, and in between it exchanges the two extremes of the face lattice:

| face of $\sigma$ | image in $\dualof{\sigma}$ |
| --- | --- |
| facet $\tau$, $\dim = n-1$ | ray spanned by the facet normal $u_\tau$ |
| ray $\rho$, $\dim = 1$ | facet of $\dualof{\sigma}$, $\dim = n-1$ |

So the rays of $\dualof{\sigma}$ are the facet normals of $\sigma$ and vice versa, which is exactly what makes the plane computation work: in $N_\RR = \RR^2$ facets and rays coincide, so dualising a two-dimensional cone is rotating its two generators a quarter turn.

Strong convexity is visible here too.
$\sigma$ contains no line exactly when $\theset{0}$ is a face of $\sigma$, which under the bijection says $\dualof{\sigma}$ is full-dimensional, that is $\dim \dualof{\sigma} = n$.
That is the condition needed for $S_\sigma$ to generate $M$ and for $U_\sigma$ to have the right dimension.
:::
