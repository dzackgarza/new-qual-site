---
schema: qual/card@1
id: P-BERK85SU-03
kind: problem
title: Polar decomposition of a nonsingular real matrix
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    S=A^T A is symmetric positive definite. The spectral theorem gives its
    unique positive-definite symmetric square root B. Then Q=AB^{-1} is
    orthogonal and A=QB. Any other factorization A=QC has C^2=A^T A,
    so uniqueness of the positive square root forces C=B and then Q=AB^{-1}.
---

::: {.problem}
Let $A$ be a nonsingular real $n\times n$ matrix. Prove that there exist a unique orthogonal matrix $Q$ and a unique positive-definite symmetric matrix $B$ such that
\[
A=QB.
\]
:::

::: {.solution}
Set
$$
S=A^TA.
$$

<1>1. The matrix $S$ is symmetric positive definite.

::: {.proof}
Symmetry is immediate:
$$
S^T=(A^TA)^T=A^TA=S.
$$
For every nonzero vector $v\in\RR^n$,
$$
v^TSv
=
v^TA^TAv
=
\norm{Av}^2
>
0,
$$
because $A$ is nonsingular and hence $Av\neq0$.
:::

<1>2. There exists a positive-definite symmetric matrix $B$ such
that
$$
B^2=S.
$$

::: {.proof}
By the real spectral theorem, there is an orthogonal matrix $U$ and
positive real numbers $\lambda_1,\ldots,\lambda_n$ such that
$$
S
=
U
\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
U^T.
$$
Define
$$
B
=
U
\operatorname{diag}
(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})
U^T.
$$
Then $B$ is symmetric, all of its eigenvalues are positive, and
direct multiplication gives $B^2=S$.
:::

<1>3. The positive-definite symmetric square root of $S$ is unique.

::: {.proof}
Suppose $C$ is positive definite and symmetric with
$$
C^2=S.
$$
Then $C$ commutes with $S$, because
$$
CS
=
CC^2
=
C^3
=
C^2C
=
SC.
$$
Therefore $C$ preserves every eigenspace $E_\lambda$ of $S$.

On $E_\lambda$ one has
$$
C^2=\lambda I.
$$
The restriction of $C$ to $E_\lambda$ is again symmetric and
positive definite, so it has an orthonormal eigenbasis with positive
eigenvalues $\mu$. Each such eigenvalue satisfies
$$
\mu^2=\lambda,
$$
hence $\mu=\sqrt\lambda$. Thus
$$
C|_{E_\lambda}=\sqrt{\lambda} I.
$$
Step <1>2 shows that $B$ acts in exactly the same way on every
eigenspace of $S$. Since those eigenspaces span $\RR^n$, one has
$C=B$.
:::

<1>4. Define
$$
Q=AB^{-1}.
$$
Then $Q$ is orthogonal.

::: {.proof}
The matrix $B$ is positive definite and therefore invertible. Since
$B$ is symmetric and $B^2=A^TA$,
$$
\begin{aligned}
Q^TQ
&=
B^{-1}A^TAB^{-1}\\
&=
B^{-1}B^2B^{-1}\\
&=
I.
\end{aligned}
$$
Hence $Q$ is orthogonal.
:::

<1>5. One has
$$
\boxed{A=QB}
$$
with $Q$ orthogonal and $B$ positive-definite symmetric.

::: {.proof}
By step <1>4,
$$
QB
=
AB^{-1}B
=
A.
$$
The required properties of $Q$ and $B$ were established in steps
<1>2 and <1>4.
:::

<1>6. This factorization is unique.

::: {.proof}
Suppose also that
$$
A=Q_1B_1,
$$
where $Q_1$ is orthogonal and $B_1$ is positive definite and
symmetric. Then
$$
A^TA
=
B_1Q_1^TQ_1B_1
=
B_1^2.
$$
Thus $B_1$ is a positive-definite symmetric square root of $S=A^TA$.
By step <1>3,
$$
B_1=B.
$$
Since $B$ is invertible,
$$
Q_1
=
AB^{-1}
=
Q.
$$
So both factors are unique.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 proves existence, and step <1>6 proves uniqueness.
:::
:::
