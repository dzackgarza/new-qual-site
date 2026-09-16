---
schema: qual/card@1
id: E-HAT-3.3-3
kind: problem
title: "Covering spaces of orientable manifolds"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that every covering space of an orientable manifold is an orientable manifold.
:::

::: {.solution}
Let $p:\widetilde M\to M$ be a covering map and suppose $M$ is orientable. For each $x\in M$, choose an orientation class
\[
\mu_x\in H_n(M,M-\{x\};\mathbb Z)
\]
that varies locally constantly with $x$.

If $\widetilde x\in\widetilde M$ and $x=p(\widetilde x)$, choose an evenly covered neighborhood $U$ of $x$ and let $\widetilde U$ be the sheet containing $\widetilde x$. The restriction
\[
p:\widetilde U\longrightarrow U
\]
is a homeomorphism, hence induces an isomorphism on local homology. Define the local orientation at $\widetilde x$ to be the unique class
\[
\widetilde\mu_{\widetilde x}\in H_n(\widetilde M,\widetilde M-\{\widetilde x\};\mathbb Z)
\]
that maps to $\mu_x$ under this local identification.

On a fixed sheet over an evenly covered neighborhood, these classes vary locally constantly because the classes $\mu_x$ do. Thus the collection $\widetilde\mu_{\widetilde x}$ defines an orientation of $\widetilde M$. Therefore every covering space of an orientable manifold is orientable.
:::
