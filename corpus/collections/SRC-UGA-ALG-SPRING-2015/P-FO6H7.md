---
schema: qual/card@1
id: P-FO6H7
kind: problem
title: Commuting diagonalizable operators are simultaneously diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $F$ be a field and $V$ a finite dimensional $F\dash$vector space, and let $A, B: V\to V$ be commuting $F\dash$linear maps.
Suppose there is a basis $\mcb_1$ with respect to which $A$ is diagonalizable and a basis $\mcb_2$ with respect to which $B$ is diagonalizable.

Prove that there is a basis $\mcb_3$ with respect to which $A$ and $B$ are both diagonalizable.
:::

::: {.solution}
Because $A$ is diagonalizable,
\[
V=\bigoplus_{\lambda}E_\lambda(A),
\qquad
E_\lambda(A)=\ker(A-\lambda I).
\]
Since $AB=BA$, every eigenspace $E_\lambda(A)$ is $B$-invariant: if $v\in E_\lambda(A)$, then
\[
A(Bv)=B(Av)=B(\lambda v)=\lambda Bv.
\]

Because $B$ is diagonalizable, its minimal polynomial is a product of distinct linear factors. The minimal polynomial of the restriction $B|_{E_\lambda(A)}$ divides the minimal polynomial of $B$, so it too is a product of distinct linear factors. Hence each restriction $B|_{E_\lambda(A)}$ is diagonalizable.

For every $\lambda$, choose a basis of $E_\lambda(A)$ consisting of eigenvectors of $B$. The union of these bases is a basis of $V$ because the eigenspaces of $A$ form a direct sum. Every vector in this union is simultaneously an eigenvector of $A$ and $B$. Therefore, with respect to this basis, both $A$ and $B$ are diagonal.
:::
