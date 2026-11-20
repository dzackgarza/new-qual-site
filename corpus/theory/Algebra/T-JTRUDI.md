---
schema: qual/card@1
id: T-JTRUDI
kind: theorem
title: The Jacobi--Trudi identity
slogan: '$s_\lambda=\det(h_{\lambda_i-i+j})$'
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Schur Functions
relations: []
review: draft
---

::: {.theorem}
Let $h_k$ be the complete homogeneous symmetric function of degree $k$ in $x_1,x_2,\ldots$, with $h_0\coloneqq1$ and $h_k\coloneqq0$ for $k<0$, and let $\lambda$ be a partition with at most $n$ parts.
Then the Schur function $s_\lambda$ is the determinant
$$
s_\lambda = \det\bigl(h_{\lambda_i-i+j}\bigr)_{1\leq i,j\leq n},
$$
the right-hand side being independent of $n\geq\ell(\lambda)$.

This is [@FH91, (A.5)].
:::
