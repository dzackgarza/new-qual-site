---
schema: qual/card@1
id: D-T4LOC
kind: definition
title: Dual norm
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Norms
relations: []
review: draft
---

::: {.definition}
Let $X\neq\theset{0}$ be a normed vector space over $\CC$, and let $\dualof{X}$ be the space of continuous [[D-EPSKF|linear functionals]] $X\to\CC$.
For $L \in \dualof{X}$, the \dfn{dual norm} or \dfn{operator norm} of $L$ is
$$
\norm{L}_{\dualof{X}}
\coloneqq \sup_{ \substack{x\in X \\ \norm{x} = 1} } \abs{L(x)}
= \sup_{ \substack{x\in X \\ \norm{x} \leq  1} } \abs{L(x)}.
$$
:::
