---
schema: qual/card@1
id: P-TRIV-LA17
kind: problem
title: Which reflections in $\RR^n$ are rotations
classification:
  areas: [prelim]
  topics:
  - Reflections
  - Rotations
  - Orthogonal Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 17, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the reflection maps in $\RR^n$. The reflection across the origin transforms every vector $\vec{x} \in \RR^n$ to $-\vec{x}$. The reflection across one of the basis axis $Oi$ inverts all coordinates of $\vec{x}$ except $x_i$. Similarly, one can define the reflections across the planes in $\RR^3$ and higher dimensional hyperplanes in $\RR^n$, $n > 3$. Some of these reflections are equivalent to rotations around the origin $O$, others are not.

(a) Observe that in $\RR^2$ the central reflection is equivalent to the rotation by an angle $\pi$ around $O$. Show that no reflections across a line crossing $O$ can be achieved by any rotation.

(b) In $\RR^3$, find if one can achieve by some rotation around $O$

(i) the reflection across $O$,

(ii) the reflection across an arbitrary line crossing $O$,

(iii) the reflection across an arbitrary plane crossing $O$.

(c) In $\RR^n$, formulate and prove a general statement about the existence of rotations that perform the reflection across a given $m$-dimensional plane, $m = 0, 1, \ldots, n - 1$, crossing the origin (where $m = 1$ corresponds to the line, and $m = 0$ to the point).
:::

::: {.solution}

Here “rotation” means an orientation-preserving orthogonal transformation,
that is, an element of $SO(n)$.

::: pf

::: pf-step

Reflection across an $m$-dimensional linear subspace $U\subseteq\RR^n$
acts as
$$
R_U
=
I_U\oplus(-I_{U^\perp}).
$$


::: pf-proof

By definition, vectors in $U$ are fixed and vectors perpendicular to $U$ have
their sign reversed.

:::

:::

::: {.pf-step #s1-2}

Its determinant is
$$
\boxed{\det R_U=(-1)^{n-m}}.
$$


::: pf-proof

Choose an orthonormal basis adapted to
$$
\RR^n=U\oplus U^\perp.
$$
In that basis,
$$
R_U=
\operatorname{diag}(
\underbrace{1,\ldots,1}_{m},
\underbrace{-1,\ldots,-1}_{n-m}
).
$$
The determinant is the product of these diagonal entries.

:::

:::

::: {.pf-step #s1-3}

In $\RR^2$, reflection through the origin is rotation by $\pi$.


::: pf-proof

Here $m=0$ and
$$
R_{\{0\}}=-I_2
=
\begin{pmatrix}
-1&0\\
0&-1
\end{pmatrix},
$$
which is exactly the matrix of a rotation through angle $\pi$.

:::

:::

::: {.pf-step #s1-4}

In $\RR^2$, reflection across any line through the origin is not a
rotation.


::: pf-proof

Such a line has dimension $m=1$, so step [](#s1-2){.pf-ref} gives
$$
\det R_U=-1.
$$
Every planar rotation has determinant $1$. Hence no rotation can equal this
reflection.

:::

:::

::: {.pf-step #s1-5}

Part (a) follows.


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give the two assertions.

:::

:::

::: {.pf-step #s1-6}

In $\RR^3$, central reflection through the origin is not a
rotation.


::: pf-proof

Here $m=0$, so
$$
\det R=(-1)^3=-1
$$
by step [](#s1-2){.pf-ref}. A rotation belongs to $SO(3)$ and has determinant $1$.

:::

:::

::: {.pf-step #s1-7}

In $\RR^3$, reflection across a line through the origin is a
rotation by $\pi$ around that line.


::: pf-proof

Let the line be $U$. Then
$$
\RR^3=U\oplus U^\perp,
$$
where $U^\perp$ is a $2$-plane. The reflection fixes $U$ and acts as $-I$ on
$U^\perp$. On a $2$-plane, $-I$ is rotation by $\pi$. Hence the whole map is
the usual rotation by $\pi$ about the axis $U$.

:::

:::

::: {.pf-step #s1-8}

In $\RR^3$, reflection across a plane through the origin is not a
rotation.


::: pf-proof

Here $m=2$, so step [](#s1-2){.pf-ref} gives
$$
\det R=-1.
$$
Thus the reflection is orientation-reversing and cannot lie in $SO(3)$.

:::

:::

::: {.pf-step #s1-9}

Part (b) follows.


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} settle the point, line, and plane cases.

:::

:::

::: {.pf-step #s1-10}

If $n-m$ is odd, reflection across an $m$-plane cannot be a rotation.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\det R_U=(-1)^{n-m}=-1.
$$
Every rotation has determinant $1$.

:::

:::

::: {.pf-step #s1-11}

If $n-m$ is even, reflection across an $m$-plane is a rotation in the
general $SO(n)$ sense.


::: pf-proof

Write
$$
n-m=2r.
$$
Choose an orthonormal basis of $U^\perp$ grouped into mutually orthogonal
$2$-planes
$$
P_1\oplus\cdots\oplus P_r.
$$
On each $P_j$, rotate by $\pi$, and fix $U$ pointwise. The resulting
orthogonal transformation acts as $-I$ on every $P_j$, hence as $-I$ on all
of $U^\perp$, while acting as $I$ on $U$. It is therefore exactly $R_U$.

Each $2$-plane rotation has determinant $1$, so their orthogonal direct sum
has determinant $1$ and lies in $SO(n)$.

:::

:::

::: {.pf-step #s1-12}

Therefore reflection across an $m$-dimensional plane through the origin
is realizable by a rotation if and only if
$$
\boxed{n-m\text{ is even}.}
$$


::: pf-proof

Step [](#s1-10){.pf-ref} proves necessity and step [](#s1-11){.pf-ref} proves sufficiency.

:::

:::

::: {.pf-step #s1-13}

Part (c) follows.


::: pf-proof

Step [](#s1-12){.pf-ref} is the requested general statement.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} and [](#s1-9){.pf-ref}, and [](#s1-13){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
