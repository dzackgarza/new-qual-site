---
schema: qual/card@1
id: FD-S62UB
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
relations:
- kind: variant-of
  target: D-4I3SL
review: draft
---

::: {.definition}
Let $R$ be a commutative [[D-GURUB|ring]].
An element $r\in R$ is a \dfn{zero divisor} if there exists a nonzero $x\in R$ such that $rx=0$.
:::

::: {.remark}
Equivalently, the $R$-linear map $R\to R$, $x\mapsto rx$, is not injective, since its kernel is $\theset{x\in R \st rx=0}$.
:::
