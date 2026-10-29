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
Let $N$ be a lattice of rank $n$, put $M\coloneqq\Hom(N,\ZZ)$, and let $\sigma\subseteq N_\RR$ be a full-dimensional strongly convex rational polyhedral cone.
The assignment
$$
\tau \longmapsto \tau^\star\coloneqq\dualof{\sigma}\intersect\tau^\perp
$$
is an inclusion-reversing bijection from the faces of $\sigma$ to the faces of $\dualof{\sigma}\subseteq M_\RR$. Its inverse sends a face $\gamma\leq\dualof{\sigma}$ to
$$
\gamma^\star\coloneqq\sigma\intersect\gamma^\perp.
$$
For every face $\tau\leq\sigma$,
$$
\dim \tau + \dim \tau^\star = n .
$$
:::

::: {.remark title="Rays and facets"}
The bijection sends $\sigma$ to $\theset{0}$ and $\theset{0}$ to $\dualof{\sigma}$. It exchanges rays and facets:

| face of $\sigma$ | image in $\dualof{\sigma}$ |
| --- | --- |
| facet $\tau$, $\dim = n-1$ | ray $\dualof{\sigma}\intersect\tau^\perp$ spanned by a primitive facet normal in $M$ |
| ray $\rho$, $\dim = 1$ | facet of $\dualof{\sigma}$, $\dim = n-1$ |

Thus the primitive ray generators of $\dualof{\sigma}$ are the primitive inward facet normals of $\sigma$, and conversely.

For an arbitrary polyhedral cone $C\subseteq N_\RR$, strong convexity is equivalent to $\theset{0}$ being a face of $C$, and by face duality this is equivalent to $\dualof{C}$ being full-dimensional. For the strongly convex $\sigma$ above, the semigroup $S_\sigma\coloneqq\dualof{\sigma}\intersect M$ therefore generates $M$ as a group.
:::
