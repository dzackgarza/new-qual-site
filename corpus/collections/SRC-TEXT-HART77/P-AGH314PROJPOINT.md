---
schema: qual/card@1
id: P-AGH314PROJPOINT
kind: problem
title: Projection from a point, and the cuspidal cubic image of the twisted cubic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Twisted Cubic
  - Cuspidal Cubic
relations:
- kind: uses
  target: P-AGH212DUPLE
review: draft
---

::: problem
Let $\PP^n$ be a hyperplane in $\PP^{n+1}$ and let $P \in \PP^{n+1} \sm \PP^n$.
Define $\phi: \PP^{n+1} \sm \ts{P} \to \PP^n$ by letting $\phi(Q)$ be the intersection with $\PP^n$ of the unique line through $P$ and $Q$.

1. Show that $\phi$ is a morphism.
2. Let $Y \subseteq \PP^3$ be the twisted cubic curve, the image of the $3$-uple embedding of $\PP^1$.
   If $t, u$ are the homogeneous coordinates on $\PP^1$, then $Y$ is given parametrically by
   $(x,y,z,w) = (t^3, t^2 u, t u^2, u^3)$.
   Let $P = \tv{0 : 0 : 1 : 0}$ and let $\PP^2$ be the hyperplane $z = 0$.
   Show that the projection of $Y$ from $P$ is a cuspidal cubic curve in the plane, and find its equation.
:::
