---
schema: qual/card@1
id: P-AGHPRODTOP
kind: problem
title: The Zariski topology on $\AA^2$ against the product topology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Products
relations:
- kind: related-to
  target: FE-ISIPR
review: draft
---

::: problem
Identify $\AA^2$ with $\AA^1 \times \AA^1$ in the natural way.
Show that the Zariski topology on $\AA^2$ is not the product topology of the Zariski topologies on the two copies of $\AA^1$.
:::

::: solution
The diagonal $\Delta = V(x-y)$ is Zariski closed in $\AA^2$, and it is not closed in the product topology.

Suppose it were.
Then $\AA^2 \sm \Delta$ is open in the product, so it contains a basic box $U \times V$ around each of its points.
On $\AA^1$ the Zariski topology is cofinite, so $U = \AA^1 \sm \ts{p_1,\ldots,p_m}$ and $V = \AA^1 \sm \ts{q_1,\ldots,q_n}$.
Over an infinite field pick $z$ distinct from every $p_i$ and $q_j$; then $(z,z)$ lies in $U \times V$ and on $\Delta$, contradicting $U \times V \subseteq \AA^2 \sm \Delta$.

The product topology sees only finite unions of horizontal and vertical lines, and no curve that is not one; the Zariski topology on $\AA^2$ has a closed set for every plane curve.
:::

::: {.remark}
Erratum: an alternative argument sometimes given uses the hyperbola $V(xy-1)$, whose projection $\pi_x(V(xy-1)) = \AA^1 \sm \ts{0}$ is not closed, and claims that projections would be closed maps if $\AA^2$ had the product topology.
Projections from a product topology are open maps but need not be closed, so that argument does not work.
:::
