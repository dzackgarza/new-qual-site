---
schema: qual/card@1
id: D-FK47C
kind: definition
title: Elementary Symmetric Functions
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Polynomials
relations: []
review: draft
---

::: {.definition title="Elementary Symmetric Functions"}
For indeterminates $x_1, \cdots, x_n$ over a commutative ring $R$, the **elementary symmetric functions** are
\[
e_k \da \sum_{i_1 < i_2 < \cdots < i_k} x_{i_1} x_{i_2}\cdots x_{i_k}, \qquad 1 \leq k \leq n
,\]
together with $e_0 \da 1$.
They are the coefficients of the generic monic polynomial:
\[
\prod_{i=1}^n (t - x_i) = \sum_{k=0}^n (-1)^k e_k t^{n-k}
,\]
so the coefficients of a monic polynomial are, up to sign, the elementary symmetric functions of its roots.
Every symmetric polynomial in $R[x_1, \cdots, x_n]$ is a polynomial in $e_1, \cdots, e_n$ over $R$, uniquely so.
:::

::: {.concept}
See Dummit and Foote, §14.6.
:::
