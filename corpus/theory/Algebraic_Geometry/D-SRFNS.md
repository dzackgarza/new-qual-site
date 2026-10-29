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
Let $X$ be a smooth projective surface over an algebraically closed field.
The \dfn{Néron--Severi group} is
$$
\NS(X)
\coloneqq
\Pic(X)/\Pic^0(X)
\cong
\Div(X)/{\sim_{\mathrm{alg}}}.
$$

Divisors $D$ and $D'$ are \dfn{numerically equivalent}, $D\equiv D'$, if
$$
D\cdot E=D'\cdot E
\qquad
\text{for every divisor }E.
$$
The \dfn{numerical divisor group} is
$$
N^1(X)
\coloneqq
\Div(X)/\equiv.
$$
:::

::: {.theorem title="Theorem of the base"}
$\NS(X)$ is a finitely generated abelian group.
The natural map
$$
\NS(X)\longrightarrow N^1(X)
$$
is surjective with torsion kernel, so
$$
N^1(X)\cong\NS(X)/\NS(X)_{\mathrm{tors}}.
$$
Their common rank $\rho(X)$ is the \dfn{Picard number}.
:::

::: {.remark}
The point of passing to $\NS$ is that $\Pic$ is usually not discrete: the connected component $\Pic^0$ is an abelian variety of dimension $q = h^1(\OO_X)$, and $\NS=\Pic/\Pic^0$ is the discrete component group.
Intersection numbers cannot see $\Pic^0$ or torsion in $\NS$, so the intersection pairing descends to $N^1(X)$.
After tensoring with $\RR$ it is a nondegenerate symmetric bilinear form on
$$
N^1(X)_\RR
\coloneqq
N^1(X)\tensor_\ZZ\RR,
$$
and the Hodge index theorem gives signature $(1,\rho(X)-1)$.

Examples are $\rho(\PP^2)=1$ and $\rho(\PP^1\times\PP^1)=2$, where $\NS=\Pic$ because $\Pic^0=0$.
For a complex projective K3 surface, $\Pic^0=0$ and $1\le\rho\le20$; in positive characteristic the Picard number of a K3 surface can be as large as $22$.
For an abelian surface, $\Pic^0$ has dimension $2$, so $\NS$ is a genuine quotient of $\Pic$.
Blowing up a point adds one to $\rho$, adjoining the class of the exceptional curve.
:::
