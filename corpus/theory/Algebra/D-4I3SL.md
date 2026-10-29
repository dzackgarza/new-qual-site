---
schema: qual/card@1
id: D-4I3SL
kind: definition
title: Zero divisor
prompts:
- What is a zero divisor?
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Integral Domains
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-GURUB|ring]].
An element $r\in R$ is a \dfn{zero divisor} if there exists $a\in R\setminus\theset 0$ such that $ar = 0$ or $ra = 0$.
:::

::: {.remark}
If $R$ is commutative, then $r\in R$ is a zero divisor if and only if the $R$-linear map
$$
R \to R, \qquad x \mapsto rx
$$
is not injective.
:::
