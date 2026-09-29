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

::: pf

::: {.pf-step #s1}

There is a real symmetric positive definite matrix $B$ such that
$$
B^2=A.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

The matrix $B$ has a QR factorization
$$
B=QR
$$
in which $Q$ is orthogonal and $R$ is upper triangular with positive
diagonal entries.

::: pf-proof

The matrix $B$ is invertible because its eigenvalues in step [](#s1){.pf-ref} are
positive. Applying Gram--Schmidt to its linearly independent columns
gives a QR factorization with nonzero diagonal entries in $R$.
Multiplying a column of $Q$ and the corresponding row of $R$ by $-1$
when necessary makes every diagonal entry of $R$ positive without
changing the product $QR$.

:::

:::

::: {.pf-step #s3}

The matrix $R$ from step [](#s2){.pf-ref} satisfies
$$
\boxed{R^TR=A}.
$$

::: pf-proof

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
By step [](#s1){.pf-ref}, $B^T=B$ and $B^2=A$. Hence
$$
R^TR=B^2=A.
$$
This proves part (a).

:::

:::

::: {.pf-step #s4}

The matrix $R$ is invertible and
$$
R^T=AR^{-1}.
$$

::: pf-proof

By step [](#s2){.pf-ref}, $R$ is triangular with positive, hence nonzero, diagonal
entries, so it is invertible. From step [](#s3){.pf-ref},
$$
R^TR=A.
$$
Multiplying on the right by $R^{-1}$ gives
$$
R^T=AR^{-1}.
$$

:::

:::

::: {.pf-step #s5}

One has
$$
RR^T=RAR^{-1}.
$$

::: pf-proof

Multiply the identity in step [](#s4){.pf-ref} on the left by $R$:
$$
RR^T
=
R(AR^{-1})
=
RAR^{-1}.
$$

:::

:::

::: {.pf-step #s6}

The matrices $RR^T$ and $A$ have the same eigenvalues, with the
same algebraic multiplicities.

::: pf-proof

Step [](#s5){.pf-ref} says exactly that $RR^T$ is similar to $A$. Similar matrices
have the same characteristic polynomial and therefore the same
eigenvalues with the same algebraic multiplicities. This proves part
(b).

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (a), and step [](#s6){.pf-ref} proves part (b).

:::

:::

:::
