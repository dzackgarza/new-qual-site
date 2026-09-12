---
schema: qual/card@1
id: P-UCTOP-FA12-2
kind: problem
title: Homology of cube with opposite faces glued by 90-degree rotation
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $X$ be the space obtained by gluing opposite pairs of faces of a standard cube $I^3$ via 90 degree rotations.
Compute the homology $H_*(X; \mathbb{Z})$.

::: {.solution}
<1>1. Under the quarter-turn face pairings, the quotient CW structure has two $0$-cells, four $1$-cells, three $2$-cells, and one $3$-cell.
::: {.proof}
The quarter-turn identifications partition the eight vertices into two classes and the twelve edges into four classes; opposite faces are paired, giving three $2$-cells, while the cube interior gives one $3$-cell.
:::

<1>2. With suitable orientations of the cells, the cellular boundary maps are
$$
\partial_1=
\begin{pmatrix}
-1&1&-1&1\\
1&-1&1&-1
\end{pmatrix},
\qquad
\partial_2=
\begin{pmatrix}
1&1&1\\
1&1&-1\\
1&-1&-1\\
1&-1&1
\end{pmatrix}.
$$
::: {.proof}
Orient the four edge classes alternately between the two vertex classes. Tracing one representative of each pair of opposite faces through the quarter-turn identifications yields the three columns of $\partial_2$. These are the standard cellular incidence matrices for the cube with right-handed one-quarter-twist face pairings.
:::

<1>3. The Smith normal forms are
$$
\partial_1\sim\begin{pmatrix}1&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
\partial_2\sim
\begin{pmatrix}
1&0&0\\
0&2&0\\
0&0&2\\
0&0&0
\end{pmatrix}.
$$
::: {.proof}
These follow by integral row and column operations. In particular, $\partial_1$ has rank $1$, while $\partial_2$ has rank $3$ with invariant factors $1,2,2$.
:::

<1>4. The top cellular boundary is zero: $\partial_3=0$.
::: {.proof}
For each quotient face, the two opposite cube faces contribute with opposite local degrees to the attaching map of the $3$-cell. The quarter-turn is orientation-preserving on the face, so the contributions cancel.
:::

<1>5. Hence
$$
\boxed{H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,3,\\
\mathbb Z/2\oplus\mathbb Z/2,&i=1,\\
0,&i=2\text{ or }i>3.
\end{cases}}
$$
::: {.proof}
The Smith form of $\partial_1$ gives $H_0\cong\mathbb Z$. Since $\ker\partial_1$ has rank $3$ and the image of $\partial_2$ has index $4$ in it, $H_1\cong(\mathbb Z/2)^2$. The map $\partial_2$ is injective, so $H_2=0$, and <1>4 gives $H_3\cong\mathbb Z$.
:::
:::
