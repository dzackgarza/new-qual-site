---
schema: qual/card@1
id: P-AGH393FLATEXAMPLES
kind: problem
title: Examples of flatness and nonflatness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Finite Morphisms
  - Embedded Points
relations: []
review: draft
---

::: problem
Some examples of flatness and nonflatness.

a. If $f: X \to Y$ is a finite surjective morphism of nonsingular varieties over an algebraically closed field $k$, then $f$ is flat.

b. Let $X$ be a union of two planes meeting at a point, each of which maps isomorphically to a plane $Y$. Show that $f$ is not flat. For example, let $Y = \Spec k[x,y]$ and
\[
X = \Spec k[x,y,z,w] / (z,w) \intersect (x+z, y+w)
.\]

c. Again let $Y = \Spec k[x,y]$, but take $X = \Spec k[x,y,z,w] / (z^2, zw, w^2, xz - yw)$. Show that $X_{\mathrm{red}} \cong Y$ and $X$ has no embedded points, but that $f$ is not flat.
:::
