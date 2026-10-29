---
schema: qual/card@1
id: P-UCLAB15S-09
kind: problem
title: A linear operator carrying one pair of subspaces onto another with the same intersection dimension
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $V=\RR^n$, and let $U_1,U_2,W_1,W_2\subset V$ be subspaces of dimension $d$ such that
\[
\dim(U_1\cap W_1)=\dim(U_2\cap W_2)=\ell,
\qquad \ell\le d\le n.
\]
Prove that there exists a linear operator $T:V\to V$ such that
\[
T(U_1)=U_2,\qquad T(W_1)=W_2.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Choose a basis
\[
c_1,\ldots,c_\ell
\]
of
\[
U_1\cap W_1.
\]
Extend it to bases
\[
c_1,\ldots,c_\ell,u_{\ell+1},\ldots,u_d
\]
of $U_1$ and
\[
c_1,\ldots,c_\ell,w_{\ell+1},\ldots,w_d
\]
of $W_1$.


::: pf-proof

Every basis of a subspace extends to a basis of any larger finite-dimensional subspace.
Since
\[
\dim(U_1\cap W_1)=\ell,
\]
the chosen intersection basis extends by exactly $d-\ell$ vectors to each $d$-dimensional subspace.

:::

:::

::: {.pf-step #s1-2}

The list
\[
\mathcal B_1
=
\bigl(
c_1,\ldots,c_\ell,
u_{\ell+1},\ldots,u_d,
w_{\ell+1},\ldots,w_d
\bigr)
\]
is a basis of
\[
U_1+W_1.
\]


::: pf-proof

The list clearly spans
\[
U_1+W_1.
\]
Its length is
\[
\ell+(d-\ell)+(d-\ell)
=
2d-\ell.
\]
By the dimension formula,
\[
\dim(U_1+W_1)
=
\dim U_1+\dim W_1-\dim(U_1\cap W_1)
=
2d-\ell.
\]
A spanning list with exactly the dimension of the space is a basis.

:::

:::

::: pf-step

Likewise, choose a basis
\[
c'_1,\ldots,c'_\ell
\]
of
\[
U_2\cap W_2,
\]
extend it to bases
\[
c'_1,\ldots,c'_\ell,u'_{\ell+1},\ldots,u'_d
\]
of $U_2$ and
\[
c'_1,\ldots,c'_\ell,w'_{\ell+1},\ldots,w'_d
\]
of $W_2$.
Then
\[
\mathcal B_2
=
\bigl(
c'_1,\ldots,c'_\ell,
u'_{\ell+1},\ldots,u'_d,
w'_{\ell+1},\ldots,w'_d
\bigr)
\]
is a basis of
\[
U_2+W_2.
\]


::: pf-proof

Apply the same argument as in steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, using
\[
\dim(U_2\cap W_2)=\ell.
\]

:::

:::

::: {.pf-step #s1-4}

The two sums have equal dimension:
\[
\dim(U_1+W_1)
=
\dim(U_2+W_2)
=
2d-\ell.
\]


::: pf-proof

This follows from the dimension formula and the common values of
\[
\dim U_i=\dim W_i=d
\]
and
\[
\dim(U_i\cap W_i)=\ell.
\]

:::

:::

::: {.pf-step #s1-5}

Extend $\mathcal B_1$ to a basis of $V$ by adding vectors
\[
z_1,\ldots,z_r,
\]
and extend $\mathcal B_2$ to a basis of $V$ by adding
\[
z'_1,\ldots,z'_r,
\]
where
\[
r=n-(2d-\ell).
\]


::: pf-proof

By step [](#s1-4){.pf-ref}, the two subspaces have the same dimension.
Each basis therefore requires the same number
\[
r
\]
of additional vectors to become a basis of the $n$-dimensional space $V$.

:::

:::

::: {.pf-step #s1-6}

Define $T:V\to V$ on the first basis by
\[
T(c_i)=c'_i
\qquad
(1\le i\le\ell),
\]
\[
T(u_j)=u'_j
\qquad
(\ell<j\le d),
\]
\[
T(w_j)=w'_j
\qquad
(\ell<j\le d),
\]
and
\[
T(z_q)=z'_q
\qquad
(1\le q\le r),
\]
then extend linearly.


::: pf-proof

A linear map is uniquely determined by its values on a basis.
Step [](#s1-5){.pf-ref} gives a basis of $V$ on which the displayed prescription is defined.

:::

:::

::: {.pf-step #s1-7}

The operator $T$ is invertible.


::: pf-proof

By construction, $T$ sends the basis from step [](#s1-5){.pf-ref} bijectively onto the target basis from the same step.
A linear map sending a basis to a basis is an isomorphism.

:::

:::

::: {.pf-step #s1-8}

One has
\[
\boxed{T(U_1)=U_2}.
\]


::: pf-proof

The subspace $U_1$ has basis
\[
c_1,\ldots,c_\ell,u_{\ell+1},\ldots,u_d.
\]
Step [](#s1-6){.pf-ref} sends these vectors to
\[
c'_1,\ldots,c'_\ell,u'_{\ell+1},\ldots,u'_d,
\]
which is a basis of $U_2$.
Therefore
\[
T(U_1)=U_2.
\]

:::

:::

::: {.pf-step #s1-9}

One also has
\[
\boxed{T(W_1)=W_2}.
\]


::: pf-proof

The basis
\[
c_1,\ldots,c_\ell,w_{\ell+1},\ldots,w_d
\]
of $W_1$ is sent by step [](#s1-6){.pf-ref} to the basis
\[
c'_1,\ldots,c'_\ell,w'_{\ell+1},\ldots,w'_d
\]
of $W_2$.
Hence
\[
T(W_1)=W_2.
\]

:::

:::

::: pf-qed

Steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref} give the required operator, and step [](#s1-7){.pf-ref} shows it may in fact be chosen invertible.

:::

:::

:::
