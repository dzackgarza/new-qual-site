---
schema: qual/card@1
id: FD-V5ISD
kind: definition
title: Borel sets
prompts:
- What is a Borel set?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
The \dfn{Borel $\sigma$-algebra} of $X$ is the smallest $\sigma$-algebra of subsets of $X$ that contains every open subset of $X$, namely the intersection of all such $\sigma$-algebras.
Its elements are the \dfn{Borel sets} of $X$.
:::

::: {.remark}
Since a $\sigma$-algebra is closed under complements, countable unions, and countable intersections, every closed set, every [[FD-BBR6Q|$F_\sigma$ set]], and every [[FD-HGESN|$G_\delta$ set]] is a Borel set.
:::
