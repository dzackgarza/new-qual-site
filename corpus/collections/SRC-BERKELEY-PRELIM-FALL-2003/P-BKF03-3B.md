---
schema: qual/card@1
id: P-BKF03-3B
kind: problem
title: The bound $\lvert\det(A+B)\rvert\le2^n$ for unitary matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified reduction to I+C with C unitary and the eigenvalue product bound.
---

::: {.problem}
Let A and B be $n \times n$ complex unitary matrices.
Prove that $| \operatorname* { d e t } ( A + B ) | \leq 2 ^ { n }$
:::


::: {.solution}
<1>1. The matrix
\[
C:=A^{-1}B
\]
is unitary, and
\[
A+B=A(I+C).
\]
::: {.proof}
Because $A$ and $B$ are unitary, $A^{-1}=A^*$ and
\[
C^*C=(A^{-1}B)^*(A^{-1}B)=B^*(A^{-1})^*A^{-1}B.
\]
Since $(A^{-1})^*=A$ and $AA^{-1}=I$, this becomes
\[
C^*C=B^*B=I.
\]
Thus $C$ is unitary.
The factorization $A+B=A(I+A^{-1}B)=A(I+C)$ is immediate.
:::

<1>2. One has $|\det A|=1$.
::: {.proof}
From $A^*A=I$, taking determinants gives
\[
\overline{\det A}\,\det A=1.
\]
Hence $|\det A|^2=1$, so $|\det A|=1$.
:::

<1>3. If $\lambda_1,\dots,\lambda_n$ are the eigenvalues of $C$, counted with algebraic multiplicity, then $|\lambda_j|=1$ for every $j$.
::: {.proof}
A unitary matrix is normal, hence unitarily diagonalizable.
Equivalently, if $Cv=\lambda v$ with $v\ne0$, then
\[
\|v\|=\|Cv\|=\|\lambda v\|=|\lambda|\,\|v\|,
\]
so $|\lambda|=1$.
:::

<1>4. Therefore
\[
|\det(A+B)|\le2^n.
\]
::: {.proof}
By <1>1 and <1>2,
\[
|\det(A+B)|=|\det A|\,|\det(I+C)|=|\det(I+C)|.
\]
The eigenvalues of $I+C$ are $1+\lambda_1,\dots,1+\lambda_n$, so
\[
|\det(I+C)|=\prod_{j=1}^n|1+\lambda_j|.
\]
By <1>3 and the triangle inequality,
\[
|1+\lambda_j|\le1+|\lambda_j|=2.
\]
Thus
\[
\boxed{|\det(A+B)|\le2^n}.
\]
:::
:::

