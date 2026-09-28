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
The \dfn{Néron--Severi group} is $\NS(X) = \Div(X)/\equiv$.
Its rank $\rho(X)$ is the \dfn{Picard number}.
:::

::: {.theorem title="Theorem of the base"}
$\NS(X)$ is a finitely generated abelian group.
:::

::: {.remark}
For a smooth projective surface $X$ over $\CC$, the connected component $\Pic^0(X)$ of $\Pic(X)$ is an abelian variety of dimension $q = h^1(\OO_X)$, and $\NS(X)$ as defined here is $\Pic(X)/\Pic^0(X)$ modulo its torsion subgroup.
For $D\in\Pic^0(X)$ and every divisor $E$, $D\cdot E=0$, so the intersection pairing is defined on $\NS(X)$, where it is a nondegenerate symmetric bilinear form on a free abelian group of finite rank.
By the Hodge index theorem, its extension to $\NS(X)\otimes\RR$ has signature $(1,\rho(X)-1)$.

Examples are $\rho(\PP^2)=1$ and $\rho(\PP^1\times\PP^1)=2$, where $\NS=\Pic$ because $q=0$; a K3 surface has $q=0$ and $1\le\rho\le20$; an abelian surface has $q=2$, so $\Pic^0$ is two-dimensional and $\NS$ is a genuine quotient.
Blowing up a point adds one to $\rho$, adjoining the class of the exceptional curve.
:::
