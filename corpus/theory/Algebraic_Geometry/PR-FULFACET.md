---
schema: qual/card@1
id: PR-FULFACET
kind: proposition
title: Facet normals and the half-space presentation of a cone
slogan: 'Facet normals generate the dual cone, and their nonnegative half-spaces cut out the original cone.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cones
  - Convex Geometry
relations:
- kind: uses
  target: PR-FULSEP
review: draft
prompts:
- Given a full-dimensional cone, produce the linear functional cutting out a given facet.
- Present a cone as an intersection of half-spaces, and as inequalities against the generators of its dual.
---

::: {.proposition title="The facet normal"}
Let $N$ be a lattice, put $M\coloneqq\Hom(N,\ZZ)$, let $\sigma\subseteq N_\RR$ be a full-dimensional rational polyhedral cone, and let $\tau\leq\sigma$ be a facet.
Then the ray
$$
\dualof{\sigma}\intersect\tau^\perp\subseteq M_\RR
$$
has a unique primitive generator $u_\tau\in M\cap\dualof{\sigma}$. It satisfies
$$
\tau = \sigma \intersect u_\tau^\perp .
$$
The hyperplane $H_\tau\coloneqq u_\tau^\perp$ is the linear span of $\tau$.
:::

::: {.proposition title="Two presentations"}
If $\sigma$ spans $N_\RR$ and $\sigma \neq N_\RR$, then
$$
\sigma = \Intersect_{\tau \text{ a facet of } \sigma} H_\tau^+ , \qquad
H_\tau^+ \coloneqq \theset{ v \in N_\RR \st \inner{u_\tau}{v} \geq 0 } .
$$
Equivalently, if $u_1, \ldots, u_t$ generate $\dualof{\sigma}$, then
$$
\sigma = \theset{ v \in N_\RR \st \inner{u_1}{v} \geq 0, \ \ldots, \ \inner{u_t}{v} \geq 0 } .
$$
:::

::: {.remark title="Generators against inequalities"}
If $\sigma=\Cone(v_1,\ldots,v_r)$, then
$$
\sigma^\vee=\theset{u\in M_\RR\st\inner{u}{v_i}\geq0\text{ for }1\leq i\leq r}.
$$
Conversely, if $\sigma=\theset{v\in N_\RR\st\inner{u_j}{v}\geq0\text{ for }1\leq j\leq t}$, then $\sigma^\vee=\Cone(u_1,\ldots,u_t)$.
For a full-dimensional rational polyhedral cone, the irredundant inequalities are indexed by its facets, so the primitive facet normals $u_\tau$ are exactly the primitive ray generators of $\sigma^\vee$.
:::
