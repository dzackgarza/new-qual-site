---
schema: qual/card@1
id: P-AGH2218RINGMAPSPEC
kind: problem
title: Injectivity and surjectivity of a ring map read off from the induced morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Ring Homomorphisms
  - Closed Immersions
relations: []
review: draft
---

::: problem
Compare properties of a ring homomorphism to the induced morphism on spectra.

a. Let $A$ be a ring, $X = \Spec A$, and $f \in A$.
Show that $f$ is nilpotent if and only if $D(f)$ is empty.

b. Let $\phi: A \to B$ be a homomorphism of rings and let $f: Y = \Spec B \to X = \Spec A$ be the induced morphism of affine schemes.
Show that $\phi$ is injective if and only if the map of sheaves $f^{\sharp}: \OO_X \to f_* \OO_Y$ is injective.
Show furthermore that in that case $f$ is dominant, that is, $f(Y)$ is dense in $X$.

c. With the same notation, show that if $\phi$ is surjective then $f$ is a homeomorphism of $Y$ onto a closed subset of $X$, and $f^{\sharp}: \OO_X \to f_* \OO_Y$ is surjective.

d. Prove the converse to (c): if $f: Y \to X$ is a homeomorphism onto a closed subset and $f^{\sharp}: \OO_X \to f_* \OO_Y$ is surjective, then $\phi$ is surjective.
:::

::: remark
For part (d), consider $X' = \Spec\qty{A/\ker \phi}$ and apply parts (b) and (c).
:::
