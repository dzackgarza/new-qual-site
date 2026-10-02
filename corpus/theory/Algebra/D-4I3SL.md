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
Let $R$ be a commutative [[D-GURUB|ring]].
An element $r\in R$ is a \dfn{zero divisor} if there exists a nonzero element $a\in R$ such that
$$
ar=0.
$$
:::

::: {.remark}
Equivalently, $r\in R$ is a zero divisor if and only if the $R$-linear map
$$
R \to R, \qquad x \mapsto rx
$$
is not injective.

For a noncommutative ring, left and right zero divisors are distinct notions and must be specified separately.
:::
