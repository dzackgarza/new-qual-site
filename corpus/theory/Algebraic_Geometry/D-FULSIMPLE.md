---
schema: qual/card@1
id: D-FULSIMPLE
kind: definition
title: Simple and simplicial polytopes and simplicial normal fans
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
- Which condition on a polytope $P$ makes $X_P$ have only finite quotient singularities?
---

::: {.definition}
Let $P$ have dimension $d$.

- $P$ is a \dfn{simplex} if it has exactly $d+1$ vertices.

- $P$ is \dfn{simple} if every vertex lies on exactly $d$ facets.

- $P$ is \dfn{simplicial} if every facet is a simplex.
:::

::: {.proposition}
The normal fan $\Sigma_P$ is simplicial exactly when $P$ is simple.
Hence $X_P$ is $\QQ$-factorial with at worst finite quotient singularities exactly when $P$ is simple, and $X_P$ is smooth exactly when in addition each vertex has its $d$ edge directions forming a $\ZZ$-basis of $M$.
:::

::: {.example title="Each without the other"}
The cube in $\RR^3$ is simple and not simplicial: each vertex meets three facets, but the facets are squares.
The octahedron in $\RR^3$ is simplicial and not simple: each facet is a triangle, but each vertex meets four of them.
The two are polar duals, which is the general picture — $P$ is simple exactly when $P^\circ$ is simplicial.

Explicitly, the cube $P \subseteq \RR^3$ with vertices $(\pm 1, \pm 1, \pm 1)$ has facet normals $\pm e_1, \pm e_2, \pm e_3$ and facet presentation $\inner{m}{\pm e_i} \geq -1$.
The origin is interior, so $P^\circ$ is the octahedron with vertices $\pm e_i$, and the maximal cones of the normal fan of $P$ are the eight octants of $\RR^3$, the cones over the facets of $P^\circ$.
:::

::: {.remark}
For a full-dimensional polytope $P$, the vertices of $P$ correspond to the maximal cones of $\Sigma_P$: the cone at a vertex $v$ is spanned by the inward facet normals of the facets containing $v$.
So $v$ lies on exactly $d$ facets if and only if its cone has exactly $d$ rays, that is, if and only if the cone is simplicial.
The facets of $P$ correspond to the rays of $\Sigma_P$, so the shape of a facet, such as whether it is a simplex, does not affect whether $\Sigma_P$ is simplicial.
:::
