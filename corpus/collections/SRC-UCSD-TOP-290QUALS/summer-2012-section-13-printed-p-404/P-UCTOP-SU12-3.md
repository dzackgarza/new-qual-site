---
schema: qual/card@1
id: P-UCTOP-SU12-3
kind: problem
title: Homology of cube with opposite faces glued by 180-degree rotation
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $X$ be the space obtained by gluing opposite pairs of faces of a standard cube $I^3$ via 180 degree rotations.
Compute the homology $H_*(X; \mathbb{Z})$.

::: {.solution}
<1>1. Under the three half-turn face pairings, the eight cube vertices fall into four equivalence classes, the twelve edges into six classes, and the six faces into three classes. Thus the quotient has cellular chain groups
$$
0\to \mathbb Z\xrightarrow{\partial_3}\mathbb Z^3\xrightarrow{\partial_2}\mathbb Z^6\xrightarrow{\partial_1}\mathbb Z^4\to0.
$$
::: {.proof}
Write a cube vertex as $(x,y,z)\in\{0,1\}^3$. The pairing of the two faces perpendicular to the $x$-axis is
$$(0,y,z)\sim(1,1-y,1-z),$$
and cyclically for the other two coordinate directions. The resulting vertex classes are
$$
\{000,111\},\quad \{001,110\},\quad \{010,101\},\quad \{011,100\}.
$$
For each coordinate direction, the four parallel edges split into two orbits under the other two face pairings, giving six edge classes total. Each opposite pair of square faces gives one $2$-cell, and the cube interior gives one $3$-cell.
:::

<1>2. Choose oriented edge classes $e_0,\dots,e_5$ so that $e_0,e_2,e_4$ form a spanning tree of the quotient $1$-skeleton. With suitable orientations of the three quotient faces, their cellular boundaries are the columns of
$$
\partial_2=
\begin{pmatrix}
0&1&1\\
0&-1&1\\
1&0&-1\\
-1&0&-1\\
-1&-1&0\\
1&-1&0
\end{pmatrix}.
$$
::: {.proof}
Take representatives of the six edge classes to be the positive coordinate edges
$$
\begin{aligned}
e_0&:000\to100,&e_1&:001\to101,\\
e_2&:000\to010,&e_3&:001\to011,\\
e_4&:000\to001,&e_5&:010\to011.
\end{aligned}
$$
The half-turn identifications reverse the orientations of the opposite representative edges. Tracing the boundaries of the faces $x=0$, $y=0$, and $z=0$ gives respectively
$$
e_2-e_3-e_4+e_5,\qquad e_0-e_1-e_4-e_5,\qquad e_0+e_1-e_2-e_3,
$$
which are exactly the displayed columns.
:::

<1>3. Collapsing the spanning tree $e_0,e_2,e_4$ identifies
$$
H_1(X;\mathbb Z)\cong \operatorname{coker}
\begin{pmatrix}
0&-1&1\\
-1&0&-1\\
1&-1&0
\end{pmatrix}.
$$
::: {.proof}
After collapsing the tree, the three non-tree edges $e_1,e_3,e_5$ form a basis for the first homology of the quotient $1$-skeleton. The attaching maps of the three $2$-cells have coordinates given by the corresponding three rows of the matrix in <1>2.
:::

<1>4. The Smith normal form of this $3\times3$ matrix is
$$
\operatorname{diag}(1,1,2),
$$
so
$$
H_1(X;\mathbb Z)\cong\mathbb Z/2.
$$
::: {.proof}
The matrix has determinant $2$, and one of its $2\times2$ minors is $\pm1$. Hence its Smith invariants are $1,1,2$.
:::

<1>5. The map $\partial_2$ is injective, so $H_2(X;\mathbb Z)=0$ once $\partial_3=0$.
::: {.proof}
The $3\times3$ minor used in <1>3 has determinant $2\ne0$, hence $\partial_2$ has rank $3$, equal to the rank of its domain.
:::

<1>6. The cellular boundary $\partial_3$ is zero.
::: {.proof}
For each quotient $2$-cell, the two opposite cube faces occur in the boundary of the $3$-cell with opposite incidence signs. The half-turn within the face is orientation-preserving, so the two contributions cancel. Thus every coefficient of $\partial_3$ is zero.
:::

<1>7. Therefore
$$
\boxed{H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,3,\\
\mathbb Z/2,&i=1,\\
0,&i=2\text{ or }i>3.
\end{cases}}
$$
::: {.proof}
The quotient is connected, giving $H_0\cong\mathbb Z$. Combine <1>4--<1>6 with the cellular chain complex in <1>1.
:::
:::
