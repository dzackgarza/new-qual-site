---
schema: qual/card@1
id: D-NKRGN
kind: definition
title: Euclidean domain
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Factorization
  - Integral Domains
relations: []
review: draft
---

::: {.definition}
An [[D-QJ3QL|integral domain]] $R$ is \dfn{Euclidean} if there exists a function $d\colon R\to \ZZ_{\geq 0}$ such that for all $x,y\in R$ with $y\neq 0$ there exist $q,r\in R$ with $x = qy + r$ and either $r=0$ or $d(r) < d(y)$.
Such a function $d$ is a \dfn{Euclidean function} on $R$.
:::
