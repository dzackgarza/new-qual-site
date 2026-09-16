---
schema: qual/card@1
id: FT-52GNK
kind: theorem
title: Urysohn's lemma
prompts:
- State Urysohn's lemma.
- Which separation property does Urysohn's lemma characterise, and by what function?
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Continuity
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a topological space.
Then $X$ is [[D-YEQC3|normal]] if and only if for every pair of disjoint closed subsets $A, B \subseteq X$ there is a continuous function $f\colon X\to [0,1]$ with $f(a) = 0$ for all $a\in A$ and $f(b) = 1$ for all $b\in B$ [@Mun00].
:::

::: {.remark}
The forward direction is Urysohn's lemma; the converse follows by taking the disjoint open sets $f^{-1}([0,1/2))$ and $f^{-1}((1/2,1])$.
The hypothesis that $A$ and $B$ are disjoint cannot be dropped: if $A\cap B\neq\emptyset$, no such $f$ exists.
:::
