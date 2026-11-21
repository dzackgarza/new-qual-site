---
schema: qual/card@1
id: FE-207WC
kind: example
title: The two small resolutions of the cone over the quadric surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Resolutions
  - Birational Geometry
relations:
- kind: related-to
  target: T-TORDIV
- kind: related-to
  target: D-SRFADE
review: draft
prompts:
- Resolve the cone over the quadric surface by a small resolution.
- Why are the two small resolutions of the cone over the quadric surface not isomorphic over the cone?
---

::: {.example title="The resolutions"}
Let $C=\Spec k[w,x,y,z]/(wz-xy)\subseteq\AA^4_k$ be the affine cone over the quadric surface $\PP^1\times\PP^1\subseteq\PP^3$.
Resolving the rational map $C\dashrightarrow\PP^1$ that sends a point of $C\sm\theset{0}$ to $[w:x]$ gives a variety $X$ with a proper birational morphism $\pi\colon X\to C$ that is an isomorphism away from the vertex, with $\pi^{-1}(0)\cong\PP^1$.
The fibre over the vertex has codimension two in $X$, so $\pi$ is a small resolution and differs from the resolution obtained by blowing up the vertex [@Vak25, Exercise 22.4.N].
Resolving instead the map that sends the point to $[w:y]$ gives a second small resolution $\pi'\colon X'\to C$, an isomorphism away from the vertex with $\PP^1$ over it, and there is no morphism $X\to X'$ commuting with $\pi$ and $\pi'$; the birational map $X\dashrightarrow X'$ is the Atiyah flop [@Vak25, Remark 22.4.11].
:::
