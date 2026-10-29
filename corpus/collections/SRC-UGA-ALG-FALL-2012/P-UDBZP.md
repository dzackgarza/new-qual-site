---
schema: qual/card@1
id: P-UDBZP
kind: problem
title: Every nondegenerate real matrix factors as $UT$ with $U$ orthogonal and $T$
  upper triangular
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Inner Product Spaces
  - Bases
relations: []
review: draft
---

::: {.problem}
Prove that any nondegenerate matrix $X\in M_n(\RR)$ can be written as $X = UT$ where $U$ is orthogonal and $T$ is upper triangular.
:::

::: {.solution}

Write $X=(x_1\ \cdots\ x_n)$, where $x_j\in\RR^n$.

::: pf

::: {.pf-step #s1-1}

There is an orthonormal basis $u_1,\ldots,u_n$ such that
$$
\operatorname{span}(u_1,\ldots,u_j)=
\operatorname{span}(x_1,\ldots,x_j)
\quad(1\leq j\leq n).
$$


::: pf-proof

Nondegeneracy of $X$ means its columns are linearly independent. Apply Gram--Schmidt in the given column order. Because no step produces zero, the resulting orthonormal vectors have the same successive spans as the original columns.

:::

:::

::: {.pf-step #s1-2}

The matrix $X$ has a factorization
$$
\boxed{X=UT}
$$
with $U$ orthogonal and $T$ upper triangular.


::: pf-proof

Let $U=(u_1\ \cdots\ u_n)$. By step [](#s1-1){.pf-ref}, for each $j$ there are unique coefficients $t_{ij}\in\RR$ with $x_j=\sum_{i=1}^j t_{ij}u_i$. Set $t_{ij}=0$ for $i>j$ and define $T=(t_{ij})$. It is upper triangular, and its $j$-th column under multiplication by $U$ is $x_j$, so $UT=X$. Orthonormality gives $U^{\mathsf T}U=I_n$, hence $U$ is orthogonal.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} establishes the required factorization.

:::

:::

:::
