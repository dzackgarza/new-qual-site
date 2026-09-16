---
schema: qual/card@1
id: PR-UQ3XJ
kind: proposition
title: Order of $\GL_n(\FF_q)$
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
Let $q$ be a prime power and $n\geq1$.
Then
$$
\abs{\GL_n(\FF_q)} = \prod_{k=0}^{n-1}\qty{q^n - q^k} = (q^n-1)(q^n-q)\cdots(q^n - q^{n-1}).
$$
:::

::: {.proof}
A matrix in $M_n(\FF_q)$ is invertible if and only if its columns form a basis of $\FF_q^n$ [@DF04, sec. 11.1], so we count ordered bases.
If the first $k$ columns are linearly independent, the $(k+1)$-st column can be any vector outside their span, a subspace with $q^k$ elements, so there are $q^n-q^k$ choices.
Multiplying over $k=0,\ldots,n-1$ gives the formula.
:::
