---
schema: qual/card@1
id: P-TRIV-LA31
kind: problem
title: Exponentials of the infinitesimal rotation generators of $SO(3)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 31, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Define the matrix exponential $e ^ { A }$ of a matrix A as follows: $e ^ { A } \ = \ \sum _ { n = 0 } ^ { \infty } { \frac { A ^ { n } } { n ! } }$ Consider the following matrices

$$
M _ { x } = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] } , M _ { y } = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \end{array} \right] } , M _ { z } = { \left[ \begin{array} { l l l } { 0 } & { - 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } .\tag{7}
$$

(a) Write $\mathrm { T r } M _ { i } , M _ { i } ^ { T } , i = x , y , z$

(b) Calculate $e ^ { \theta M _ { x } } , e ^ { \theta M _ { y } } , e ^ { \theta M _ { z } }$ , where $\theta \in [ 0 , 2 \pi )$

(c) Give a geometrical interpretation of the transformations $e ^ { \theta M _ { i } } , i = x , y , z$ acting on the vectors in $\RR ^ { 3 }$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For each $i\in\{x,y,z\}$,
$$
\boxed{\operatorname{Tr}M_i=0}.
$$


::: pf-proof

Each displayed matrix has zero diagonal.

:::

:::

::: {.pf-step #s1-2}

For each $i\in\{x,y,z\}$,
$$
\boxed{M_i^T=-M_i}.
$$


::: pf-proof

Each matrix is skew-symmetric by inspection: transposition exchanges the two
nonzero off-diagonal entries and reverses their signs.

:::

:::

::: {.pf-step #s1-3}

Part (a) follows.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give the trace and transpose of all three generators.

:::

:::

::: {.pf-step #s1-4}

For each generator $M_i$,
$$
M_i^3=-M_i.
$$


::: pf-proof

For example,
$$
M_x^2
=
\begin{pmatrix}
0&0&0\\
0&-1&0\\
0&0&-1
\end{pmatrix},
$$
so
$$
M_x^3=M_xM_x^2=-M_x.
$$
The computations for $M_y$ and $M_z$ are identical after permuting
coordinates.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
e^{\theta M_i}
=
I+\sin\theta,M_i+(1-\cos\theta)M_i^2.
}
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
M_i^{2k+1}=(-1)^kM_i
$$
and, for $k\geq1$,
$$
M_i^{2k}=(-1)^{k-1}M_i^2.
$$
Substitute these identities into the power series for the exponential. The odd
terms sum to
$$
\sin\theta,M_i,
$$
and the nonconstant even terms sum to
$$
(1-\cos\theta)M_i^2.
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
e^{\theta M_x}
=
\begin{pmatrix}
1&0&0\\
0&\cos\theta&-\sin\theta\\
0&\sin\theta&\cos\theta
\end{pmatrix}.
}
$$


::: pf-proof

Substitute $M_x$ and $M_x^2$ into step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\boxed{
e^{\theta M_y}
=
\begin{pmatrix}
\cos\theta&0&\sin\theta\\
0&1&0\\
-\sin\theta&0&\cos\theta
\end{pmatrix}.
}
$$


::: pf-proof

Substitute $M_y$ and $M_y^2$ into step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

One has
$$
\boxed{
e^{\theta M_z}
=
\begin{pmatrix}
\cos\theta&-\sin\theta&0\\
\sin\theta&\cos\theta&0\\
0&0&1
\end{pmatrix}.
}
$$


::: pf-proof

Substitute $M_z$ and $M_z^2$ into step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Part (b) follows.


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} give all three exponentials.

:::

:::

::: {.pf-step #s1-10}

The transformation $e^{\theta M_x}$ is rotation by angle $\theta$
about the $x$-axis.


::: pf-proof

Step [](#s1-6){.pf-ref} fixes the $x$-coordinate and rotates the $(y,z)$-coordinates by the
standard planar rotation matrix.

:::

:::

::: {.pf-step #s1-11}

The transformations $e^{\theta M_y}$ and $e^{\theta M_z}$ are rotations
by angle $\theta$ about the $y$- and $z$-axes, respectively.


::: pf-proof

Step [](#s1-7){.pf-ref} fixes the $y$-coordinate and rotates the $(z,x)$-plane, while step
[](#s1-8){.pf-ref} fixes the $z$-coordinate and rotates the $(x,y)$-plane.

:::

:::

::: {.pf-step #s1-12}

Part (c) follows.


::: pf-proof

Steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref} give the geometrical interpretation.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-9){.pf-ref}, and [](#s1-12){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
