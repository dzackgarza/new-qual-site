---
schema: qual/card@1
id: D-MSYMF
kind: definition
title: Monomial symmetric functions
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring, let $x_1,\ldots,x_n$ be indeterminates over $R$, and let $\lambda=(\lambda_1,\ldots,\lambda_\ell)$ be a [[D-YTABL|partition]] with $\ell\leq n$.
The \dfn{monomial symmetric function} $m_\lambda$ is the sum of the distinct monomials $x^\alpha=x_1^{\alpha_1}\cdots x_n^{\alpha_n}$ whose exponent vector $\alpha\in\NN^n$ is a rearrangement of $(\lambda_1,\ldots,\lambda_\ell,0,\ldots,0)$:
$$
m_\lambda\coloneqq\sum_{\alpha}x^{\alpha},
$$
the sum over the distinct such $\alpha$.
:::
