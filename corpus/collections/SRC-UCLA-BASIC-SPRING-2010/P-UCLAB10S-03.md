---
schema: qual/card@1
id: P-UCLAB10S-03
kind: problem
title: Joint eigenbasis for commuting normal operators
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 3. Let $S$ and $T$ be commuting normal operators on a finite-dimensional complex inner-product space $V$.
Prove that $S$ and $T$ have a common basis of eigenvectors.
:::

::: pf

::: pf-step

Since $S$ is normal, $V$ is an orthogonal direct sum of its eigenspaces:
\[
V=\bigoplus_{\lambda}E_\lambda(S).
\]


::: pf-proof

By the spectral theorem for normal operators on finite-dimensional complex inner-product spaces, $S$ has an orthonormal basis of eigenvectors.
Grouping basis vectors with the same eigenvalue gives the displayed orthogonal decomposition.

:::

:::

::: pf-step

Every eigenspace
\[
E_\lambda(S)
\]
is invariant under $T$.


::: pf-proof

Let
\[
v\in E_\lambda(S).
\]
Then
\[
Sv=\lambda v.
\]
Using
\[
ST=TS,
\]
one gets
\[
S(Tv)
=
T(Sv)
=
\lambda Tv.
\]
Hence
\[
Tv\in E_\lambda(S).
\]

:::

:::

::: pf-step

Every eigenspace
\[
E_\lambda(S)
\]
is also invariant under $T^*$.


::: pf-proof

Because $T$ is normal and commutes with $S$, the adjoint $T^*$ also commutes with $S$.

Indeed, by the spectral theorem for the normal operator $T$, there is a polynomial $p$ on the finite set of eigenvalues of $T$ such that
\[
T^*=p(T).
\]
Since $S$ commutes with $T$, it commutes with every polynomial in $T$, hence with $T^*$.

Therefore, if
\[
Sv=\lambda v,
\]
then
\[
S(T^*v)
=
T^*(Sv)
=
\lambda T^*v,
\]
so
\[
T^*v\in E_\lambda(S).
\]

:::

:::

::: pf-step

The restriction
\[
T_\lambda
=
T|_{E_\lambda(S)}
\]
is normal on the inner-product space $E_\lambda(S)$.


::: pf-proof

By steps <1>2--<1>3, both $T$ and $T^*$ preserve
\[
E_\lambda(S).
\]
Thus
\[
T_\lambda^*
=
T^*|_{E_\lambda(S)}.
\]
Since
\[
TT^*=T^*T
\]
on $V$, restricting to $E_\lambda(S)$ gives
\[
T_\lambda T_\lambda^*
=
T_\lambda^*T_\lambda.
\]
Hence $T_\lambda$ is normal.

:::

:::

::: pf-step

Each eigenspace
\[
E_\lambda(S)
\]
has an orthonormal basis consisting of eigenvectors of $T$.


::: pf-proof

By step <1>4, the restriction $T_\lambda$ is normal on the finite-dimensional complex inner-product space
\[
E_\lambda(S).
\]
The spectral theorem therefore gives an orthonormal basis of $E_\lambda(S)$ consisting of eigenvectors of $T_\lambda$, hence of $T$.

:::

:::

::: pf-step

Every vector in the bases from step <1>5 is simultaneously an eigenvector of $S$ and $T$.


::: pf-proof

Each such vector lies in
\[
E_\lambda(S),
\]
so it is an eigenvector of $S$ with eigenvalue $\lambda$.
By construction in step <1>5, it is also an eigenvector of $T$.

:::

:::

::: pf-step

The union over all eigenvalues $\lambda$ of the bases from step <1>5 is a basis of $V$.


::: pf-proof

By step <1>1, the eigenspaces of $S$ form an orthogonal direct sum equal to $V$.
Choosing a basis in each summand and taking their union therefore gives a basis of $V$.

:::

:::

::: pf-step

Therefore
\[
\boxed{
S\text{ and }T\text{ have a common orthonormal basis of eigenvectors}.
}
\]


::: pf-proof

By steps <1>6--<1>7, the union basis consists entirely of simultaneous eigenvectors.

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
