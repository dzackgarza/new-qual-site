---
schema: qual/card@1
id: P-UCLAB01F-08
kind: problem
title: Matrix of a composition of a spatial rotation and reflection
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Visually checked against Problem 8 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Let $T:\RR^3\to\RR^3$ be the rotation by $60^\circ$ counterclockwise in the plane perpendicular to $(1,1,1)$, and let $S:\RR^3\to\RR^3$ be reflection in the plane perpendicular to $(1,0,1)$.
Determine the matrix of $S\circ T$ in the standard basis
$$
\{(1,0,0),(0,1,0),(0,0,1)\}.
$$
You do not have to multiply the resulting matrices, but you must determine any inverses that arise.
:::

::: {.solution}

Let
$$
u_1=\frac1{\sqrt2}(1,-1,0),\qquad
u_2=\frac1{\sqrt6}(1,1,-2),\qquad
u_3=\frac1{\sqrt3}(1,1,1).
$$
The ordered basis $(u_1,u_2,u_3)$ is positively oriented, so the given normal vector $u_3$ induces the usual counterclockwise orientation on $u_3^\perp$.

::: pf

::: {.pf-step #s1-1}

The vectors $u_1,u_2,u_3$ form a positively oriented orthonormal basis of $\RR^3$.


::: pf-proof

Direct computation gives
$$
u_i\cdot u_j=\delta_{ij}.
$$
Moreover,
$$
(1,-1,0)\times(1,1,-2)=(2,2,2),
$$
which is a positive multiple of $(1,1,1)$. Hence $(u_1,u_2,u_3)$ is positively oriented.

:::

:::

::: {.pf-step #s1-2}

In the basis $(u_1,u_2,u_3)$, the matrix of $T$ is
$$
R=
\begin{pmatrix}
\frac12&-\frac{\sqrt3}{2}&0\\
\frac{\sqrt3}{2}&\frac12&0\\
0&0&1
\end{pmatrix}.
$$


::: pf-proof

The vectors $u_1,u_2$ form an oriented orthonormal basis of the plane perpendicular to $(1,1,1)$, while $u_3$ spans the rotation axis. Thus $T$ acts on $\operatorname{span}(u_1,u_2)$ as counterclockwise rotation through $60^\circ$ and fixes $u_3$. The displayed matrix is exactly this action.

:::

:::

::: {.pf-step #s1-3}

If
$$
Q=
\begin{pmatrix}
\frac1{\sqrt2}&\frac1{\sqrt6}&\frac1{\sqrt3}\\
-\frac1{\sqrt2}&\frac1{\sqrt6}&\frac1{\sqrt3}\\
0&-\frac2{\sqrt6}&\frac1{\sqrt3}
\end{pmatrix},
$$
then
$$
Q^{-1}=Q^t
=
\begin{pmatrix}
\frac1{\sqrt2}&-\frac1{\sqrt2}&0\\
\frac1{\sqrt6}&\frac1{\sqrt6}&-\frac2{\sqrt6}\\
\frac1{\sqrt3}&\frac1{\sqrt3}&\frac1{\sqrt3}
\end{pmatrix}
$$
and the standard-basis matrix of $T$ is
$$
[T]=QRQ^t.
$$


::: pf-proof

The columns of $Q$ are $u_1,u_2,u_3$. By step [](#s1-1){.pf-ref}, $Q$ is orthogonal, so $Q^{-1}=Q^t$. Conjugating the matrix from step [](#s1-2){.pf-ref} by the change-of-basis matrix gives
$$
[T]=QRQ^{-1}=QRQ^t.
$$

:::

:::

::: {.pf-step #s1-4}

The standard-basis matrix of the reflection $S$ is
$$
[S]=
\begin{pmatrix}
0&0&-1\\
0&1&0\\
-1&0&0
\end{pmatrix}.
$$


::: pf-proof

Let
$$
n=(1,0,1)^t.
$$
Reflection across the plane $n^\perp$ is
$$
S(v)=v-2\frac{v\cdot n}{n\cdot n}n.
$$
Since $n\cdot n=2$,
$$
[S]
=
I-nn^t
=
I-
\begin{pmatrix}
1&0&1\\
0&0&0\\
1&0&1
\end{pmatrix},
$$
which is the displayed matrix.

:::

:::

::: {.pf-step #s1-5}

The matrix of $S\circ T$ in the standard basis is
$$
\boxed{
[S\circ T]
=
\begin{pmatrix}
0&0&-1\\
0&1&0\\
-1&0&0
\end{pmatrix}
Q
\begin{pmatrix}
\frac12&-\frac{\sqrt3}{2}&0\\
\frac{\sqrt3}{2}&\frac12&0\\
0&0&1
\end{pmatrix}
Q^t
},
$$
where $Q$ and $Q^t=Q^{-1}$ are the explicit matrices in step [](#s1-3){.pf-ref}.


::: pf-proof

Matrix multiplication represents composition in the order
$$
[S\circ T]=[S][T].
$$
Substitute step [](#s1-3){.pf-ref} for $[T]$ and step [](#s1-4){.pf-ref} for $[S]$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested standard-basis matrix and step [](#s1-3){.pf-ref} explicitly determines the inverse arising from the change of basis.

:::

:::

:::
