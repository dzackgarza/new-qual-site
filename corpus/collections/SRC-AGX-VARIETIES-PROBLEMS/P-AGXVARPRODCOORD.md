---
schema: qual/card@1
id: P-AGXVARPRODCOORD
kind: problem
title: The coordinate ring of a product of affine varieties is a tensor product
classification:
  areas:
  - algebraic-geometry
  topics:
  - Products of Varieties
  - Tensor Products
  - Coordinate Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the corresponding clause of Zaidenberg Exercises 2.7 in the recorded
    source. Over the standing field k=C it asks that the Cartesian product of
    two affine varieties be an affine variety and that its coordinate ring be
    the tensor product of the coordinate rings.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced structure-sheaf-looking notation O_X by the source's global
    coordinate-ring notation O(X), and made the affine embeddings and field C
    explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked closedness and irreducibility of the point-set product fibrewise,
    then identified its vanishing ideal by coefficient expansion against a
    linearly independent family in O(Y). Cross-checked against
    P-AGH315AFFPRODUCT.
---

::: {.problem}
Let
$$
X\subseteq\AA^n_\CC,
\qquad
Y\subseteq\AA^m_\CC
$$
be affine varieties. Show that
$$
X\cross Y\subseteq\AA^{n+m}_\CC
$$
is an affine variety and that
$$
\mco(X\cross Y)
\cong
\mco(X)\tensor_\CC\mco(Y).
$$
:::

::: {.solution}
Write coordinates on $\AA^{n+m}_\CC$ as
$$
(x_1,\ldots,x_n,y_1,\ldots,y_m).
$$

<1>1. The subset $X\cross Y$ is Zariski closed in $\AA^{n+m}_\CC$.

::: {.proof}
Let
$$
I(X)\subseteq\CC[x_1,\ldots,x_n],
\qquad
I(Y)\subseteq\CC[y_1,\ldots,y_m]
$$
be the vanishing ideals. In
$$
S=\CC[x_1,\ldots,x_n,y_1,\ldots,y_m]
$$
consider
$$
J=I(X)S+I(Y)S.
$$
A point $(x,y)$ lies in $V(J)$ exactly when every polynomial in $I(X)$
vanishes at $x$ and every polynomial in $I(Y)$ vanishes at $y$. Hence
$$
V(J)=X\cross Y.
$$
Thus $X\cross Y$ is closed.
:::

<1>2. If $Z\subseteq X\cross Y$ is closed, then
$$
X_Z
=
\{x\in X:\{x\}\cross Y\subseteq Z\}
$$
is closed in $X$.

::: {.proof}
Choose finitely many polynomials
$$
F_1,\ldots,F_r\in S
$$
whose common zero set on $X\cross Y$ is $Z$. Fix one such polynomial $F$.
Its image in
$$
\CC[x_1,\ldots,x_n]\tensor_\CC\mco(Y)
$$
can be written
$$
\sum_{j=1}^N a_j(x)e_j
$$
with
$$
e_1,\ldots,e_N\in\mco(Y)
$$
$\CC$-linearly independent.

For a fixed $x\in X$, the polynomial $F(x,-)$ vanishes on all of $Y$
exactly when its class in $\mco(Y)$ is zero, that is,
$$
\sum_{j=1}^N a_j(x)e_j=0.
$$
Linear independence gives
$$
a_1(x)=\cdots=a_N(x)=0.
$$
Thus the condition that $F$ vanish on the whole fibre $\{x\}\cross Y$ is
Zariski closed in $X$. Intersecting these closed conditions for
$F_1,\ldots,F_r$ gives $X_Z$.
:::

<1>3. The closed subset $X\cross Y$ is irreducible.

::: {.proof}
Suppose
$$
X\cross Y=Z_1\union Z_2
$$
with $Z_1$ and $Z_2$ closed. For $i=1,2$, put
$$
X_i
=
\{x\in X:\{x\}\cross Y\subseteq Z_i\}.
$$
By step <1>2, each $X_i$ is closed in $X$.

Fix $x\in X$. The fibre
$$
\{x\}\cross Y
$$
is isomorphic to the irreducible variety $Y$, and it is the union of its
closed intersections with $Z_1$ and $Z_2$. Hence the whole fibre is contained
in one $Z_i$. Therefore
$$
X=X_1\union X_2.
$$
Since $X$ is irreducible, either $X=X_1$ or $X=X_2$. In the first case every
fibre lies in $Z_1$, so
$$
X\cross Y=Z_1;
$$
similarly in the second case
$$
X\cross Y=Z_2.
$$
Thus $X\cross Y$ is irreducible.
:::

<1>4. The natural homomorphism
$$
\mco(X)\tensor_\CC\mco(Y)
\longrightarrow
\mco(X\cross Y)
$$
is an isomorphism.

::: {.proof}
The quotient map
$$
S
\longrightarrow
\mco(X)\tensor_\CC\mco(Y)
$$
has kernel
$$
I(X)S+I(Y)S.
$$
By step <1>1 this ideal is contained in
$$
I(X\cross Y).
$$

For the reverse inclusion, let
$$
F\in I(X\cross Y).
$$
Write its image in the tensor product as
$$
\overline F
=
\sum_{j=1}^N a_j\tensor b_j,
$$
where
$$
b_1,\ldots,b_N\in\mco(Y)
$$
are $\CC$-linearly independent. For every $x\in X$, vanishing of $F$ on
the fibre $\{x\}\cross Y$ gives
$$
\sum_{j=1}^N a_j(x)b_j=0
$$
in $\mco(Y)$. Linear independence implies
$$
a_j(x)=0
$$
for every $j$ and every $x\in X$. Thus each $a_j$ is zero in $\mco(X)$,
so
$$
\overline F=0.
$$
Hence
$$
I(X\cross Y)=I(X)S+I(Y)S.
$$
Taking quotients gives
$$
\boxed{
\mco(X\cross Y)
\cong
\mco(X)\tensor_\CC\mco(Y).
}
$$
:::

<1>5. The product $X\cross Y$ is an affine variety.

::: {.proof}
Step <1>1 shows that it is Zariski closed in affine space, and step <1>3
shows that it is irreducible. An irreducible Zariski-closed subset of affine
space is an affine variety.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves that $X\cross Y$ is an affine variety, and step <1>4
computes its coordinate ring.
:::
:::
