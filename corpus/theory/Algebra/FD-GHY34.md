---
schema: qual/card@1
id: FD-GHY34
kind: definition
title: Irreducible polynomial over a field
prompts:
- When is a polynomial over a field irreducible?
- When is a polynomial irreducible, in terms of the degrees of its factors?
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

::: {.remark title="Degree form"}
Equivalently, a nonconstant $p\in K[x]$ is irreducible if and only if there are no $q,r\in K[x]$ with $p=qr$, $\deg q<\deg p$, and $\deg r<\deg p$.
If $p=qr$, then $\deg q+\deg r=\deg p$, so $q$ is constant exactly when $\deg r=\deg p$, and $r$ is constant exactly when $\deg q=\deg p$.
:::
