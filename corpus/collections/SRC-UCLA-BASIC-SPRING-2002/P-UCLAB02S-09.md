---
schema: qual/card@1
id: P-UCLAB02S-09
kind: problem
title: Matrix of a rotation in a specified two-plane in four-space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Exam Spring 2002 PDF.
---

::: {.problem}
Find the matrix, in the standard basis of $\RR^4$, for either rotation by an angle $\theta$ in the plane perpendicular to the subspace spanned by
$$
(1,1,1,1)
\qquad\text{and}\qquad
(1,1,1,0).
$$

You need not multiply the matrices out, but you must compute any inverses that occur.
:::

::: {.solution}

Let
$$
a=(1,1,1,1),
\qquad
b=(1,1,1,0).
$$

::: pf

::: pf-step

The plane perpendicular to
$$
\operatorname{span}\{a,b\}
$$
is
$$
P=
\left\{
(x_1,x_2,x_3,0):
x_1+x_2+x_3=0
\right\}.
$$


::: pf-proof

A vector
$$
x=(x_1,x_2,x_3,x_4)
$$
lies in the orthogonal complement exactly when
$$
x\cdot a
=
x_1+x_2+x_3+x_4
=0
$$
and
$$
x\cdot b
=
x_1+x_2+x_3
=0.
$$
Subtracting gives
$$
x_4=0.
$$
The remaining condition is
$$
x_1+x_2+x_3=0.
$$

:::

:::

::: {.pf-step #s1-2}

An orthonormal basis of $P$ is
$$
u_1
=
\frac1{\sqrt2}(1,-1,0,0),
\qquad
u_2
=
\frac1{\sqrt6}(1,1,-2,0).
$$


::: pf-proof

Both vectors lie in $P$ because their fourth coordinates vanish and the sums of their first three coordinates are zero.
Also
$$
\|u_1\|=\|u_2\|=1
$$
and
$$
u_1\cdot u_2
=
\frac{1-1}{\sqrt{12}}
=0.
$$
Since $P$ has dimension $2$, they form an orthonormal basis.

:::

:::

::: {.pf-step #s1-3}

An orthonormal basis of
$$
\operatorname{span}\{a,b\}
$$
is
$$
u_3
=
\frac1{\sqrt3}(1,1,1,0),
\qquad
u_4
=
(0,0,0,1).
$$


::: pf-proof

The vector $u_3$ is the normalized vector $b$.
Also
$$
a-b=(0,0,0,1)=u_4.
$$
Thus $u_3,u_4$ span the same subspace as $a,b$.
They are orthonormal because $u_3$ has fourth coordinate zero and $u_4$ has only fourth coordinate nonzero.

:::

:::

::: {.pf-step #s1-4}

The ordered list
$$
u_1,u_2,u_3,u_4
$$
is an orthonormal basis of $\RR^4$.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, the first two vectors form an orthonormal basis of
$$
\operatorname{span}\{a,b\}^{\perp},
$$
and the last two form an orthonormal basis of
$$
\operatorname{span}\{a,b\}.
$$
The two subspaces are orthogonal complements, so the full list is an orthonormal basis of $\RR^4$.

:::

:::

::: {.pf-step #s1-5}

In the basis from step [](#s1-4){.pf-ref}, one rotation through angle $\theta$ in the perpendicular plane, fixing
$$
\operatorname{span}\{a,b\}
$$
pointwise, has matrix
$$
R=
\begin{pmatrix}
\cos\theta&-\sin\theta&0&0\\
\sin\theta&\cos\theta&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
$$


::: pf-proof

The upper-left block is the standard counterclockwise rotation through angle $\theta$ in the oriented orthonormal basis
$$
u_1,u_2
$$
of the perpendicular plane.
The last two basis vectors span the subspace to be fixed, so the final block is the identity.
The opposite choice of orientation replaces $\theta$ by $-\theta$.

:::

:::

::: {.pf-step #s1-6}

Let
$$
Q=
\begin{pmatrix}
\frac1{\sqrt2}&\frac1{\sqrt6}&\frac1{\sqrt3}&0\\
-\frac1{\sqrt2}&\frac1{\sqrt6}&\frac1{\sqrt3}&0\\
0&-\frac2{\sqrt6}&\frac1{\sqrt3}&0\\
0&0&0&1
\end{pmatrix}.
$$
Then
$$
\boxed{Q^{-1}=Q^T}
$$
with
$$
Q^T=
\begin{pmatrix}
\frac1{\sqrt2}&-\frac1{\sqrt2}&0&0\\
\frac1{\sqrt6}&\frac1{\sqrt6}&-\frac2{\sqrt6}&0\\
\frac1{\sqrt3}&\frac1{\sqrt3}&\frac1{\sqrt3}&0\\
0&0&0&1
\end{pmatrix}.
$$


::: pf-proof

The columns of $Q$ are the orthonormal basis vectors
$$
u_1,u_2,u_3,u_4.
$$
Hence $Q$ is orthogonal, so
$$
Q^{-1}=Q^T.
$$

:::

:::

::: {.pf-step #s1-7}

In the standard basis, the required rotation matrix is
$$
\boxed{
[T]_{\mathrm{std}}
=
QRQ^T
}.
$$


::: pf-proof

The matrix $Q$ changes coordinates from the basis
$$
u_1,u_2,u_3,u_4
$$
to the standard basis.
Therefore conjugating the matrix $R$ from step [](#s1-5){.pf-ref} by $Q$ gives the standard-basis matrix:
$$
[T]_{\mathrm{std}}
=
QRQ^{-1}
=
QRQ^T.
$$
All inverses appearing in this expression were computed explicitly in step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the requested matrix in the standard basis.

:::

:::

:::
