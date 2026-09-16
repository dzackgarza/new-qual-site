---
schema: qual/card@1
id: FF-CY5EA
kind: fact
title: Torsion elements of a module
prompts:
- When is $m \in M$ a torsion element?
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
relations: []
review: draft
---

::: {.fact}
Let $R$ be a commutative ring and let $M$ be an $R$-module.
An element $m\in M$ is a [[D-ZJJ7G|torsion element]] if and only if its annihilator $\Ann_R(m)\coloneqq\theset{r\in R\suchthat rm=0}$ is a nonzero ideal of $R$.
:::

::: {.proof}
By definition, $m$ is a torsion element if and only if there is a nonzero $r\in R$ with $rm=0$, that is, a nonzero element of $\Ann_R(m)$.
:::
