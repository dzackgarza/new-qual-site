---
schema: qual/card@1
id: D-SCHUR
kind: definition
title: Schur functions
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Young Tableaux
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring, let $x_1,\ldots,x_n$ be indeterminates over $R$, and let $\lambda$ be a [[D-YTABL|partition]] with at most $n$ parts.
The \dfn{Schur function} $s_\lambda(x_1,\ldots,x_n)$ is the sum
$$
s_\lambda\coloneqq\sum_{T}x^{\operatorname{cont}(T)},
$$
over the [[D-YTABL|semistandard tableaux]] $T$ of shape $\lambda$ with entries in $\{1,\ldots,n\}$, where $x^{\operatorname{cont}(T)}\coloneqq\prod_i x_i^{\nu_i}$ for the content $\nu$ of $T$.
:::

::: {.remark}
For $\lambda$ with at most $n$ parts,
$$
s_\lambda=\frac{\det(x_i^{\lambda_j+n-j})_{1\leq i,j\leq n}}{\det(x_i^{n-j})_{1\leq i,j\leq n}},
$$
the Weyl character formula for $\GL_n$; the determinantal form is the definition adopted in [@FH91, (A.4)].
:::
