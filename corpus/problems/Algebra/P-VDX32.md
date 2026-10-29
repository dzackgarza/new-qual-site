---
schema: qual/card@1
id: P-VDX32
kind: problem
title: Matrix algebra
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Matrices
relations: []
review: draft
---

::: {.problem}
What is a matrix algebra?
:::

::: {.solution}
Let $k$ be a commutative ring, usually a field, and let $M_n(k)$ be the set of $n\times n$ matrices with entries in $k$.

::: pf

::: pf-step
$M_n(k)$ is an associative unital $k$-algebra, with entrywise addition and scalar multiplication, matrix multiplication, and identity $I_n$.

::: pf-proof
Matrix multiplication is associative, $k$-bilinear, and has $I_n$ as a two-sided identity.
:::

:::

::: pf-step
As a $k$-module $M_n(k)$ is free of rank $n^2$, with basis the matrix units $E_{ij}$, $1\le i,j\le n$, which multiply by $E_{ij}E_{pq}=\delta_{jp}E_{iq}$.

::: pf-proof
Here $E_{ij}$ has a single $1$ in position $(i,j)$, and every matrix $A$ equals $\sum_{i,j}a_{ij}E_{ij}$ uniquely.
The $(r,s)$ entry of $E_{ij}E_{pq}$ is $\sum_t\delta_{ri}\delta_{tj}\delta_{tp}\delta_{sq}=\delta_{jp}\delta_{ri}\delta_{sq}$, the $(r,s)$ entry of $\delta_{jp}E_{iq}$.
:::

:::

::: pf-qed
A matrix algebra over $k$ is the full matrix algebra $M_n(k)$; more generally the term can mean a $k$-subalgebra of some $M_n(k)$, when the context makes that usage clear.
:::

:::
:::
