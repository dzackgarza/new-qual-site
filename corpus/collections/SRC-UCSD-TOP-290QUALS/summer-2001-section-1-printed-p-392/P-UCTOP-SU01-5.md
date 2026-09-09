---
schema: qual/card@1
id: P-UCTOP-SU01-5
kind: problem
title: Fundamental group and homology of pentagon identification space
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

Let $X$ be the result of gluing up the edges of two solid pentagons in pairs, according to the picture shown in the source.
Compute the fundamental group and the homology groups of $X$.
Is it a manifold?

::: {.solution}
<1>1. Reading the arrows in the source diagram clockwise from the top vertex, the two pentagons have attaching words
$$
w_1=abc\,d^{-1}e^{-1},
\qquad
w_2=adb\,e^{-1}c^{-1}.
$$
::: {.proof}
For the left pentagon, the arrows on the upper-right, lower-right, and bottom edges agree with clockwise traversal, while those on the lower-left and upper-left edges oppose it; the labels are respectively $a,b,c,d,e$. For the right pentagon, the corresponding clockwise labels are $a,d,b,e,c$ with the same arrow pattern. Hence the displayed words.
:::

<1>2. All ten polygon vertices are identified to a single vertex in the quotient.
::: {.proof}
Let the left vertices be $L_0,\dots,L_4$ clockwise from the top and the right vertices $R_0,\dots,R_4$. Preserving the edge arrows gives
$$
\begin{aligned}
a:&\quad L_0\sim R_0,\ L_1\sim R_1,\\
b:&\quad L_1\sim R_2,\ L_2\sim R_3,\\
c:&\quad L_2\sim R_0,\ L_3\sim R_4,\\
d:&\quad L_4\sim R_1,\ L_3\sim R_2,\\
e:&\quad L_0\sim R_4,\ L_4\sim R_3.
\end{aligned}
$$
These relations put every $L_i$ and every $R_i$ in one equivalence class.
:::

<1>3. Thus $X$ has a CW structure with one $0$-cell, five $1$-cells $a,b,c,d,e$, and two $2$-cells attached by $w_1,w_2$.
::: {.proof}
The five paired edge classes give the five $1$-cells, <1>2 gives one vertex, and the interiors of the two pentagons give the two $2$-cells.
:::

<1>4. Therefore
$$
\pi_1(X)\cong
\left\langle a,b,c,d,e\ \middle|\ abc d^{-1}e^{-1},\ adb e^{-1}c^{-1}\right\rangle.
$$
::: {.proof}
Apply the standard CW presentation of the fundamental group: one generator for each $1$-cell and one relator for each $2$-cell attaching word from <1>1.
:::

<1>5. The cellular chain complex in positive degrees is
$$
0\longrightarrow\mathbb Z^2
\xrightarrow{\partial_2}
\mathbb Z^5
\xrightarrow{0}
\mathbb Z
\longrightarrow0,
$$
where, in the ordered basis $(a,b,c,d,e)$,
$$
\partial_2=
\begin{pmatrix}
1&1\\
1&1\\
1&-1\\
-1&1\\
-1&-1
\end{pmatrix}.
$$
::: {.proof}
The cellular boundary of a $2$-cell records the exponent sum of each oriented $1$-cell in its attaching word. The two columns are therefore the exponent-sum vectors of $w_1$ and $w_2$. Since there is one vertex, $\partial_1=0$.
:::

<1>6. We have
$$
H_2(X)=0,
\qquad
H_1(X)\cong\mathbb Z^3\oplus\mathbb Z/2,
\qquad
H_0(X)\cong\mathbb Z.
$$
::: {.proof}
The two columns of $\partial_2$ are linearly independent, so $\ker\partial_2=0$. For the cokernel, the gcd of all entries is $1$, while the gcd of the $2\times2$ minors is $2$ (for example, the minor using rows $a,c$ has determinant $-2$, and every nonzero $2\times2$ minor is $\pm2$). Hence the Smith normal form has nonzero diagonal entries $1,2$. Thus
$$
\operatorname{coker}\partial_2\cong\mathbb Z^{5-2}\oplus\mathbb Z/2.
$$
Connectedness gives $H_0\cong\mathbb Z$.
:::

<1>7. The space $X$ is a closed connected $2$-manifold.
::: {.proof}
Every point in the interior of a polygon has a disk neighborhood, and every point in the interior of an edge has a disk neighborhood because each edge is paired with exactly one other edge. At the unique vertex, the link is obtained from the ten corner intervals by gluing their endpoints according to the edge pairings. Every endpoint is paired exactly once, so the link is a disjoint union of circles; <1>2 shows all ten corners lie in one vertex-equivalence class, hence this link is connected and therefore is a single circle. Thus the vertex also has a disk neighborhood. No boundary remains after all edges are paired.
:::

<1>8. In fact, $X$ is the closed nonorientable surface of genus $4$.
::: {.proof}
Its Euler characteristic from <1>3 is
$$
\chi(X)=1-5+2=-2.
$$
By <1>6, $H_2(X;\mathbb Z)=0$, so the closed connected surface is nonorientable. A closed nonorientable surface of genus $k$ has Euler characteristic $2-k$, hence $2-k=-2$ and $k=4$. This also agrees with
$$
H_1(N_4;\mathbb Z)\cong\mathbb Z^3\oplus\mathbb Z/2.
$$
:::

<1>9. Consequently one may also identify
$$
\pi_1(X)\cong
\langle x_1,x_2,x_3,x_4\mid x_1^2x_2^2x_3^2x_4^2=1\rangle.
$$
::: {.proof}
By <1>7--<1>8, $X$ is homeomorphic to the standard closed nonorientable genus-$4$ surface, whose usual polygon presentation gives the displayed fundamental-group presentation.
:::
:::

