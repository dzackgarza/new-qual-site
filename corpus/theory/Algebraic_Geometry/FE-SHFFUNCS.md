---
schema: qual/card@1
id: FE-SHFFUNCS
kind: example
title: Sheaves of functions on a space and on a manifold
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Examples
  - Structure Sheaf
relations:
- kind: uses
  target: D-VARREG
- kind: related-to
  target: D-AN662
review: draft
prompts:
- Give the standard examples of sheaves of functions.
- Why is the sheaf of continuous functions a sheaf?
- What are the stalks of the sheaf of holomorphic functions?
---

::: {.example title="Sheaves of functions"}
On a topological space $X$ the assignment $U\mapsto C^0(U,\RR)$ of continuous real-valued functions is a sheaf of rings; on a differentiable manifold $U\mapsto C^\infty(U)$ is a subsheaf of it, and on a complex manifold $U\mapsto\OO_X^{an}(U)$ of holomorphic functions is a subsheaf of that [@Har77, Example II.1.0.2].
On an open subset of a variety the same assignment with regular functions is the structure sheaf $\OO_X$ [@Har77, Example II.1.0.1] ([[D-VARREG]]).
:::

::: {.remark}
Each of these satisfies the sheaf axioms for one reason: a function is continuous, smooth, or holomorphic exactly when its restriction to every member of an open cover is, so the functions satisfying the condition glue and are determined by their local restrictions.
The stalks of the holomorphic sheaf are rings of convergent power series, hence local rings, and the maximal ideal at a point is the ideal of functions vanishing there ([[D-AN662]]).
:::
