---
schema: qual/card@1
id: E-HAT-4.K-2
kind: problem
title: Contractible fibers of a simplicial map
classification:
  areas:
  - topology
  topics:
  - Symmetric Products
  - Quasifibrations
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that a simplicial map $f: K \to L$ is a homotopy equivalence if $f^{-1}(x)$ is contractible for all $x \in L$.
:::

::: {.solution}
For a simplex $\sigma$ of $L$, let $V_\sigma$ be its open star: the union of the interiors of all simplices containing $\sigma$. Put $U_\sigma=f^{-1}(V_\sigma)$. The $V_\sigma$ cover $L$, and the $U_\sigma$ cover $K$. A nonempty finite intersection of these open stars is $V_\rho$, where $\rho$ is the simplex spanned by the union of their vertices; the corresponding intersection of the $U_\sigma$ is $U_\rho$.

Let $x_\rho$ be the barycenter of $\rho$. The space $V_\rho$ contracts to $x_\rho$. The preimage $U_\rho$ deformation retracts onto $f^{-1}(x_\rho)$. To see this, write a point of a simplex of $K$ in barycentric coordinates. For each vertex $w$ of its image simplex, the sum of the coordinates of vertices mapping to $w$ is the $w$-coordinate of its image. Move these sums linearly toward the coordinates of $x_\rho$, scaling all coordinates in each fiber of the vertex map by the same factor. Every coordinate corresponding to a vertex of $\rho$ has positive sum throughout $U_\rho$, so this scaling is continuous. At the end the image is $x_\rho$, and points already over $x_\rho$ remain fixed.

By hypothesis $f^{-1}(x_\rho)$ is contractible. Thus each restriction $f:U_\rho\to V_\rho$ is a weak homotopy equivalence. Corollary 4K.2 applied to the open-star covers shows that $f$ is a weak homotopy equivalence. Since simplicial complexes have CW type, Whitehead's theorem gives the required homotopy equivalence.
:::
