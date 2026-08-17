---
schema: qual/card@1
id: P-A7YBX
kind: problem
title: Every simple $R$-module is cyclic
classification:
  areas:
  - algebra
  topics:
  - modules
  - semisimplicity
  - cyclic-groups
relations: []
review: draft
solved: false
---

::: problem
We want to show that every simple $R\dash$module $M$ is cyclic, i.e. if the only ideals of $M$ are $(0)$ and $M$ itself, that $M = \generators{m}$ for some element $m\in M$.

Towards a contradiction, let $M$ be a simple $R\dash$module and suppose $M$ is not cyclic, so $M\neq \generators{m}$ for any $m\in M$.
But then let $a\in M$ be an arbitrary nontrivial element; then $(a)$ is a non-empty ideal (since it contains $a$), so $(a) \neq 0$.
Since $M$ is simple, we must have $(a) = M$, a contradiction.
:::
