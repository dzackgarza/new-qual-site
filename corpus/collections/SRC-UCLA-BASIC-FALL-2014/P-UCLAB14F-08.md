---
schema: qual/card@1
id: P-UCLAB14F-08
kind: problem
title: Spectrum and determinant of a constant-off-diagonal matrix
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 8. Compute the eigenvalues of the following $n\times n$ matrix:
\[
M=
\begin{pmatrix}
k&1&1&\cdots&1\\
1&k&1&\cdots&1\\
1&1&k&\cdots&1\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&1&1&\cdots&k
\end{pmatrix}.
\]
Use the eigenvalues to compute $\det(M)$.
:::

::: {.solution}

Let
\[
\mathbf 1=
\begin{pmatrix}
1\\
\vdots\\
1
\end{pmatrix}
\in\RR^n,
\]
and let
\[
J=\mathbf1\mathbf1^t
\]
be the all-ones matrix.

::: pf

::: {.pf-step #s1-1}

The matrix $M$ can be written as
\[
\boxed{M=(k-1)I+J}.
\]


::: pf-proof

The matrix $(k-1)I$ contributes $k-1$ on the diagonal and $0$ off the diagonal.
Adding $J$, which has every entry equal to $1$, produces diagonal entries
\[
(k-1)+1=k
\]
and off-diagonal entries $1$.

:::

:::

::: {.pf-step #s1-2}

One has
\[
J\mathbf1=n\mathbf1.
\]


::: pf-proof

Every row of $J$ consists of $n$ ones, so every coordinate of $J\mathbf1$ equals $n$.

:::

:::

::: {.pf-step #s1-3}

If
\[
v\in\mathbf1^\perp,
\]
then
\[
Jv=0.
\]


::: pf-proof

Since
\[
J=\mathbf1\mathbf1^t,
\]
one has
\[
Jv
=
\mathbf1(\mathbf1^tv).
\]
The condition $v\in\mathbf1^\perp$ means
\[
\mathbf1^tv=0.
\]
Therefore $Jv=0$.

:::

:::

::: {.pf-step #s1-4}

The vector $\mathbf1$ is an eigenvector of $M$ with eigenvalue
\[
\boxed{k+n-1}.
\]


::: pf-proof

Using steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
\[
\begin{aligned}
M\mathbf1
&=
(k-1)\mathbf1+J\mathbf1\\
&=
(k-1)\mathbf1+n\mathbf1\\
&=
(k+n-1)\mathbf1.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-5}

Every vector in $\mathbf1^\perp$ is an eigenvector of $M$ with eigenvalue
\[
\boxed{k-1}.
\]


::: pf-proof

If $v\in\mathbf1^\perp$, then by steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref},
\[
Mv
=(k-1)v+Jv
=(k-1)v.
\]

:::

:::

::: {.pf-step #s1-6}

The eigenvalues of $M$ are
\[
\boxed{k+n-1}
\]
with multiplicity $1$ and
\[
\boxed{k-1}
\]
with multiplicity $n-1$.


::: pf-proof

The space decomposes orthogonally as
\[
\RR^n
=
\operatorname{span}\{\mathbf1\}
\oplus
\mathbf1^\perp.
\]
The first summand has dimension $1$ and carries the eigenvalue from step [](#s1-4){.pf-ref}.
The second has dimension $n-1$ and carries the eigenvalue from step [](#s1-5){.pf-ref}.
Together these account for all $n$ dimensions.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{
\det(M)
=(k+n-1)(k-1)^{n-1}
}.
\]


::: pf-proof

The determinant of a matrix is the product of its eigenvalues counted with algebraic multiplicity.
Apply step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} give the requested spectrum and determinant.

:::

:::

:::
