---
schema: qual/card@1
id: T-COHGROTH
kind: theorem
title: Grothendieck vanishing above the dimension
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
Two features distinguish this from every other vanishing theorem on the syllabus.
It asks nothing of $\mcf$: no quasicoherence, no coherence.
And the bound is topological, the dimension of the underlying space, not the dimension of a variety over a field.

Noetherianness of the space is load-bearing and is used to run the Noetherian induction on closed subsets; without it the statement fails.
Nothing else can be dropped, since $H^n$ is generally nonzero: $H^n(\PP^n, \OO(-n-1)) \neq 0$ shows the bound is sharp.

For quasicoherent sheaves there is a cheaper route to the same bound on $\PP^n$: a cover by $n+1$ affines makes the Čech complex vanish above degree $n$.
The two arguments give the same number for different reasons, and the Čech one says nothing about non-quasicoherent sheaves.
:::
