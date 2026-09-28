---
schema: qual/card@1
id: FD-ONITX
kind: definition
title: Local homeomorphism
prompts:
- 'When is a map $f: X \to Y$ a local homeomorphism?'
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Covering Spaces
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
A continuous map $f\colon X\to Y$ is a \dfn{local homeomorphism} if every $x\in X$ has an open [[D-JMRPA|neighborhood]] $U_x$ such that $f(U_x)$ is open in $Y$ and $f\vert_{U_x}\colon U_x \to f(U_x)$ is a [[D-9KQZT|homeomorphism]].
:::

::: {.example}
Every [[D-ANO2D|covering space]] $p\colon\tilde X\to X$ is a local homeomorphism.
For a sheaf of sets $\mathcal F$ on a space $X$, the projection from its étale space to $X$ is a local homeomorphism.
:::
