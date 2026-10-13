---
schema: qual/card@1
id: P-UCLAB11S-03
kind: problem
title: Unitary diagonalization of a Hermitian operator
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Let $H$ be a Hermitian (self-adjoint) operator on a finite-dimensional inner-product space.
Show that there exists a unitary operator $U$ such that $UHU^*$ is diagonal.
:::

::: {.solution}
<1>1. By the spectral theorem, there exists an orthonormal basis
\[
v_1,\ldots,v_n
\]
of eigenvectors of $H$.

::: {.proof}
The operator $H$ is Hermitian on a finite-dimensional inner-product space.
The spectral theorem for Hermitian operators therefore gives an orthonormal basis consisting of eigenvectors.
Thus there are real numbers
\[
\lambda_1,\ldots,\lambda_n
\]
such that
\[
Hv_j=\lambda_jv_j
\]
for every $j$.
:::

<1>2. Let $U^*$ be the unitary change-of-basis operator sending the standard orthonormal basis
\[
e_1,\ldots,e_n
\]
to
\[
v_1,\ldots,v_n.
\]
Then
\[
U
\]
is its inverse.

::: {.proof}
An operator sending one orthonormal basis to another preserves inner products, hence is unitary.
Thus
\[
(U^*)^{-1}=U.
\]
Equivalently,
\[
UU^*=U^*U=I.
\]
:::

<1>3. For every $j$,
\[
UHU^*e_j=\lambda_je_j.
\]

::: {.proof}
By definition,
\[
U^*e_j=v_j.
\]
Hence
\[
\begin{aligned}
UHU^*e_j
&=
UH v_j\\
&=
U(\lambda_jv_j)\\
&=
\lambda_jUv_j\\
&=
\lambda_je_j.
\end{aligned}
\]
:::

<1>4. Therefore
\[
\boxed{
UHU^*
=
\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
}.
\]

::: {.proof}
Step <1>3 shows that every standard basis vector $e_j$ is an eigenvector of $UHU^*$ with eigenvalue $\lambda_j$.
Thus the matrix of $UHU^*$ in the standard basis is diagonal with those diagonal entries.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required unitary diagonalization.
:::
:::
