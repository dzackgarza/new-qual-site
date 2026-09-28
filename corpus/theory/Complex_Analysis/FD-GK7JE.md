---
schema: qual/card@1
id: FD-GK7JE
kind: definition
title: Conformal map
prompts:
- What is a conformal map?
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Holomorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open.
A map $f\colon\Omega\to\CC$ is \dfn{conformal} if $f$ is [[D-E7A5W|holomorphic]] on $\Omega$ and $f'(z)\neq0$ for every $z\in\Omega$.
:::

::: {.proposition}
A conformal map $f\colon\Omega\to\CC$ is locally injective: every $z_0\in\Omega$ has an open neighborhood on which $f$ is injective.
:::

::: {.proof}
Since $f'(z_0)\neq0$, the holomorphic inverse function theorem gives an open neighborhood $V$ of $z_0$ such that $f|_V$ is a bijection onto an open set with holomorphic inverse; in particular $f|_V$ is injective.
:::
