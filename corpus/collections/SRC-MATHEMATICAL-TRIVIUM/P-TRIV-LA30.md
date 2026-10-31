---
schema: qual/card@1
id: P-TRIV-LA30
kind: problem
title: Number of independent real parameters of a unitary matrix
classification:
  areas: [prelim]
  topics:
  - Unitary Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 30, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let U be $n \times n$ unitary matrix.
Calculate the number of independent elements of $U .$
:::

::: {.solution}

Interpret “independent elements” as independent real parameters.

::: pf

::: pf-step

The first column of a unitary matrix has
$$
2n-1
$$
independent real parameters.


::: pf-proof

A column of a complex $n\times n$ matrix lies in $\CC^n$, which has
real dimension $2n$. Unitarity requires the column to have norm $1$, imposing
one real equation. Thus the first column lies on the sphere
$$
S^{2n-1}
$$
and has $2n-1$ real parameters.

:::

:::

::: {.pf-step #s1-2}

Once the first $k-1$ orthonormal columns are fixed, the $k$th column has
$$
2(n-k+1)-1
$$
independent real parameters.


::: pf-proof

The orthogonal complement of the first $k-1$ columns is a complex vector space
of complex dimension
$$
n-k+1.
$$
Its underlying real dimension is
$$
2(n-k+1).
$$
The $k$th column must be a unit vector in this space, so it lies on a sphere of
real dimension
$$
2(n-k+1)-1.
$$

:::

:::

::: pf-step

Therefore the total number of independent real parameters is
$$
\sum_{k=1}^{n}
\bigl(2(n-k+1)-1\bigr).
$$


::: pf-proof

Add the independent choices from step [](#s1-2){.pf-ref} for all $n$ columns.

:::

:::

::: {.pf-step #s1-4}

This sum equals
$$
(2n-1)+(2n-3)+\cdots+3+1=n^2.
$$


::: pf-proof

The sum of the first $n$ positive odd integers is $n^2$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{n^2}
$$
independent real parameters are needed to specify an $n\times n$ unitary
matrix.


::: pf-proof

This is step [](#s1-4){.pf-ref}. Equivalently,
$$
\dim_{\RR}U(n)=n^2.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required count.

:::

:::

:::
