---
schema: qual/card@1
id: P-BKF03-3B
kind: problem
title: The bound $\abs{\det(A+B)}\le2^n$ for unitary matrices
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
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
Let $A$ and $B$ be $n \times n$ complex unitary matrices.
Prove that $\abs{\det(A + B)} \leq 2^{n}$.
:::


::: {.solution}

::: pf

::: {.pf-step #C-unitary-factorization}
The matrix
$$
C:=A^{-1}B
$$
is unitary, and
$$
A+B=A(I+C).
$$

::: pf-proof
Because $A$ and $B$ are unitary, $A^{-1}=A^*$ and
$$
C^*C=(A^{-1}B)^*(A^{-1}B)=B^*(A^{-1})^*A^{-1}B.
$$
Since $(A^{-1})^*=A$ and $AA^{-1}=I$, this becomes
$$
C^*C=B^*B=I.
$$
Thus $C$ is unitary.
The factorization $A+B=A(I+A^{-1}B)=A(I+C)$ is immediate.
:::

:::

::: {.pf-step #det-A-modulus-one}
One has $\abs{\det A}=1$.

::: pf-proof
From $A^*A=I$, taking determinants gives
$$
\overline{\det A}\,\det A=1.
$$
Hence $\abs{\det A}^2=1$, so $\abs{\det A}=1$.
:::

:::

::: {.pf-step #eigenvalues-modulus-one}
If $\lambda_1,\dots,\lambda_n$ are the eigenvalues of $C$, counted with algebraic multiplicity, then $\abs{\lambda_j}=1$ for every $j$.

::: pf-proof
A unitary matrix is normal, hence unitarily diagonalizable.
Equivalently, if $Cv=\lambda v$ with $v\ne0$, then
$$
\norm{v}=\norm{Cv}=\norm{\lambda v}=\abs{\lambda}\,\norm{v},
$$
so $\abs{\lambda}=1$.
:::

:::

::: {.pf-step #final-bound}
Therefore
$$
\abs{\det(A+B)}\le2^n.
$$

::: pf-proof
By steps [](#C-unitary-factorization){.pf-ref} and [](#det-A-modulus-one){.pf-ref},
$$
\abs{\det(A+B)}=\abs{\det A}\,\abs{\det(I+C)}=\abs{\det(I+C)}.
$$
The eigenvalues of $I+C$ are $1+\lambda_1,\dots,1+\lambda_n$, so
$$
\abs{\det(I+C)}=\prod_{j=1}^n\abs{1+\lambda_j}.
$$
By step [](#eigenvalues-modulus-one){.pf-ref} and the triangle inequality,
$$
\abs{1+\lambda_j}\le1+\abs{\lambda_j}=2.
$$
Thus
$$
\boxed{\abs{\det(A+B)}\le2^n}.
$$
:::

:::

:::

:::

