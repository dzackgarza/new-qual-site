---
schema: qual/card@1
id: PR-I1T7M
kind: proposition
title: A polynomial of degree $2$ or $3$ is irreducible exactly when it has no root
slogan: 'In degree $2$ or $3$, irreducibility over a field is checked by looking for roots.'
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and let $f\in k[x]$ have degree $2$ or $3$.
Then $f$ is [[D-BVMTZ|irreducible]] in $k[x]$ if and only if $f$ has no root in $k$ [@DF04, Proposition 9.4.10].
:::

::: {.remark}
The criterion fails in degree $4$: $x^4+4=(x^2+2x+2)(x^2-2x+2)$ is reducible over $\QQ$ and has no rational root.
:::
