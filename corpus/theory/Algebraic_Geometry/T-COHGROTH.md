---
schema: qual/card@1
id: T-COHGROTH
kind: theorem
title: Grothendieck vanishing above the dimension
slogan: 'An $n$-dimensional Noetherian space has no sheaf cohomology above degree $n$, with no coherence hypothesis needed.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Vanishing Theorems
  - Dimension
relations:
- kind: uses
  target: D-COHDER
review: draft
prompts:
- State Grothendieck vanishing.
- What is the cohomological dimension of a scheme?
- Why does $H^i(\PP^n, \mcf)$ vanish for $i > n$?
---

::: {.theorem}
Let $X$ be a Noetherian topological space of dimension $n$.
Then $H^i(X, \mcf) = 0$ for all $i > n$ and every sheaf of abelian groups $\mcf$ on $X$.
:::

::: {.remark}
The theorem places no hypothesis on $\mcf$: it need not be quasicoherent or coherent.
The bound is topological: it is the dimension of the underlying space, not the dimension of a variety over a field.

The Noetherian hypothesis on $X$ cannot be dropped; the proof is a Noetherian induction on closed subsets.
The bound is sharp: $H^n(\PP^n, \OO(-n-1)) \neq 0$.

For quasicoherent sheaves there is a shorter route to the same bound on $\PP^n$: a cover by $n+1$ affines makes the Čech complex vanish above degree $n$.
The two arguments give the same number for different reasons, and the Čech one says nothing about non-quasicoherent sheaves.
:::
