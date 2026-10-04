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

(c) Give a geometrical interpretation of the transformations $e ^ { \theta M _ { i } } , i = x , y , z$ acting on the vectors in $\mathbb { R } ^ { 3 }$
:::

::: {.solution}
<1>1. For each $i\in\{x,y,z\}$,
$$
\boxed{\operatorname{Tr}M_i=0}.
$$

::: {.proof}
Each displayed matrix has zero diagonal.
:::

<1>2. For each $i\in\{x,y,z\}$,
$$
\boxed{M_i^T=-M_i}.
$$

::: {.proof}
Each matrix is skew-symmetric by inspection: transposition exchanges the two
nonzero off-diagonal entries and reverses their signs.
:::

<1>3. Part (a) follows.

::: {.proof}
Steps <1>1--<1>2 give the trace and transpose of all three generators.
:::

<1>4. For each generator $M_i$,
$$
M_i^3=-M_i.
$$

::: {.proof}
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

<1>5. Therefore
$$
\boxed{
e^{\theta M_i}
=
I+\sin\theta,M_i+(1-\cos\theta)M_i^2.
}
$$

::: {.proof}
By step <1>4,
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

<1>6. One has
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

::: {.proof}
Substitute $M_x$ and $M_x^2$ into step <1>5.
:::

<1>7. One has
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

::: {.proof}
Substitute $M_y$ and $M_y^2$ into step <1>5.
:::

<1>8. One has
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

::: {.proof}
Substitute $M_z$ and $M_z^2$ into step <1>5.
:::

<1>9. Part (b) follows.

::: {.proof}
Steps <1>6--<1>8 give all three exponentials.
:::

<1>10. The transformation $e^{\theta M_x}$ is rotation by angle $\theta$
about the $x$-axis.

::: {.proof}
Step <1>6 fixes the $x$-coordinate and rotates the $(y,z)$-coordinates by the
standard planar rotation matrix.
:::

<1>11. The transformations $e^{\theta M_y}$ and $e^{\theta M_z}$ are rotations
by angle $\theta$ about the $y$- and $z$-axes, respectively.

::: {.proof}
Step <1>7 fixes the $y$-coordinate and rotates the $(z,x)$-plane, while step
<1>8 fixes the $z$-coordinate and rotates the $(x,y)$-plane.
:::

<1>12. Part (c) follows.

::: {.proof}
Steps <1>10--<1>11 give the geometrical interpretation.
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>3, <1>9, and <1>12 establish parts (a), (b), and (c), respectively.
:::
:::
