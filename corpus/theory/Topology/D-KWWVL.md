---
schema: qual/card@1
id: D-KWWVL
kind: definition
title: Saturated subset
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $p\colon X\to Y$ be a surjective map.
A subset $U\subseteq X$ is \dfn{saturated} with respect to $p$ if for every $y\in Y$ with $U\cap p\inv(y)\neq\emptyset$ we have $p\inv(y)\subseteq U$.
:::

::: {.proposition}
A subset $U\subseteq X$ is saturated with respect to $p$ if and only if $U = p\inv(B)$ for some $B\subseteq Y$, in which case $B = p(U)$.
:::

::: {.concept}
See [@Mun00].
:::
