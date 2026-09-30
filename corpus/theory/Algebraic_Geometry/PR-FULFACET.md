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
Let $\sigma \subseteq N_\RR$ span $N_\RR$, and let $\tau \leq \sigma$ be a facet.
Then there is $u_\tau \in \dualof{\sigma}$, unique up to a positive scalar and unique on the nose once taken primitive in $M$, with
\[
\tau = \sigma \intersect u_\tau^\perp .
\]
It spans the ray $\dualof{\sigma} \intersect \tau^\perp$, and the hyperplane $H_\tau \definedas u_\tau^\perp$ is the hyperplane spanned by $\tau$.
:::

::: {.proposition title="Two presentations"}
If $\sigma$ spans $N_\RR$ and $\sigma \neq N_\RR$, then
\[
\sigma = \Intersect_{\tau \text{ a facet of } \sigma} H_\tau^+ , \qquad H_\tau^+ \definedas \theset{ v \in N_\RR \st \inner{u_\tau}{v} \geq 0 } .
\]
Equivalently, if $u_1, \ldots, u_t$ generate $\dualof{\sigma}$, then
\[
\sigma = \theset{ v \in N_\RR \st \inner{u_1}{v} \geq 0, \ \ldots, \ \inner{u_t}{v} \geq 0 } .
\]
:::

::: {.remark title="Generators against inequalities"}
This is the working content of double duality.
A cone arrives in one of two forms, and every computation needs the other.

- Given by generators, $\sigma = \Cone(v_1, \ldots, v_r)$: the inequalities are $\inner{u}{v_i} \geq 0$, and solving them produces $\dualof{\sigma}$.

- Given by inequalities, $\sigma = \Intersect H_{u_j}^+$: the $u_j$ are generators of $\dualof{\sigma}$.

So passing from generators to inequalities on one side is passing from inequalities to generators on the other, and dualising twice returns the start.
The facet normals are the minimal such list: $\dualof{\sigma}$ needs exactly the primitive $u_\tau$ as its ray generators, one per facet of $\sigma$.
:::
