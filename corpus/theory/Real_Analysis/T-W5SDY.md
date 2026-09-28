---
schema: qual/card@1
id: T-W5SDY
kind: theorem
title: The dual space $\dualof{X}$ with the operator norm is a Banach space
slogan: 'The dual of every normed space is complete in the operator norm.'
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Norms
  - Completeness
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a normed vector space over $\mathbb K\in\theset{\RR,\CC}$, and let $\dualof{X}$ be the vector space of continuous linear functionals $X\to\mathbb K$ with the [[D-T4LOC|operator norm]] $\norm{L}_{\text{op}}\coloneqq\sup_{x\in X,\ \norm{x}\leq1}\abs{L(x)}$.
Then $(\dualof{X},\norm{\cdot}_{\text{op}})$ is a [[D-BG455|Banach space]].
:::
