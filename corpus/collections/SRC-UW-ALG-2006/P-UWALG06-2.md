---
schema: qual/card@1
id: P-UWALG06-2
kind: problem
title: Eigenvalues of a matrix with $A(A^c)^T=I_n$ satisfy $\lambda c(\lambda)=1$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Eigenvalues
relations: []
review: draft
---

::: {.problem}
Let $c$ be an automorphism of order 1 or 2 of a field $F$.
Suppose that $c$ has the property that for any finite set $\{a_j\}_{j\in J}$ of nonzero elements of $F$, $\sum_{j\in J}a_jc(a_j)$ is nonzero.
For any $n\times n$-matrix $A=(a_{ij})$ with entries in $F$, let $A^c=(c(a_{ij}))$.
The $n\times n$ identity matrix is denoted by $I_n$.

Show that if $A$ has the property that $A(A^c)^T=I_n$, then every eigenvalue $\lambda\in F$ for $A$ satisfies the equation $\lambda c(\lambda)=1$.

(Remark: This result implies the familiar facts that the eigenvalues of an orthogonal matrix over the field of real numbers are in the set $\{\pm1\}$ and that the eigenvalues of a unitary matrix over the complex numbers have absolute value 1. One takes $c$ to be the identity map in the first case, complex conjugation in the second.)
:::
