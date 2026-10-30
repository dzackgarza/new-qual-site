---
schema: qual/card@1
id: P-UGAP09S-06
kind: problem
title: A self-adjoint matrix with spectrum $\{0,1\}$ is idempotent
classification:
  areas: [prelim]
  topics:
  - Spectral Theorem
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Suppose $A\in M_n(\RR)$ is self-adjoint and its only eigenvalues are $0$ and $1$. Prove that
$$
A^2=A.
$$
Carefully state any major theorem used in the argument.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The real spectral theorem states that every self-adjoint matrix
$A\in M_n(\RR)$ is orthogonally diagonalizable: there is an orthogonal
matrix $Q$ and a real diagonal matrix $D$ such that
$$
A=QDQ^T,
$$
and the diagonal entries of $D$ are the eigenvalues of $A$.


::: pf-proof

This is the finite-dimensional spectral theorem for real self-adjoint
operators.

:::

:::

::: {.pf-step #s1-2}

Under the hypotheses of the problem,
$$
D^2=D.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, every diagonal entry of $D$ is an eigenvalue of $A$. By
hypothesis each such entry is either $0$ or $1$. Since
$$
0^2=0
\qquad\text{and}\qquad
1^2=1,
$$
squaring $D$ leaves every diagonal entry unchanged.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{A^2=A}.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref} and orthogonality,
$$
\begin{aligned}
A^2
&=(QDQ^T)(QDQ^T)\\
&=QD(Q^TQ)DQ^T\\
&=QD^2Q^T.
\end{aligned}
$$
By step [](#s1-2){.pf-ref}, $D^2=D$, so
$$
A^2=QDQ^T=A.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
