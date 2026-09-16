---
schema: qual/card@1
id: D-SI6OM
kind: definition
title: Deck transformation
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $p\colon\tilde X\to X$ be a [[D-ANO2D|covering space]].
A \dfn{deck transformation} of $p$ is a [[D-9KQZT|homeomorphism]] $\psi\colon\tilde X\to\tilde X$ with $p\circ\psi=p$.
The deck transformations form a group $\Deck(\tilde X\to X)$ under composition.
:::

::: {.remark}
In the slice category $\mathsf{Top}_{/X}$, whose objects are continuous maps to $X$ and whose morphisms are maps over $X$, the group $\Deck(\tilde X\to X)$ is the automorphism group $\Aut_{\mathsf{Top}_{/X}}(p)$ of the object $p\colon\tilde X\to X$.
A deck transformation permutes each fiber $p\inv(x)$.
If $\tilde X$ is connected, a deck transformation is determined by the image of one point, so a deck transformation with a fixed point is the identity [@Hat02, p. 70].
:::
