---
schema: qual/card@1
id: P-UCLAB05F-06
kind: problem
title: Polynomial images and squares of real symmetric matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
(a) Prove that if $P$ is a real-coefficient polynomial and $A$ is a real symmetric matrix, then the eigenvalues of $P(A)$ are exactly the numbers $P(\lambda)$, where $\lambda$ is an eigenvalue of $A$.

(b) Use part (a) to prove that if $A$ is a real symmetric matrix, then $A^2$ is nonnegative definite.

(c) Check part (b) by verifying directly that $\det(A^2)$ and $\operatorname{trace}(A^2)$ are nonnegative when $A$ is real symmetric.
:::

::: {.solution}

Let
$$
P(X)=c_0+c_1X+\cdots+c_mX^m.
$$

::: pf

::: {.pf-step #s1-1}

Since $A$ is real symmetric, there is an orthonormal basis
$$
v_1,\ldots,v_n
$$
of $\RR^n$ consisting of eigenvectors of $A$.


::: pf-proof

This is the spectral theorem for real symmetric matrices. Write
$$
Av_i=\lambda_i v_i
$$
with $\lambda_i\in\RR$.

:::

:::

::: {.pf-step #s1-2}

For every $i$,
$$
P(A)v_i=P(\lambda_i)v_i.
$$


::: pf-proof

Since
$$
A^kv_i=\lambda_i^k v_i
$$
for every $k\ge0$,
$$
\begin{aligned}
P(A)v_i
&=
\sum_{k=0}^m c_kA^kv_i\\
&=
\sum_{k=0}^m c_k\lambda_i^kv_i\\
&=
P(\lambda_i)v_i.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The eigenvalues of $P(A)$ are exactly
$$
\boxed{P(\lambda_1),\ldots,P(\lambda_n)},
$$
counted with multiplicity.


::: pf-proof

By step [](#s1-2){.pf-ref}, every basis vector $v_i$ is an eigenvector of $P(A)$ with eigenvalue $P(\lambda_i)$. Since the $v_i$ form a basis by step [](#s1-1){.pf-ref}, the matrix of $P(A)$ in this basis is diagonal with diagonal entries
$$
P(\lambda_1),\ldots,P(\lambda_n).
$$
Therefore these are precisely all eigenvalues of $P(A)$.

:::

:::

::: {.pf-step #s1-4}

Every eigenvalue of $A^2$ is nonnegative.


::: pf-proof

Apply step [](#s1-3){.pf-ref} to
$$
P(X)=X^2.
$$
The eigenvalues of $A^2$ are
$$
\lambda_1^2,\ldots,\lambda_n^2,
$$
all of which are nonnegative.

:::

:::

::: {.pf-step #s1-5}

The matrix $A^2$ is nonnegative definite.


::: pf-proof

The matrix $A^2$ is symmetric because
$$
(A^2)^t=(A^t)^2=A^2.
$$
Using the orthonormal eigenbasis from step [](#s1-1){.pf-ref}, write
$$
v=\sum_{i=1}^n c_iv_i.
$$
Then
$$
v\mathbin{\cdot}A^2v
=
\sum_{i=1}^n \lambda_i^2c_i^2
\ge0
$$
by step [](#s1-4){.pf-ref}. Hence $A^2$ is nonnegative definite.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{\det(A^2)=(\det A)^2\ge0}.
$$


::: pf-proof

Multiplicativity of determinant gives
$$
\det(A^2)=\det(A)\det(A)=(\det A)^2.
$$
The square of a real number is nonnegative.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\boxed{\operatorname{trace}(A^2)=\sum_{i,j=1}^n a_{ij}^2\ge0}.
$$


::: pf-proof

The $i$th diagonal entry of $A^2$ is
$$
(A^2)_{ii}
=
\sum_{j=1}^n a_{ij}a_{ji}.
$$
Since $A$ is symmetric,
$$
a_{ji}=a_{ij}.
$$
Therefore
$$
\operatorname{trace}(A^2)
=
\sum_{i=1}^n\sum_{j=1}^n a_{ij}a_{ji}
=
\sum_{i,j=1}^n a_{ij}^2
\ge0.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} prove part (b), and steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} verify the two nonnegativity statements in part (c).

:::

:::

:::
