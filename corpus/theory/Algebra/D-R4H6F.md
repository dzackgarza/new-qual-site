---
schema: qual/card@1
id: D-R4H6F
kind: definition
title: Associate elements
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Rings
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring.
Elements $a, b\in R$ are \dfn{associates} if there exists a [[D-QQIQZ|unit]] $u\in R^{\times}$ such that $a = ub$.
:::

::: {.proposition}
Let $R$ be an [[D-QJ3QL|integral domain]] and $a,b\in R$.
Then $a$ and $b$ are associates if and only if $a\divides b$ and $b\divides a$.
:::

::: {.proof}
If $a=ub$ with $u$ a unit, then $b\divides a$, and $b=u^{-1}a$ gives $a\divides b$.
Conversely, suppose $b=ac$ and $a=bd$ with $c,d\in R$, in the sense of [[D-AVBIP|divisibility]].
If $a=0$, then $b=0$ and $a=1\cdot b$.
If $a\neq 0$, then $a=acd$ gives $a(1-cd)=0$, so $cd=1$ because $R$ is an integral domain; thus $d$ is a unit and $a=db$.
:::
