---
schema: qual/card@1
id: PR-MK2W6
kind: proposition
title: Irreducible polynomials over a perfect field are separable
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Splitting Fields
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a [[D-KQFIV|perfect]] field, for instance a field of characteristic $0$ or a finite field.
Every irreducible polynomial $f \in k[x]$ has distinct roots in a splitting field of $f$ over $k$.
:::

::: {.example}
Over an imperfect field this fails: for $k = \FF_p(t)$, the polynomial $x^p - t$ is irreducible, and in a splitting field it factors as $(x - t^{1/p})^p$.
:::
