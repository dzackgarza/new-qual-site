---
schema: qual/card@1
id: P-UCLAB02F-08
kind: problem
title: Rotation by $60^\circ$ about the axis $(1,1,2)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Visually checked against Problem 8 of the retained UCLA Basic Examination, Fall 2002 PDF; the source specifies a counterclockwise 60-degree rotation in the plane perpendicular to (1,1,2).
---

::: {.problem}
Let $T$ be the rotation through $60^\circ$ counterclockwise about the origin in the plane perpendicular to $(1,1,2)$ in $\RR^3$.

(i) Find the matrix of $T$ in the standard basis, and find all real eigenvalues and eigenspaces of $T$.

(ii) What are the eigenvalues and eigenspaces of the same transformation after replacing $\RR^3$ by $\CC^3$?

You do not have to multiply matrices out, but you must compute any inverses.
:::

::: {.solution}

Let
\[
u_1=\frac1{\sqrt2}(1,-1,0),\qquad
u_2=\frac1{\sqrt3}(1,1,-1),\qquad
u_3=\frac1{\sqrt6}(1,1,2).
\]

::: pf

::: pf-step

The ordered triple $(u_1,u_2,u_3)$ is a positively oriented orthonormal basis of $\RR^3$.


::: pf-proof

Direct computation gives
\[
u_i\cdot u_j=\delta_{ij}.
\]
Moreover,
\[
(1,-1,0)\times(1,1,-1)=(1,1,2),
\]
so $u_1\times u_2=u_3$. Thus the basis is positively oriented.

:::

:::

::: {.pf-step #s1-2}

In the basis $(u_1,u_2,u_3)$, the matrix of $T$ is
\[
R=
\begin{pmatrix}
\frac12&-\frac{\sqrt3}{2}&0\\
\frac{\sqrt3}{2}&\frac12&0\\
0&0&1
\end{pmatrix}.
\]


::: pf-proof

The vector $u_3$ spans the rotation axis, so $T(u_3)=u_3$. The vectors $u_1,u_2$ form the positively oriented orthonormal basis of the perpendicular plane determined by the normal $u_3$. Therefore the restriction of $T$ to that plane is the usual counterclockwise rotation through $60^\circ$, whose matrix is the upper-left $2\times2$ block displayed above.

:::

:::

::: {.pf-step #s1-3}

If
\[
Q=
\begin{pmatrix}
\frac1{\sqrt2}&\frac1{\sqrt3}&\frac1{\sqrt6}\\
-\frac1{\sqrt2}&\frac1{\sqrt3}&\frac1{\sqrt6}\\
0&-\frac1{\sqrt3}&\frac2{\sqrt6}
\end{pmatrix},
\]
then
\[
Q^{-1}=Q^t
=
\begin{pmatrix}
\frac1{\sqrt2}&-\frac1{\sqrt2}&0\\
\frac1{\sqrt3}&\frac1{\sqrt3}&-\frac1{\sqrt3}\\
\frac1{\sqrt6}&\frac1{\sqrt6}&\frac2{\sqrt6}
\end{pmatrix}
\]
and
\[
\boxed{[T]_{\mathrm{std}}=QRQ^t}.
\]


::: pf-proof

The columns of $Q$ are the orthonormal vectors $u_1,u_2,u_3$. Hence $Q$ is orthogonal and $Q^{-1}=Q^t$. Conjugating the matrix of $T$ from step [](#s1-2){.pf-ref} by the change-of-basis matrix $Q$ gives the standard-basis matrix.

:::

:::

::: {.pf-step #s1-4}

Over $\RR$, the only eigenvalue of $T$ is
\[
\boxed{1},
\]
with eigenspace
\[
\boxed{E_1=\operatorname{span}_{\RR}\{(1,1,2)\}}.
\]


::: pf-proof

In the basis $(u_1,u_2,u_3)$, the characteristic polynomial is
\[
(\lambda-1)
\left[
\left(\lambda-\frac12\right)^2+\frac34
\right].
\]
The quadratic factor has no real roots. Thus the only real eigenvalue is $1$. The $1$-eigenspace is the rotation axis, namely
\[
\operatorname{span}_{\RR}\{u_3\}
=
\operatorname{span}_{\RR}\{(1,1,2)\}.
\]

:::

:::

::: {.pf-step #s1-5}

Over $\CC$, the eigenvalues are
\[
\boxed{
1,\qquad
\lambda_+=\frac12+\frac{\sqrt3}{2}i,qquad
\lambda_-=\frac12-\frac{\sqrt3}{2}i
}.
\]


::: pf-proof

These are the three roots of the characteristic polynomial computed in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Over $\CC$, the corresponding eigenspaces are
\[
\boxed{
E_1=\operatorname{span}_{\CC}\{u_3\},
\qquad
E_{\lambda_+}=\operatorname{span}_{\CC}\{u_1-i u_2\},
\qquad
E_{\lambda_-}=\operatorname{span}_{\CC}\{u_1+i u_2\}
}.
\]


::: pf-proof

The vector $u_3$ is fixed by $T$. On the complexification of $\operatorname{span}(u_1,u_2)$, step [](#s1-2){.pf-ref} gives
\[
T(u_1-i u_2)
=
\left(\frac12+\frac{\sqrt3}{2}i\right)(u_1-i u_2)
\]
and
\[
T(u_1+i u_2)
=
\left(\frac12-\frac{\sqrt3}{2}i\right)(u_1+i u_2).
\]
The three eigenvalues in step [](#s1-5){.pf-ref} are distinct, so each eigenspace is one-dimensional and the displayed spans are the complete eigenspaces.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested standard-basis matrix and inverse, step [](#s1-4){.pf-ref} gives all real eigenvalues and eigenspaces, and steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} give the complex eigenvalues and eigenspaces.

:::

:::

:::
