---
schema: qual/card@1
id: D-FK47C
kind: definition
title: Elementary symmetric functions
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Polynomials
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring and let $x_1, \ldots, x_n$ be indeterminates over $R$.
The \dfn{elementary symmetric functions} in $x_1, \ldots, x_n$ are $e_0 \coloneqq 1$ and
$$
e_k \coloneqq \sum_{1\leq i_1 < i_2 < \cdots < i_k\leq n} x_{i_1} x_{i_2}\cdots x_{i_k} \in R[x_1, \ldots, x_n], \qquad 1 \leq k \leq n.
$$
:::

::: {.proposition}
In $R[x_1,\ldots,x_n][t]$,
$$
\prod_{i=1}^n (t - x_i) = \sum_{k=0}^n (-1)^k e_k t^{n-k}.
$$
Consequently, if a monic polynomial of degree $n$ over a commutative ring factors as $\prod_{i=1}^n(t-r_i)$, its coefficient of $t^{n-k}$ is $(-1)^k e_k(r_1,\ldots,r_n)$.
:::

::: {.theorem}
Let $R$ be a commutative ring.
Every symmetric polynomial in $R[x_1, \ldots, x_n]$ is equal to $g(e_1, \ldots, e_n)$ for a unique polynomial $g\in R[y_1,\ldots,y_n]$.
:::

::: {.concept}
See [@DF04].
:::
