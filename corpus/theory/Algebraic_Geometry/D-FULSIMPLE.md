---
schema: qual/card@1
id: D-FULSIMPLE
kind: definition
title: Simple and simplicial polytopes, and which one makes the normal fan simplicial
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Polytopes
  - Quotient Singularities
relations:
- kind: uses
  target: D-TORPOLY
- kind: uses
  target: PR-D2F15
review: draft
prompts:
- Distinguish simple from simplicial polytopes, with an example of each that is not the other.
- Which condition on a polytope makes X_P have only finite quotient singularities?
---

::: {.definition}
Let $P$ have dimension $d$.

- $P$ is a \dfn{simplex} if it has exactly $d+1$ vertices.

- $P$ is **simple** if every vertex lies on exactly $d$ facets.

- $P$ is **simplicial** if every facet is a simplex.
:::

::: {.proposition}
The normal fan $\Sigma_P$ is simplicial exactly when $P$ is simple.
Hence $X_P$ is $\QQ$-factorial with at worst finite quotient singularities exactly when $P$ is simple, and $X_P$ is smooth exactly when in addition each vertex has its $d$ edge directions forming a $\ZZ$-basis of $M$.
:::

::: {.example title="Each without the other"}
The cube in $\RR^3$ is simple and not simplicial: each vertex meets three facets, but the facets are squares.
The octahedron in $\RR^3$ is simplicial and not simple: each facet is a triangle, but each vertex meets four of them.
The two are polar duals, which is the general picture — $P$ is simple exactly when $P^\circ$ is simplicial.
:::

::: {.remark}
The direction of the correspondence is the thing to get right, and the normal fan is what fixes it.
Vertices of $P$ give the maximal cones of $\Sigma_P$, and a maximal cone is spanned by the facet normals at its vertex.
So "each vertex meets exactly $d$ facets" is literally "each maximal cone has exactly $d$ rays", which is simpliciality of the fan.
The facets of $P$ contribute only the rays, and their internal shape is irrelevant.
:::
