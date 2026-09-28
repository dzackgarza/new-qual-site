---
schema: qual/card@1
id: D-QQIQZ
kind: definition
title: Units
classification:
  areas:
  - algebra
  topics:
  - Rings
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-GURUB|ring]].
An element $r\in R$ is a \dfn{unit} if there exists $s\in R$ such that $rs = sr = 1$.
The set of units of $R$ is denoted $R^{\times}$.
:::

::: {.remark}
If $r\in R^{\times}$, the element $s$ with $rs=sr=1$ is unique: if also $rs'=s'r=1$, then $s'=s'(rs)=(s'r)s=s$.
It is written $r^{-1}$, and $(R^{\times}, \cdot)$ is a group, abelian when $R$ is commutative.
:::
