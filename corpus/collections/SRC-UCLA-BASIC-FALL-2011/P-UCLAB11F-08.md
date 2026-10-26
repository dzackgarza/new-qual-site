---
schema: qual/card@1
id: P-UCLAB11F-08
kind: problem
title: Kernel stabilization criterion for diagonalizability
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 8. Assume that a complex matrix $A$ satisfies
\[
\ker(A-\lambda I)=\ker((A-\lambda I)^2)
\]
for every $\lambda\in\mathbb C$.
Show from first principles, without using the theory of canonical forms, that $A$ is diagonalizable.
:::

The proof is by induction on the dimension $n$ of the underlying complex vector space $V=\mathbb C^n$.

::: pf

::: pf-step

If $n=1$, then $A$ is diagonalizable.


::: pf-proof

Every linear operator on a one-dimensional vector space is multiplication by a scalar.

:::

:::

::: pf-step

Assume $n>1$. Then $A$ has an eigenvalue $\lambda\in\mathbb C$ and a nonzero eigenspace
\[
E=\ker(A-\lambda I).
\]


::: pf-proof

The characteristic polynomial of $A$ has degree $n$, so by the fundamental theorem of algebra it has a root $\lambda\in\mathbb C$. Hence
\[
\det(A-\lambda I)=0,
\]
and therefore $E$ contains a nonzero vector.

:::

:::

::: pf-step

Put
\[
B=A-\lambda I.
\]
Then
\[
\operatorname{im}B\cap\ker B=\{0\}.
\]


::: pf-proof

Let
\[
v\in\operatorname{im}B\cap\ker B.
\]
Then
\[
v=Bw
\]
for some $w\in V$, and
\[
Bv=0.
\]
Therefore
\[
B^2w=0.
\]
By the hypothesis for the eigenvalue $\lambda$,
\[
\ker B=\ker B^2.
\]
Hence
\[
Bw=0,
\]
so
\[
v=Bw=0.
\]

:::

:::

::: pf-step

One has the direct-sum decomposition
\[
\boxed{V=\ker B\oplus\operatorname{im}B}.
\]


::: pf-proof

By rank-nullity,
\[
\dim\ker B+\dim\operatorname{im}B=n=\dim V.
\]
Step <1>3 shows that their intersection is zero. Therefore the sum is direct and has dimension $n$, hence equals $V$.

:::

:::

::: pf-step

Both subspaces
\[
\ker B
\qquad\text{and}\qquad
\operatorname{im}B
\]
are invariant under $A$.


::: pf-proof

Since
\[
A=B+\lambda I,
\]
the operator $A$ commutes with $B$.

If $v\in\ker B$, then
\[
B(Av)=A(Bv)=0,
\]
so $Av\in\ker B$.

If $v\in\operatorname{im}B$, write $v=Bw$. Then
\[
Av=ABw=BAw\in\operatorname{im}B.
\]

:::

:::

::: pf-step

The restriction
\[
A_E:=A|_{\ker B}
\]
is diagonalizable.


::: pf-proof

For every $v\in\ker B$,
\[
(A-\lambda I)v=Bv=0,
\]
so
\[
Av=\lambda v.
\]
Thus $A_E=\lambda I$ on $\ker B$, which is diagonal in every basis.

:::

:::

::: pf-step

Let
\[
W=\operatorname{im}B.
\]
For every $\mu\in\mathbb C$, the restriction
\[
A_W:=A|_W
\]
satisfies
\[
\ker(A_W-\mu I)
=
\ker((A_W-\mu I)^2).
\]


::: pf-proof

The inclusion
\[
\ker(A_W-\mu I)
\subseteq
\ker((A_W-\mu I)^2)
\]
is automatic.

Conversely, let $w\in W$ satisfy
\[
(A_W-\mu I)^2w=0.
\]
Then, viewing $w$ as a vector of $V$,
\[
(A-\mu I)^2w=0.
\]
By the global hypothesis,
\[
w\in\ker(A-\mu I).
\]
Since $w\in W$, this says
\[
w\in\ker(A_W-\mu I).
\]

:::

:::

::: pf-step

If $W\ne\{0\}$, then
\[
\dim W<n.
\]


::: pf-proof

By step <1>2,
\[
\ker B\ne\{0\}.
\]
The direct-sum decomposition in step <1>4 gives
\[
\dim W
=
n-\dim\ker B
<
n.
\]

:::

:::

::: pf-step

The restriction $A_W$ is diagonalizable.


::: pf-proof

If $W=\{0\}$, the assertion is trivial.
Otherwise, step <1>8 gives
\[
\dim W<n,
\]
and step <1>7 shows that $A_W$ satisfies the same kernel-stabilization hypothesis as $A$. The induction hypothesis therefore implies that $A_W$ is diagonalizable.

:::

:::

::: pf-step

The operator $A$ is diagonalizable.


::: pf-proof

By step <1>4,
\[
V=\ker B\oplus W,
\]
and both summands are $A$-invariant by step <1>5.
Choose an eigenbasis of $\ker B$ for $A_E$ using step <1>6 and an eigenbasis of $W$ for $A_W$ using step <1>9. Their union is a basis of the direct sum $V$ consisting entirely of eigenvectors of $A$. Hence
\[
\boxed{A\text{ is diagonalizable}}.
\]

:::

:::

::: pf-qed

Steps <1>1--<1>10 establish the induction and prove the required diagonalizability without using canonical forms.

:::

:::
