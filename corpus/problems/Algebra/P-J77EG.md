---
schema: qual/card@1
id: P-J77EG
kind: problem
title: Jordan form of the $n\times n$ all-ones matrix
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Diagonalization
  - Matrices
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
Let $F$ be a field such that $n\neq0$ in $F$, and let $M\in M_n(F)$ be the matrix whose entries are all $1$.
Find its Jordan canonical form (over a splitting field, if necessary).
:::

::: {.solution}
Let
\[
\mathbf 1=(1,\ldots,1)^t.
\]
Then
\[
M\mathbf 1=n\mathbf 1,
\]
so $n$ is an eigenvalue.

For every vector $v=(v_1,\ldots,v_n)^t$ with
\[
v_1+\cdots+v_n=0,
\]
each coordinate of $Mv$ is this same sum, so $Mv=0$. Hence the hyperplane
\[
H=\left\{v\in F^n:\sum_i v_i=0\right\}
\]
is contained in the $0$-eigenspace and has dimension $n-1$.

Because $n\neq0$ in $F$, the vector $\mathbf1$ does not lie in $H$. Therefore
\[
F^n=H\oplus F\mathbf1
\]
is a direct sum of eigenspaces. Thus $M$ is diagonalizable, with eigenvalue $0$ of multiplicity $n-1$ and eigenvalue $n$ of multiplicity $1$.

Consequently
\[
J(M)=\operatorname{diag}(\underbrace{0,\ldots,0}_{n-1},n).
\]
Equivalently, since $M^2=nM$, its minimal polynomial is $x(x-n)$.
:::
