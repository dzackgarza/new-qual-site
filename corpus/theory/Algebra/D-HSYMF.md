---
schema: qual/card@1
id: D-HSYMF
kind: definition
title: Complete homogeneous symmetric functions
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring and let $x_1,\ldots,x_n$ be indeterminates over $R$.
For $k\geq0$ the \dfn{complete homogeneous symmetric function} $h_k$ is the sum of all monomials of total degree $k$ in $x_1,\ldots,x_n$; equivalently it is the coefficient of $t^k$ in $\prod_{i=1}^n(1-x_it)^{-1}$, and $h_0=1$.
For a [[D-YTABL|partition]] $\lambda$ one sets $h_\lambda\coloneqq\prod_i h_{\lambda_i}$.
:::
