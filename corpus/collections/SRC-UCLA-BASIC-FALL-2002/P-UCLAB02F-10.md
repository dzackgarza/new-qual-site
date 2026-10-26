---
schema: qual/card@1
id: P-UCLAB02F-10
kind: problem
title: Spectral theorem for normal complex matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix satisfying
\[
A^*A=AA^*,
\]
where $A^*$ is the adjoint of $A$.
Let $V=\mathbb C^n$, regarded as an inner product space with its standard inner product, and view $A:V\to V$ as a linear map.
Prove that there exists an orthonormal basis of $V$ consisting of eigenvectors of $A$; that is, prove this form of the spectral theorem for normal operators.
:::

The proof is by induction on $n$.

::: pf

::: pf-step

If $B$ is a normal complex matrix, then
\[
\|Bx\|=\|B^*x\|
\]
for every vector $x$.


::: pf-proof

Using the standard Hermitian norm,
\[
\|Bx\|^2=x^*B^*Bx
\]
and
\[
\|B^*x\|^2=x^*BB^*x.
\]
If $B$ is normal, then $B^*B=BB^*$, so the squared norms are equal.

:::

:::

::: pf-step

If $A$ is normal and
\[
Av=\lambda v,
\]
then
\[
A^*v=\overline{\lambda}v.
\]


::: pf-proof

Set
\[
B=A-\lambda I.
\]
Since $A$ is normal,
\[
\begin{aligned}
B^*B
&=(A^*-\overline{\lambda}I)(A-\lambda I)\\
&=A^*A-\lambda A^*-\overline{\lambda}A+|\lambda|^2I
\end{aligned}
\]
and
\[
\begin{aligned}
BB^*
&=(A-\lambda I)(A^*-\overline{\lambda}I)\\
&=AA^*-\overline{\lambda}A-\lambda A^*+|\lambda|^2I,
\end{aligned}
\]
so $B$ is normal. Since $Bv=0$, step <1>1 gives
\[
\|B^*v\|=\|Bv\|=0.
\]
Thus
\[
B^*v=(A^*-\overline{\lambda}I)v=0,
\]
which proves the claim.

:::

:::

::: pf-step

The matrix $A$ has a nonzero eigenvector.


::: pf-proof

The characteristic polynomial of $A$ has degree $n$. For $n\ge1$, the fundamental theorem of algebra gives a root $\lambda\in\mathbb C$. Hence
\[
\det(A-\lambda I)=0,
\]
so there is a nonzero vector $v$ satisfying
\[
Av=\lambda v.
\]

:::

:::

::: pf-step

If $v$ is an eigenvector of $A$, then $v^\perp$ is invariant under both $A$ and $A^*$.


::: pf-proof

Let
\[
Av=\lambda v.
\]
By step <1>2,
\[
A^*v=\overline{\lambda}v.
\]
If $w\in v^\perp$, then
\[
v^*Aw=(A^*v)^*w=(\overline{\lambda}v)^*w
=\lambda v^*w=0,
\]
so $Aw\in v^\perp$.

Similarly,
\[
v^*A^*w=(Av)^*w=(\lambda v)^*w
=\overline{\lambda}v^*w=0,
\]
so $A^*w\in v^\perp$.

:::

:::

::: pf-step

The restriction
\[
A|_{v^\perp}:v^\perp\to v^\perp
\]
is normal.


::: pf-proof

By step <1>4, both $A$ and $A^*$ preserve $v^\perp$. Hence the adjoint of the restriction of $A$ is the restriction of $A^*$:
\[
(A|_{v^\perp})^*=A^*|_{v^\perp}.
\]
Because
\[
A^*A=AA^*
\]
on all of $V$, restricting this equality to $v^\perp$ gives
\[
(A|_{v^\perp})^*(A|_{v^\perp})
=(A|_{v^\perp})(A|_{v^\perp})^*.
\]
Thus the restriction is normal.

:::

:::

::: pf-step

Every normal operator on $\mathbb C^n$ has an orthonormal basis of eigenvectors.


::: pf-proof

For $n=1$, every nonzero vector, after normalization, is an orthonormal eigenbasis.

Assume the assertion holds in dimension $n-1$, and let $A$ be normal on $\mathbb C^n$. By step <1>3, choose a nonzero eigenvector $v_1$ and normalize it so that
\[
\|v_1\|=1.
\]
Then
\[
v_1^\perp
\]
has dimension $n-1$. By step <1>5, the restriction of $A$ to this subspace is normal. The induction hypothesis therefore gives an orthonormal basis
\[
v_2,\ldots,v_n
\]
of $v_1^\perp$ consisting of eigenvectors of the restriction, hence of $A$. Consequently
\[
v_1,v_2,\ldots,v_n
\]
is an orthonormal basis of $\mathbb C^n$ consisting entirely of eigenvectors of $A$.

:::

:::

::: pf-qed

Step <1>6 is precisely the required spectral theorem for the normal matrix $A$.

:::

:::
