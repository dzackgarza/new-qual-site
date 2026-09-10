---
schema: qual/card@1
id: P-DB3EP
kind: problem
title: Equivalence of $A\mathbf{x}=\mathbf{b}$ with the corresponding system of linear
  equations
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Rank and Nullity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $A=(a_{ij})\in F^{m\times n}$, let $\mathbf x=(x_1,\dots,x_n)^t\in F^n$, and let $\mathbf b=(b_1,\dots,b_m)^t\in F^m$.
Prove that the matrix equation
\[
A\mathbf x=\mathbf b
\]
is equivalent to the system of linear equations
\[
a_{i1}x_1+\cdots+a_{in}x_n=b_i,
\qquad i=1,\dots,m.
\]
:::


::: {.solution}
Let $\mathbf a_i=(a_{i1},\dots,a_{in})$ be the $i$th row of $A$.

<1>1. The $i$th coordinate of $A\mathbf x$ is
\[
\sum_{j=1}^n a_{ij}x_j.
\]
::: {.proof}
This is the definition of matrix-vector multiplication: the $i$th coordinate is the dot product of the $i$th row of $A$ with the column vector $\mathbf x$.
:::

<1>2. If $A\mathbf x=\mathbf b$, then $x_1,\dots,x_n$ satisfy the displayed system.
::: {.proof}
Equality of the two vectors implies equality of their $i$th coordinates for every $i$. By <1>1,
\[
\sum_{j=1}^n a_{ij}x_j=b_i
\]
for each $i=1,\dots,m$.
:::

<1>3. Conversely, if $x_1,\dots,x_n$ satisfy the displayed system, then $A\mathbf x=\mathbf b$.
::: {.proof}
By assumption, for every $i$ the $i$th coordinate of $A\mathbf x$ equals $b_i$. Hence the vectors $A\mathbf x$ and $\mathbf b$ have equal coordinates, so they are equal.
:::
:::
