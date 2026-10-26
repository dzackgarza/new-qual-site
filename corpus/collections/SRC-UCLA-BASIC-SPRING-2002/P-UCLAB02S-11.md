---
schema: qual/card@1
id: P-UCLAB02S-11
kind: problem
title: Simultaneous orthonormal eigenbasis for commuting self-adjoint operators
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 11 of the official UCLA Basic Exam Spring 2002 PDF. The source uses the word "hermitian" for operators on a real inner-product space; the standard real terminology "self-adjoint" is used here.
---

::: {.problem}
Let $V$ be a finite-dimensional real inner-product space and let $T,S:V\to V$ be commuting self-adjoint linear operators.
Show that $V$ has an orthonormal basis consisting of vectors that are simultaneously eigenvectors of $T$ and $S$.
:::

::: pf

::: pf-step

By the spectral theorem for real self-adjoint operators,
\[
V
=
\bigoplus_{\lambda}E_\lambda,
\]
where
\[
E_\lambda=\ker(T-\lambda I)
\]
and the sum is orthogonal.


::: pf-proof

Since $T$ is self-adjoint on a finite-dimensional real inner-product space, the spectral theorem gives an orthonormal basis of $V$ consisting of eigenvectors of $T$.
Grouping basis vectors with the same eigenvalue gives the orthogonal direct-sum decomposition into eigenspaces.

:::

:::

::: pf-step

Every eigenspace $E_\lambda$ of $T$ is invariant under $S$.


::: pf-proof

Let
\[
v\in E_\lambda.
\]
Then
\[
Tv=\lambda v.
\]
Because $T$ and $S$ commute,
\[
T(Sv)
=
S(Tv)
=
S(\lambda v)
=
\lambda Sv.
\]
Thus
\[
Sv\in E_\lambda.
\]

:::

:::

::: pf-step

For each eigenvalue $\lambda$ of $T$, the restriction
\[
S_\lambda=S|_{E_\lambda}:E_\lambda\to E_\lambda
\]
is self-adjoint.


::: pf-proof

Step <1>2 shows that the restriction is well-defined.
For
\[
u,v\in E_\lambda,
\]
self-adjointness of $S$ on $V$ gives
\[
\langle S_\lambda u,v\rangle
=
\langle Su,v\rangle
=
\langle u,Sv\rangle
=
\langle u,S_\lambda v\rangle.
\]
Thus $S_\lambda$ is self-adjoint on the inner-product space $E_\lambda$.

:::

:::

::: pf-step

Each $E_\lambda$ has an orthonormal basis consisting of eigenvectors of $S$.


::: pf-proof

By step <1>3, $S_\lambda$ is self-adjoint on the finite-dimensional real inner-product space $E_\lambda$.
The spectral theorem therefore gives an orthonormal basis of $E_\lambda$ consisting of eigenvectors of $S_\lambda$, hence of $S$.

:::

:::

::: pf-step

Every vector in the bases from step <1>4 is simultaneously an eigenvector of $T$ and $S$.


::: pf-proof

Each such vector lies in
\[
E_\lambda,
\]
so it is an eigenvector of $T$ with eigenvalue $\lambda$.
By construction in step <1>4, it is also an eigenvector of $S$.

:::

:::

::: pf-step

The union over all $\lambda$ of the orthonormal bases from step <1>4 is an orthonormal basis of $V$.


::: pf-proof

By step <1>1, the eigenspaces $E_\lambda$ form an orthogonal direct sum whose sum is all of $V$.
Within each eigenspace, step <1>4 supplies an orthonormal basis.
Because distinct eigenspaces are orthogonal, the union of these bases is orthonormal.
Because their direct sum is $V$, the union spans $V$.

:::

:::

::: pf-step

Therefore $V$ has an orthonormal basis of simultaneous eigenvectors of $T$ and $S$.


::: pf-proof

This is exactly the basis constructed in steps <1>4--<1>6.

:::

:::

::: pf-qed

Step <1>7 is the required conclusion.

:::

:::
