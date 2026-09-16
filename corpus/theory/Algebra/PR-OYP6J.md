---
schema: qual/card@1
id: PR-OYP6J
kind: proposition
title: Order of $\GL_n(\FF_p)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Bases
relations: []
review: draft
---

::: {.proposition}
Let $p$ be a prime and $n\geq 1$.
Then
$$
\abs{\GL_n(\FF_p)} = (p^n-1)(p^n-p)(p^n-p^2)\cdots(p^n - p^{n-1}) = \prod_{k=0}^{n-1}(p^n-p^k).
$$
:::

::: {.proof}
A matrix in $M_n(\FF_p)$ is invertible if and only if its columns $v_1,\ldots,v_n$ form a basis of $\FF_p^n$, so $\abs{\GL_n(\FF_p)}$ is the number of ordered bases of $\FF_p^n$.
We count them column by column.
For $0\leq k\leq n-1$, suppose $v_1,\ldots,v_k$ are linearly independent.
Then $v_1,\ldots,v_{k+1}$ are linearly independent if and only if $v_{k+1}\notin\spanof(v_1,\ldots,v_k)$, and this span has $p^k$ elements, so there are $p^n-p^k$ choices for $v_{k+1}$.
Multiplying over $k=0,\ldots,n-1$ gives the formula.
:::
