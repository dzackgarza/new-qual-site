---
schema: qual/card@1
id: P-BKS10-8B
kind: problem
title: A Hermitian solution of a fifth-degree matrix equation
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution. The scalar right-hand side 2 is written as 2I in the card to make the matrix equality explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the real scalar root equation and the Hermitian spectral-theorem reduction.
---

::: {.problem}
If \(A\) is Hermitian and satisfies
\[
A^5+A=2I,
\]
prove that \(A=I\).
:::

::: {.solution}
<1>1. The real equation
$$
t^5+t=2
$$
has the unique solution
$$
t=1.
$$

::: {.proof}
Set
$$
p(t)\coloneqq t^5+t-2.
$$
For every real $t$,
$$
p'(t)=5t^4+1>0.
$$
Thus $p$ is strictly increasing on $\RR$. Since
$$
p(1)=1+1-2=0,
$$
the value $1$ is its unique real zero.
:::

<1>2. Every eigenvalue of $A$ equals $1$.

::: {.proof}
Because $A$ is Hermitian, the spectral theorem gives an orthonormal basis
of eigenvectors and all eigenvalues of $A$ are real. Let $v\neq0$ be an
eigenvector with
$$
Av=\lambda v,
\qquad
\lambda\in\RR.
$$
Applying the matrix equation to $v$ gives
$$
(A^5+A)v
=
(\lambda^5+\lambda)v
=
2v.
$$
Hence
$$
\lambda^5+\lambda=2.
$$
Step <1>1 therefore gives $\lambda=1$.
:::

<1>3. One has
$$
\boxed{A=I}.
$$

::: {.proof}
By the Hermitian spectral theorem, $A$ is unitarily diagonalizable. Step
<1>2 shows that every diagonal entry in such a diagonalization is $1$.
Thus the diagonal form is $I$, and conjugating $I$ by a unitary matrix
leaves it unchanged. Hence $A=I$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
