---
schema: qual/card@1
id: D-BVMTZ
kind: definition
title: Reducible and irreducible polynomials
prompts:
- When is a polynomial over a field irreducible?
- When is a polynomial irreducible, in terms of the degrees of its factors?
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Irreducibility Criteria
  - Factorization
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and let $f\in k[x]$ be nonconstant.
The polynomial $f$ is \dfn{reducible} if there exist $g, h\in k[x]$ with $\deg g, \deg h \geq 1$ and $f = gh$.
The polynomial $f$ is \dfn{irreducible} if it is not reducible.
:::

::: {.remark}
Every polynomial of degree $1$ is irreducible: in a factorization $f=gh$,
$$
\deg f=\deg g+\deg h=1,
$$
so one factor has degree $0$.
:::
