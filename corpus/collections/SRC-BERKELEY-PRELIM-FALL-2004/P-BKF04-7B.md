---
schema: qual/card@1
id: P-BKF04-7B
kind: problem
title: Dimension of the span of commutators $AB-BA$ in $M_n(\RR)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $n\geq1$, and let $M_n(\mathbb{R})$ be the ring of $n\times n$ matrices over the field of real numbers. What is the dimension of the subspace $V$ of $M_n(\mathbb{R})$ spanned by the matrices of the form $AB-BA$ where $A,B\in M_n(\mathbb{R})$?
:::

::: {.solution}
Let $E_{ij}$ be the matrix with $1$ in the $(i,j)$ position and zeros elsewhere. Since $AB-BA$ is linear in each of $A$ and $B$, the subspace $V$ equals the span of the matrices $AB-BA$ with $A=E_{ij}$ and $B=E_{k\ell}$. We have

$$
E_{ij}E_{k\ell}-E_{k\ell}E_{ij}=
\begin{cases}
0&\text{if }j\neq k\text{ and }i\neq\ell,\\
E_{i\ell}&\text{if }j=k\text{ and }i\neq\ell,\\
-E_{kj}&\text{if }j\neq k\text{ and }i=\ell,\\
E_{ii}-E_{jj}&\text{if }j=k\text{ and }i=\ell.
\end{cases}
$$

Varying $i,j,k,\ell$ shows that $V$ is spanned by the $E_{ij}$ with $i\neq j$ together with the $E_{ii}-E_{i+1,i+1}$ for $i=1,\ldots,n-1$. These matrices are linearly independent, so $\dim V=(n^2-n)+(n-1)=\boxed{n^2-1}$. Equivalently, $V$ is the space of trace-zero matrices.
:::
