---
schema: qual/card@1
id: E-U9VN1
kind: problem
title: Manifolds imbed as closed subspaces of codimension at least one
classification:
  areas:
  - topology
  topics:
  - Dimension
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Corollary.
Every $m$-manifold can be imbedded in $\mathbb{R}^{2m+1}$ as a closed subspace.
:::

::: {.solution}
An \(m\)-manifold \(M\) is locally compact Hausdorff and second-countable, and by the preceding corollary \(\dim M\le m\). The noncompact embedding theorem proved in this section says that a locally compact Hausdorff space with a countable basis, all of whose compact subspaces have dimension at most \(m\), embeds as a closed subspace of \(\mathbb R^{2m+1}\). Its hypotheses hold for \(M\) by the proof of the preceding corollary. Therefore there is an embedding
\[
M\hookrightarrow\mathbb R^{2m+1}
\]
whose image is closed.
:::
