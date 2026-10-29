---
schema: qual/card@1
id: P-UCLAB08S-10
kind: problem
title: A matrix commuting with simple spectrum is diagonalizable
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $A\in M_n(\CC)$ have $n$ distinct eigenvalues.
Prove that if $B\in M_n(\CC)$ satisfies $AB=BA$, then $B$ is diagonalizable.
:::

::: {.solution}

Let
\[
\lambda_1,\ldots,\lambda_n
\]
be the distinct eigenvalues of $A$, and choose corresponding nonzero eigenvectors
\[
v_1,\ldots,v_n.
\]

::: pf

::: {.pf-step #s1-1}

The vectors
\[
v_1,\ldots,v_n
\]
are linearly independent.


::: pf-proof

Eigenvectors belonging to distinct eigenvalues are linearly independent.
For completeness, suppose
\[
\sum_{j=1}^n c_jv_j=0.
\]
Fix $k$ and apply
\[
\prod_{j\ne k}(A-\lambda_jI).
\]
Every term except the $k$th is annihilated, giving
\[
c_k
\prod_{j\ne k}(\lambda_k-\lambda_j)
v_k
=0.
\]
The scalar product is nonzero because the eigenvalues are distinct and
\[
v_k\ne0.
\]
Hence
\[
c_k=0.
\]
Since $k$ was arbitrary, all coefficients vanish.

:::

:::

::: {.pf-step #s1-2}

The list
\[
v_1,\ldots,v_n
\]
is a basis of $\CC^n$.


::: pf-proof

By step [](#s1-1){.pf-ref}, it is a linearly independent list of $n$ vectors in the $n$-dimensional space $\CC^n$.
Therefore it is a basis.

:::

:::

::: {.pf-step #s1-3}

Each eigenspace
\[
E_{\lambda_j}
=
\ker(A-\lambda_jI)
\]
is one-dimensional:
\[
E_{\lambda_j}
=
\operatorname{span}\{v_j\}.
\]


::: pf-proof

The direct sum of all eigenspaces contains the $n$ linearly independent vectors from step [](#s1-1){.pf-ref} and therefore has dimension at least $n$.
Since the ambient space has dimension $n$, the sum of the dimensions of the eigenspaces is exactly $n$.
There are $n$ distinct eigenvalues, and every eigenspace has dimension at least $1$.
Hence every eigenspace has dimension exactly $1$.

:::

:::

::: {.pf-step #s1-4}

Every eigenspace of $A$ is invariant under $B$.


::: pf-proof

Let
\[
v\in E_{\lambda_j}.
\]
Then
\[
Av=\lambda_jv.
\]
Using
\[
AB=BA,
\]
one gets
\[
A(Bv)
=
B(Av)
=
B(\lambda_jv)
=
\lambda_jBv.
\]
Therefore
\[
Bv\in E_{\lambda_j}.
\]

:::

:::

::: {.pf-step #s1-5}

For each $j$, there exists
\[
\mu_j\in\CC
\]
such that
\[
\boxed{Bv_j=\mu_jv_j}.
\]


::: pf-proof

By step [](#s1-4){.pf-ref},
\[
Bv_j\in E_{\lambda_j}.
\]
By step [](#s1-3){.pf-ref},
\[
E_{\lambda_j}
=
\operatorname{span}\{v_j\}.
\]
Therefore
\[
Bv_j
\]
is a scalar multiple of $v_j$.

:::

:::

::: {.pf-step #s1-6}

The basis
\[
v_1,\ldots,v_n
\]
consists of eigenvectors of $B$.


::: pf-proof

This is exactly the content of step [](#s1-5){.pf-ref}, together with the fact from step [](#s1-2){.pf-ref} that the vectors form a basis.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{B\text{ is diagonalizable}.}
\]


::: pf-proof

A linear operator is diagonalizable precisely when the ambient vector space has a basis consisting of eigenvectors.
Step [](#s1-6){.pf-ref} supplies such a basis for $B$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
