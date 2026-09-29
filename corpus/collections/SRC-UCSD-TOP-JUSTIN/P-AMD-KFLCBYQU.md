---
schema: qual/card@1
id: P-AMD-KFLCBYQU
kind: problem
title: Order-6 homeomorphism of the torus fixing the origin
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $x_0$ be the image of $0$, show that there is an order 6 homeomorphism $f: T \to T$ fixing $x_0$.
Find a representation of $f_*$ as a matrix, and find its determinant.
:::

::: {.solution}

::: pf

::: pf-step

Identify $T$ with $\RR^2/\ZZ^2$, with $x_0$ the image of $0$.

::: pf-proof

This is the standard linear model of the torus.

:::

:::

::: pf-step

Let
$$
B=\begin{pmatrix}0&-1\\1&1\end{pmatrix}\in SL_2(\ZZ)
$$
and define
$$
f([x,y])=[-y,x+y].
$$

::: pf-proof

Because $B\ZZ^2=\ZZ^2$, the integral linear automorphism $B:\RR^2\to\RR^2$ descends to a homeomorphism of $\RR^2/\ZZ^2$.

:::

:::

::: pf-step

The map $f$ fixes $x_0$.

::: pf-proof

$B(0,0)=(0,0)$.

:::

:::

::: pf-step

One has
$$
B^2=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},
\qquad
B^3=-I,
\qquad
B^6=I.
$$

::: pf-proof

These identities follow by direct matrix multiplication.

:::

:::

::: pf-step

No positive power $B^j$ with $1\le j<6$ is the identity, so $f$ has order exactly $6$.

::: pf-proof

The matrices $B$ and $B^2$ displayed above are not $I$, while $B^3=-I\ne I$. Then $B^4=-B\ne I$ and $B^5=-B^2\ne I$. Together with $B^6=I$, this proves that the order is $6$.

:::

:::

::: pf-step

In the standard basis of $H_1(T;\ZZ)\cong\ZZ^2$, the induced map is represented by
$$
\boxed{f_*=B=\begin{pmatrix}0&-1\\1&1\end{pmatrix}}.
$$

::: pf-proof

The standard generators of $H_1(T;\ZZ)$ are the images of the coordinate vectors in $\ZZ^2$, and the induced map on these generators is exactly the lattice automorphism $B$.

:::

:::

::: pf-step

Its determinant is
$$\boxed{\det f_*=1}.$$

::: pf-proof

$\det B=0\cdot1-(-1)\cdot1=1$.

:::

:::

:::

:::
