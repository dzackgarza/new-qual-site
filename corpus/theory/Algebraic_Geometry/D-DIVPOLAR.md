---
schema: qual/card@1
id: D-DIVPOLAR
kind: definition
title: Polarizations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Polarizations
  - Ample Line Bundles
  - Neron-Severi Group
relations:
- kind: uses
  target: D-DIVAMPLE
- kind: uses
  target: D-DIVEQUIV
review: draft
prompts:
- What is a polarization?
---

::: {.definition}
A \dfn{polarization} on a projective variety $X$ is the class in $\NS(X)$ of an ample line bundle.
A \dfn{polarized variety} is a pair $(X, \mcl)$ with $\mcl$ ample, considered up to isomorphisms preserving the class of $\mcl$ in $\NS(X)$.
The \dfn{degree} of a polarization on $X$ of dimension $n$ is the intersection number $\mcl^n$.
:::

::: {.example}
$(\PP^n, \OO(1))$ is polarized of degree $1$, and a hypersurface of degree $d$ with $\OO(1)$ is polarized of degree $d$.
A K3 surface with an ample class $h$ has a polarization of degree $h^2 = 2g - 2$, and a quartic surface in $\PP^3$ is a K3 surface of degree $4$.
For an abelian variety $A$, a polarization is equivalently an isogeny $A \to A^\dual$ of the form $x \mapsto t_x^* \mcl \otimes \mcl^{-1}$; it is \dfn{principal} when this is an isomorphism, as for the theta divisor on the Jacobian of a curve.
:::
