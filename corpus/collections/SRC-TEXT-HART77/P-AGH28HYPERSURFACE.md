---
schema: qual/card@1
id: P-AGH28HYPERSURFACE
kind: problem
title: A projective variety has codimension one exactly when it is a hypersurface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Hypersurfaces
  - Height Of Ideals
relations:
- kind: uses
  target: P-AGH26HOMDIM
review: draft
---

::: problem
A projective variety $Y \subseteq \PP^n$ has dimension $n-1$ if and only if it is the zero set of a single irreducible homogeneous polynomial $f$ of positive degree.
In this case $Y$ is called a **hypersurface** in $\PP^n$.
:::

::: solution
**($\implies$).** The affine cone has $\dim C(Y) = \dim Y + 1 = (n-1) + 1 = n$ inside $\AA^{n+1}$, so $C(Y)$ has codimension one there.
Hence $C(Y) = Z(f)$ for some irreducible $f \in k[x_0,\ldots,x_n]$.
Letting $F$ be the homogenization of $f$, the affine cone correspondence gives $Y = Z(F)$.

**($\impliedby$).** Let $Y = Z(F)$ for an irreducible homogeneous $F$ of positive degree.
Then $\gens{F}$ is a minimal prime of height $1$, and the height-quotient formula gives
\[
\height \gens{F} + \dim S/\gens{F} = \dim S
\implies 1 + \dim A(Y) = n
\implies \dim A(Y) = n-1 .
\]
:::
