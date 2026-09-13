---
schema: qual/card@1
id: P-BKF03-3B
kind: problem
title: Berkeley Fall 2003 prelim problem 3B
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
\n\n::: {.solution}\n<1>1. The matrix\n\[\nC:=A^{-1}B\n\]\nis unitary, and\n\[\nA+B=A(I+C).\n\]\n::: {.proof}\nBecause $A$ and $B$ are unitary, $A^{-1}=A^*$ and\n\[\nC^*C=(A^{-1}B)^*(A^{-1}B)=B^*(A^{-1})^*A^{-1}B.\n\]\nSince $(A^{-1})^*=A$ and $AA^{-1}=I$, this becomes\n\[\nC^*C=B^*B=I.\n\]\nThus $C$ is unitary. The factorization $A+B=A(I+A^{-1}B)=A(I+C)$ is immediate.\n:::\n\n<1>2. One has $|\det A|=1$.\n::: {.proof}\nFrom $A^*A=I$, taking determinants gives\n\[\n\overline{\det A}\,\det A=1.\n\]\nHence $|\det A|^2=1$, so $|\det A|=1$.\n:::\n\n<1>3. If $\lambda_1,\dots,\lambda_n$ are the eigenvalues of $C$, counted with algebraic multiplicity, then $|\lambda_j|=1$ for every $j$.\n::: {.proof}\nA unitary matrix is normal, hence unitarily diagonalizable. Equivalently, if $Cv=\lambda v$ with $v\ne0$, then\n\[\n\|v\|=\|Cv\|=\|\lambda v\|=|\lambda|\,\|v\|,\n\]\nso $|\lambda|=1$.\n:::\n\n<1>4. Therefore\n\[\n|\det(A+B)|\le2^n.\n\]\n::: {.proof}\nBy <1>1 and <1>2,\n\[\n|\det(A+B)|=|\det A|\,|\det(I+C)|=|\det(I+C)|.\n\]\nThe eigenvalues of $I+C$ are $1+\lambda_1,\dots,1+\lambda_n$, so\n\[\n|\det(I+C)|=\prod_{j=1}^n|1+\lambda_j|.\n\]\nBy <1>3 and the triangle inequality,\n\[\n|1+\lambda_j|\le1+|\lambda_j|=2.\n\]\nThus\n\[\n\boxed{|\det(A+B)|\le2^n}.\n\]\n:::\n:::\n