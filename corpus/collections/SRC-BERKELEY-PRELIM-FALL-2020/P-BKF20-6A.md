---
schema: qual/card@1
id: P-BKF20-6A
kind: problem
title: Cholesky factorization and a related similarity
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
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 solution: the spectral theorem
    gives a symmetric positive definite square root B, whose sign-normalized QR
    factorization yields R^T R=A; then RR^T is similar to A.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked construction and invertibility of the positive square root, the
    positive-diagonal QR convention, the Cholesky identity, and the explicit
    similarity RR^T=RAR^{-1}.
---

::: {.problem}
Let $A$ be a real symmetric positive definite $n\times n$ matrix.

(a) Show there is an upper triangular matrix $R$ with positive diagonal entries such that $R^TR=A$.

(b) Show that $RR^T$ has the same eigenvalues as $A$.
:::

::: {.solution}
<1>1. There is a real symmetric positive definite matrix $B$ such that
$$
B^2=A.
$$

::: {.proof}
By the spectral theorem, there is an orthogonal matrix $U$ and positive
numbers
$$
\lambda_1,\ldots,\lambda_n
$$
such that
$$
A
=
U
\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
U^T.
$$
Define
$$
B
\coloneqq
U
\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})
U^T.
$$
Then $B$ is real and symmetric, all its eigenvalues are positive, and
$$
B^2
=
U
\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
U^T
=
A.
$$
:::

<1>2. The matrix $B$ has a QR factorization
$$
B=QR
$$
in which $Q$ is orthogonal and $R$ is upper triangular with positive
diagonal entries.

::: {.proof}
The matrix $B$ is invertible because its eigenvalues in step <1>1 are
positive. Applying Gram--Schmidt to its linearly independent columns
gives a QR factorization with nonzero diagonal entries in $R$.
Multiplying a column of $Q$ and the corresponding row of $R$ by $-1$
when necessary makes every diagonal entry of $R$ positive without
changing the product $QR$.
:::

<1>3. The matrix $R$ from step <1>2 satisfies
$$
\boxed{R^TR=A}.
$$

::: {.proof}
Since $B=QR$ and $Q^TQ=I$,
$$
\begin{aligned}
R^TR
&=
R^TQ^TQR\\
&=
B^TB.
\end{aligned}
$$
By step <1>1, $B^T=B$ and $B^2=A$. Hence
$$
R^TR=B^2=A.
$$
This proves part (a).
:::

<1>4. The matrix $R$ is invertible and
$$
R^T=AR^{-1}.
$$

::: {.proof}
By step <1>2, $R$ is triangular with positive, hence nonzero, diagonal
entries, so it is invertible. From step <1>3,
$$
R^TR=A.
$$
Multiplying on the right by $R^{-1}$ gives
$$
R^T=AR^{-1}.
$$
:::

<1>5. One has
$$
RR^T=RAR^{-1}.
$$

::: {.proof}
Multiply the identity in step <1>4 on the left by $R$:
$$
RR^T
=
R(AR^{-1})
=
RAR^{-1}.
$$
:::

<1>6. The matrices $RR^T$ and $A$ have the same eigenvalues, with the
same algebraic multiplicities.

::: {.proof}
Step <1>5 says exactly that $RR^T$ is similar to $A$. Similar matrices
have the same characteristic polynomial and therefore the same
eigenvalues with the same algebraic multiplicities. This proves part
(b).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>6 proves part (b).
:::
:::
