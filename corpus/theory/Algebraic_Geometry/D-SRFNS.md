---
schema: qual/card@1
id: D-SRFNS
kind: definition
title: Numerical equivalence and the Néron--Severi group
classification:
  areas:
  - algebraic-geometry
  topics:
  - Neron-Severi Group
  - Intersection Theory
  - Surfaces
relations:
- kind: uses
  target: D-SRFINT
review: draft
prompts:
- What is the Néron--Severi group?
- Define numerical equivalence.
- What is the Picard number?
- What is the Néron--Severi theorem?
---

::: {.definition}
Divisors $D$ and $D'$ on a surface $X$ are \dfn{numerically equivalent}, $D \equiv D'$, if $D \cdot E = D' \cdot E$ for every divisor $E$.
The **Néron--Severi group** is $\NS(X) = \Div(X)/\equiv$.
:::

::: {.theorem title="Theorem of the base"}
$\NS(X)$ is a finitely generated abelian group.
Its rank $\rho(X)$ is the **Picard number**.
:::

::: {.remark}
The point of passing to $\NS$ is that $\Pic$ is usually not discrete: the connected component $\Pic^0$ is an abelian variety of dimension $q = h^1(\OO_X)$, and $\NS$ is the component group modulo torsion.
Intersection numbers cannot see $\Pic^0$, so the intersection pairing lives on $\NS$, where it is a nondegenerate symmetric bilinear form on a finitely generated group — a lattice.
The Hodge index theorem is the statement of its signature.

Examples to quote: $\rho(\PP^2) = 1$ and $\rho(\PP^1 \times \PP^1) = 2$, where $\NS = \Pic$ because $q = 0$; a K3 surface has $q=0$ and $\rho$ between $1$ and $20$; an abelian surface has $q=2$, so $\Pic^0$ is two-dimensional and $\NS$ is a genuine quotient.
Blowing up a point adds one to $\rho$, adjoining the class of the exceptional curve.
:::
