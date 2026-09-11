---
schema: qual/card@1
id: PR-FULFACET
kind: proposition
title: Facet normals and the half-space presentation of a cone
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
Then there is $u_\tau \in \sigma\dual$, unique up to a positive scalar and unique on the nose once taken primitive in $M$, with
\[
\tau = \sigma \intersect u_\tau^\perp .
\]
It spans the ray $\sigma\dual \intersect \tau^\perp$, and the hyperplane $H_\tau \da u_\tau^\perp$ is the hyperplane spanned by $\tau$.
:::

::: {.proposition title="Two presentations"}
If $\sigma$ spans $N_\RR$ and $\sigma \neq N_\RR$, then
\[
\sigma = \Intersect_{\tau \text{ a facet of } \sigma} H_\tau^+ , \qquad H_\tau^+ \da \ts{ v \in N_\RR \st \inp{u_\tau}{v} \geq 0 } .
\]
Equivalently, if $u_1, \ldots, u_t$ generate $\sigma\dual$, then
\[
\sigma = \ts{ v \in N_\RR \st \inp{u_1}{v} \geq 0, \ \ldots, \ \inp{u_t}{v} \geq 0 } .
\]
:::

::: {.remark title="Generators against inequalities"}
This is the working content of double duality.
A cone arrives in one of two forms, and every computation needs the other.

- Given by generators, $\sigma = \Cone(v_1, \ldots, v_r)$: the inequalities are $\inp{u}{v_i} \geq 0$, and solving them produces $\sigma\dual$.

- Given by inequalities, $\sigma = \Intersect H_{u_j}^+$: the $u_j$ are generators of $\sigma\dual$.

So passing from generators to inequalities on one side is passing from inequalities to generators on the other, and dualising twice returns the start.
The facet normals are the minimal such list: $\sigma\dual$ needs exactly the primitive $u_\tau$ as its ray generators, one per facet of $\sigma$.
:::
