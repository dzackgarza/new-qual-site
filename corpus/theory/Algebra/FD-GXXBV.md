---
schema: qual/card@1
id: FD-GXXBV
kind: definition
title: Euclidean domain
prompts:
- What is a Euclidean domain?
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Factorization
relations: []
review: draft
---

::: {.definition}
An [[D-QJ3QL|integral domain]] $R$ is a \dfn{Euclidean domain} if there exists a function $f\colon R\setminus\theset{0} \to \ZZ^{\geq 0}$, a \dfn{Euclidean function}, such that for all $a\in R$ and all nonzero $b\in R$ there exist $q, r\in R$ with $a = bq + r$ and either $r=0$ or $f(r) < f(b)$.
:::
