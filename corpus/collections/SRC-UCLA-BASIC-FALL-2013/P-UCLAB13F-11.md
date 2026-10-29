---
schema: qual/card@1
id: P-UCLAB13F-11
kind: problem
title: Spectral theorem for normal operators
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Define a normal linear transformation $N$ on a finite-dimensional complex inner-product space $V$. Assuming that $N$ is normal, show that there exists an orthogonal basis of $V$ consisting of eigenvectors of $N$.
:::

::: {.solution}

A linear transformation
\[
N:V\to V
\]
is called *normal* if
\[
\boxed{NN^*=N^*N},
\]
where $N^*$ is the adjoint of $N$.

::: pf

::: {.pf-step #s1-1}

If $N$ is normal, then for every $v\in V$,
\[
\|Nv\|=\|N^*v\|.
\]


::: pf-proof

Using the adjoint relation and normality,
\[
\begin{aligned}
\|Nv\|^2
&=
\langle Nv,Nv\rangle\\
&=
\langle N^*Nv,v\rangle\\
&=
\langle NN^*v,v\rangle\\
&=
\langle N^*v,N^*v\rangle\\
&=
\|N^*v\|^2.
\end{aligned}
\]
Taking nonnegative square roots gives the claim.

:::

:::

::: {.pf-step #s1-2}

If
\[
Nv=\lambda v,
\qquad
v\ne0,
\]
then
\[
N^*v=\overline{\lambda}v.
\]


::: pf-proof

Set
\[
T=N-\lambda I.
\]
Since $N$ is normal, $T$ is also normal:
\[
T^*T
=(N^*-\overline{\lambda}I)(N-\lambda I)
\]
and
\[
TT^*
=(N-\lambda I)(N^*-\overline{\lambda}I)
\]
are equal because $N^*N=NN^*$.

Now
\[
Tv=0.
\]
Applying step [](#s1-1){.pf-ref} to the normal operator $T$ gives
\[
\|T^*v\|=\|Tv\|=0.
\]
Hence
\[
T^*v=0,
\]
that is,
\[
(N^*-\overline{\lambda}I)v=0.
\]

:::

:::

::: {.pf-step #s1-3}

If $v$ is an eigenvector of $N$, then
\[
v^\perp
\]
is invariant under both $N$ and $N^*$.


::: pf-proof

Suppose
\[
Nv=\lambda v.
\]
By step [](#s1-2){.pf-ref},
\[
N^*v=\overline{\lambda}v.
\]

If $w\in v^\perp$, then
\[
\langle Nw,v\rangle
=
\langle w,N^*v\rangle
=
\langle w,\overline{\lambda}v\rangle
=0,
\]
so
\[
Nw\in v^\perp.
\]
Similarly,
\[
\langle N^*w,v\rangle
=
\langle w,Nv\rangle
=
\langle w,\lambda v\rangle
=0,
\]
so
\[
N^*w\in v^\perp.
\]

:::

:::

::: {.pf-step #s1-4}

The restriction
\[
N|_{v^\perp}:v^\perp\to v^\perp
\]
is normal.


::: pf-proof

By step [](#s1-3){.pf-ref}, both $N$ and $N^*$ preserve $v^\perp$.
Thus
\[
\left(N|_{v^\perp}\right)^*
=
N^*|_{v^\perp}.
\]
Restricting the identity
\[
NN^*=N^*N
\]
to $v^\perp$ gives
\[
\left(N|_{v^\perp}\right)
\left(N|_{v^\perp}\right)^*
=
\left(N|_{v^\perp}\right)^*
\left(N|_{v^\perp}\right).
\]
Hence the restriction is normal.

:::

:::

::: {.pf-step #s1-5}

If
\[
\dim V>0,
\]
then $N$ has a nonzero eigenvector.


::: pf-proof

The characteristic polynomial of $N$ has positive degree and complex coefficients.
By the fundamental theorem of algebra, it has a root
\[
\lambda\in\CC.
\]
Thus
\[
\det(N-\lambda I)=0,
\]
so
\[
\ker(N-\lambda I)\ne\{0\}.
\]
Any nonzero vector in this kernel is an eigenvector.

:::

:::

::: {.pf-step #s1-6}

Every normal operator on a finite-dimensional complex inner-product space has an orthonormal basis of eigenvectors.


::: pf-proof

Proceed by induction on
\[
n=\dim V.
\]
For $n=0$ the assertion is vacuous.

Assume $n>0$.
By step [](#s1-5){.pf-ref}, choose a nonzero eigenvector $v_1$ and normalize it so that
\[
\|v_1\|=1.
\]
Then
\[
v_1^\perp
\]
has dimension $n-1$ and is invariant under $N$ by step [](#s1-3){.pf-ref}.
The restricted operator is normal by step [](#s1-4){.pf-ref}.

By the induction hypothesis, $v_1^\perp$ has an orthonormal basis
\[
v_2,\ldots,v_n
\]
consisting of eigenvectors of the restriction, hence of $N$.
Therefore
\[
v_1,\ldots,v_n
\]
is an orthonormal basis of $V$ consisting entirely of eigenvectors of $N$.

:::

:::

::: pf-qed

The opening sentence gives the definition of normality, and step [](#s1-6){.pf-ref} proves the spectral theorem for normal operators.

:::

:::

:::
