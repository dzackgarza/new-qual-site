---
schema: qual/card@1
id: FE-ISIPR
kind: example
title: The Zariski topology on $\AA^2$ is not the product topology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Varieties
relations:
- kind: uses
  target: D-BIVAU
review: draft
prompts:
- Is the Zariski topology on $\AA^2$ the product of the Zariski topologies on the factors?
---

::: {.example}
The diagonal $\Delta = V(x-y) \subseteq \AA^2$ is Zariski closed.
It is not closed in the product topology.

Suppose it were.
Then $\AA^2 \sm \Delta$ would be open in the product, so it would contain a basic open box $U \times V$ around any of its points.
Each factor carries the cofinite topology, so $U = \AA^1 \sm \ts{p_1,\ldots,p_m}$ and $V = \AA^1 \sm \ts{q_1,\ldots,q_n}$.
Over an infinite field choose $z$ distinct from every $p_i$ and $q_j$; then $(z,z) \in (U \times V) \intersect \Delta$, contradicting $U \times V \subseteq \AA^2 \sm \Delta$.
:::

::: {.remark}
The product topology is strictly coarser: it sees only finite unions of horizontal and vertical lines, and no curve that is not one.
This is why the product in the category of varieties is not the topological product, and it is worth having ready, because the same point returns for schemes as the statement that $\Spec$ does not take products to products.
:::
