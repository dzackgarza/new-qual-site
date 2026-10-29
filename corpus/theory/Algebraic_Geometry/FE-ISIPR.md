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
Let $k$ be an infinite field.
The diagonal $\Delta = V(x-y) \subseteq \AA^2$ is Zariski closed.
It is not closed in the product topology.

Suppose it were.
Then $\AA^2 \sm \Delta$ would be open in the product, so it would contain a basic open box $U \times V$ around any of its points.
Each factor carries the cofinite topology, so $U = \AA^1 \sm \theset{p_1,\ldots,p_m}$ and $V = \AA^1 \sm \theset{q_1,\ldots,q_n}$.
Since $k$ is infinite, choose $z$ distinct from every $p_i$ and $q_j$; then $(z,z) \in (U \times V) \intersect \Delta$, contradicting $U \times V \subseteq \AA^2 \sm \Delta$.
:::

::: {.remark}
For infinite $k$, the product topology is strictly coarser than the Zariski topology on the scheme product.
Categorically,
$$
\Spec(A\tensor_k B)
\cong
\Spec A\times_{\Spec k}\Spec B,
$$
but the underlying topological space of this fibre product is generally not the product of the underlying Zariski spaces.
The diagonal in $\AA^1_k\times_k\AA^1_k$ is the basic example of a closed subset detected by the scheme product and missed by the product topology.
:::
