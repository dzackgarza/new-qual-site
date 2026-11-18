---
schema: qual/card@1
id: E-HK-XY48
kind: problem
title: Inverse of a $4 \times 4$ upper-triangular matrix
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze Exercise 1.6.5.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise and no printed copy of
    Hoffman and Kunze is retained, so the card cites it by section and number, read from the
    collection index because the card id is coded: it is §1.6 Exercise 5. The product AB was
    checked both by hand and numerically. Each step re-read: the determinant is the product 24 of
    the diagonal entries, so A is invertible; the diagonal entries of AB are 1; the superdiagonal
    entries cancel by the three displayed computations; the remaining upper entries (1,3), (1,4)
    and (2,4) are computed explicitly; and the lower entries vanish because both factors are upper
    triangular. A justification in my first draft, that columns of B have nonzeros only in two rows
    and hence that every higher entry vanishes, was not a valid argument — the two rows can both be
    above the diagonal entry in question — and is replaced by the explicit computations. Not
    claimed: any factorisation of A or a general inversion algorithm.
---

::: {.exercise}
Discover whether

$$
A = \left[ \begin{array}{c c c c} 1 & 2 & 3 & 4 \\ 0 & 2 & 3 & 4 \\ 0 & 0 & 3 & 4 \\ 0 & 0 & 0 & 4 \end{array} \right]
$$

is invertible, and find $A^{-1}$ if it exists.
:::


::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and no printed copy of Hoffman and Kunze is retained in `tmp/sources`, so the exercise is cited by section and number, read from the collection index because the card id is coded: it is §1.6 Exercise 5.

::: pf

::: {.pf-step #triangular}
$A$ is upper triangular with diagonal entries $1,2,3,4$, so $\det A=24\ne0$ and $A$ is invertible.

::: pf-proof
The determinant of an upper triangular matrix is the product of its diagonal entries, here $1\cdot2\cdot3\cdot4=24$; a square matrix is invertible exactly when its determinant is nonzero.
:::

:::

::: {.pf-step #candidate}
Let
$$
B=\begin{bmatrix}1&-1&0&0\\0&\tfrac12&-\tfrac12&0\\0&0&\tfrac13&-\tfrac13\\0&0&0&\tfrac14\end{bmatrix}.
$$

::: pf-proof
This is a definition; the entries are chosen so that each diagonal entry of $A$ is inverted and each superdiagonal entry cancels the one above it.
:::

:::

::: {.pf-step #product}
$AB=I_4$.

:::: pf-proof

::: {.pf-step #diagonal}
The diagonal entries of $AB$ are $1$.

::: pf-proof
The $(i,i)$ entry of $AB$ is the $i$th row of $A$ against the $i$th column of $B$, and each of those columns has its only nonzero entry above the diagonal position except the $i$th, so the product is $A_{ii}B_{ii}=1$ for $i=1,2,3,4$.
:::

:::

::: {.pf-step #superdiagonal}
The first superdiagonal entries of $AB$ are $0$, and every entry further above the diagonal is $0$.

::: pf-proof
The $(1,2)$ entry is $1\cdot(-1)+2\cdot\tfrac12=0$; the $(2,3)$ entry is $2\cdot(-\tfrac12)+3\cdot\tfrac13=0$; the $(3,4)$ entry is $3\cdot(-\tfrac13)+4\cdot\tfrac14=0$. The remaining upper entries are computed from the same rows and columns: the $(1,3)$ entry is $2\cdot(-\tfrac12)+3\cdot\tfrac13=0$, the $(1,4)$ entry is $3\cdot(-\tfrac13)+4\cdot\tfrac14=0$, and the $(2,4)$ entry is $3\cdot(-\tfrac13)+4\cdot\tfrac14=0$. Each upper entry is a sum of at most two terms, because the $j$th column of $B$ has nonzeros only in rows $j-1$ and $j$, and the three values above together with the superdiagonal computations cover them all.
:::

:::

::: {.pf-step #below}
The entries of $AB$ below the diagonal are $0$.

::: pf-proof
$A$ is upper triangular and $B$ is upper triangular, so $AB$ is upper triangular: the $(i,j)$ entry with $i>j$ is a sum of products $A_{ik}B_{kj}$ where $k\ge i>j$ forces $B_{kj}=0$.
:::

:::

:::

:::

::: {.pf-step}
$A$ is invertible and $A^{-1}=B$.

::: pf-proof
$A$ is invertible by step [](#triangular){.pf-ref}, and $AB=I_4$ by step [](#product){.pf-ref}; a right inverse of a square matrix is its inverse, so
$$
\boxed{A^{-1}=\begin{bmatrix}1&-1&0&0\\0&\tfrac12&-\tfrac12&0\\0&0&\tfrac13&-\tfrac13\\0&0&0&\tfrac14\end{bmatrix}.}
$$
:::

:::

:::
:::
