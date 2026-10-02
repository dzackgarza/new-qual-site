---
schema: qual/card@1
id: D-ZJJ7G
kind: definition
title: Torsion elements, torsion modules, and torsion-free modules
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative [[D-GURUB|ring]] and $M$ an $R$-module.

- An element $m\in M$ is a \dfn{torsion element} if there exists a nonzero $r\in R$ with $rm=0$.

- Write $M_t\coloneqq\theset{m\in M \st rm=0 \text{ for some nonzero } r\in R}$ for the set of torsion elements of $M$.

- $M$ is \dfn{torsion-free} if no nonzero element of $M$ is a torsion element, that is, $M_t\subseteq\theset{0}$.

- $M$ is a \dfn{torsion module} if $M_t=M$.
:::
