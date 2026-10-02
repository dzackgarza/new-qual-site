---
schema: qual/card@1
id: FD-GHY34
kind: definition
title: Irreducible polynomial over a field
prompts:
- When is a polynomial over a field irreducible?
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.definition}
Let $K$ be a [[D-UI6CU|field]].
A polynomial $p\in K[x]$ is \dfn{irreducible} if $\deg p \geq 1$ and whenever $p= qr$ with $q,r\in K[x]$, $q$ or $r$ is constant.
:::

::: {.remark}
Every polynomial of degree $1$ is irreducible: if $p=qr$, then $\deg q+\deg r=1$, so one of $q,r$ has degree $0$.
:::
