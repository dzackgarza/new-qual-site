---
schema: qual/card@1
id: P-WESTOP14-6
kind: problem
title: Fundamental groups, homology, and manifold status of three hexagon identification spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The Markdown extraction loses the diagram, but direct inspection of page 1 of assets/attachments/topology_2006-2014.pdf recovers all edge labels and arrows. Clockwise from the top edge, the first two words are abacb^{-1}c^{-1} and abca^{-1}cb; the third has three a-edges and three b-edges with word ababb^{-1}a^{-1}.
---

::: {.problem}
Consider three hexagonal disks with boundary edges identified according to the
arrows in the source diagram. Traversing clockwise from the top edge, the
first two attaching words are
$$
w_1=abacb^{-1}c^{-1},
\qquad
w_2=abca^{-1}cb.
$$
In the third diagram the three edges labeled $a$ are all identified respecting
their arrows, and likewise the three edges labeled $b$; its clockwise word is
$$
w_3=ababb^{-1}a^{-1}.
$$

For each quotient space:

1. Compute the fundamental group.
2. Compute the homology groups.
3. Determine which of the spaces are manifolds.
:::

::: {.solution}

Denote the three quotient spaces by
$$
X_1,
\qquad
X_2,
\qquad
X_3.
$$

::: pf

::: {.pf-step #s1-1}

In the first diagram all six polygon vertices are identified to one
vertex.


::: pf-proof

Number the boundary vertices
$$
v_0,v_1,\ldots,v_5
$$
clockwise, with the top edge running from
$$
v_0
$$
to
$$
v_1.
$$

The two $a$-edges are both traversed in the arrow direction, so their
arrow-starts are identified and their arrow-ends are identified:
$$
v_0\sim v_2,
\qquad
v_1\sim v_3.
$$
The $b$-pair has opposite boundary signs, and the $c$-pair likewise.
Their endpoint identifications join the two displayed classes and the
remaining vertices.
Taking the transitive closure gives
$$
v_0\sim v_1\sim\cdots\sim v_5.
$$

:::

:::

::: pf-step

Thus $X_1$ has a CW structure with one $0$-cell, three $1$-cells
$a,b,c$, and one $2$-cell attached by
$$
w_1=abacb^{-1}c^{-1}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives the single vertex.
Each pair of identified polygon edges gives one $1$-cell, and the polygon
interior gives one $2$-cell.
The attaching map is read directly from the boundary word.

:::

:::

::: {.pf-step #s1-3}

The fundamental group of $X_1$ is
$$
\boxed{
\pi_1(X_1)
\cong
\left\langle
a,b,c
\mid
abacb^{-1}c^{-1}
\right\rangle.}
$$


::: pf-proof

The $1$-skeleton is a wedge of the three loops
$$
a,b,c.
$$
Van Kampen's theorem says that attaching the $2$-cell imposes exactly the
relation represented by its attaching word.

:::

:::

::: {.pf-step #s1-4}

The cellular chain complex of $X_1$ is
$$
0
\longrightarrow
\ZZ
\xrightarrow{\partial_2}
\ZZ^3
\xrightarrow{0}
\ZZ
\longrightarrow
0,
$$
with
$$
\boxed{
\partial_2(1)=(2,0,0)}
$$
in the basis
$$
(a,b,c).
$$


::: pf-proof

For a one-vertex presentation complex, the cellular boundary of the
$2$-cell is given by the exponent sums of the oriented $1$-cells in the
attaching word.

In
$$
abacb^{-1}c^{-1},
$$
the exponent sum of
$$
a
$$
is
$$
2,
$$
while the exponent sums of
$$
b
$$
and
$$
c
$$
are
$$
0.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
H_0(X_1;\ZZ)\cong\ZZ,
\quad
H_1(X_1;\ZZ)
\cong
\ZZ^2\oplus\ZZ/2,
\quad
H_k(X_1;\ZZ)=0
\text{ for }k\ge2.}
$$


::: pf-proof

The map
$$
\partial_2:\ZZ\to\ZZ^3
$$
is injective, so
$$
H_2(X_1)=0.
$$
Also
$$
H_1(X_1)
=
\ZZ^3/
\langle(2,0,0)\rangle
\cong
\ZZ^2\oplus\ZZ/2.
$$
The complex is connected, so
$$
H_0(X_1)\cong\ZZ.
$$
There are no cells above dimension
$$
2.
$$

:::

:::

::: {.pf-step #s1-6}

The space $X_1$ is a closed $2$-manifold; in fact it is the
nonorientable surface of genus $3$.


::: pf-proof

Every boundary edge is paired with exactly one other boundary edge.
The edge pairings give ordinary disk neighborhoods at interior points of
edges, and the link of the single quotient vertex is a connected
$2$-regular graph, hence a circle.
Thus the quotient is a closed surface.

Its Euler characteristic is
$$
\chi(X_1)
=
1-3+1
=
-1.
$$
The two occurrences of
$$
a
$$
have the same boundary orientation, so the surface is nonorientable.
A closed nonorientable surface of genus
$$
k
$$
has
$$
\chi=2-k.
$$
Thus
$$
2-k=-1,
$$
so
$$
k=3.
$$

:::

:::

::: {.pf-step #s1-7}

In the second diagram the six vertices form exactly two quotient
vertices:
$$
\boxed{
\{v_0,v_2,v_4\},
\qquad
\{v_1,v_3,v_5\}.}
$$


::: pf-proof

Read the endpoint identifications from the arrows in
$$
w_2=abca^{-1}cb.
$$
The two $a$-edges have opposite boundary signs, while the two $b$-edges and
the two $c$-edges have the same signs.
The generated equivalence relation groups the alternating polygon vertices
as displayed.

:::

:::

::: {.pf-step #s1-8}

Orient the quotient edges so that
$$
a,c:P\to Q,
\qquad
b:Q\to P,
$$
where
$$
P=\{v_0,v_2,v_4\},
\qquad
Q=\{v_1,v_3,v_5\}.
$$
Then the cellular boundary maps for $X_2$ satisfy
$$
\partial_1(x,y,z)
=
(x-y+z)(Q-P)
$$
and
$$
\boxed{
\partial_2(1)=(0,2,2)}.
$$


::: pf-proof

The formula for
$$
\partial_1
$$
comes from the initial and terminal vertices of the three oriented edges.

The exponent sums in
$$
w_2=abca^{-1}cb
$$
are
$$
0
$$
for
$$
a,
$$
$$
2
$$
for
$$
b,
$$
and
$$
2
$$
for
$$
c.
$$
These give
$$
\partial_2(1)=(0,2,2).
$$
The identity
$$
\partial_1\partial_2=0
$$
is visible as
$$
0-2+2=0.
$$

:::

:::

::: {.pf-step #s1-9}

The homology of $X_2$ is
$$
\boxed{
H_0(X_2;\ZZ)\cong\ZZ,
\quad
H_1(X_2;\ZZ)
\cong
\ZZ\oplus\ZZ/2,
\quad
H_k(X_2;\ZZ)=0
\text{ for }k\ge2.}
$$


::: pf-proof

The map
$$
\partial_1
$$
has rank
$$
1,
$$
so
$$
\ker\partial_1
$$
has rank
$$
2.
$$
A convenient basis is
$$
u=(1,1,0),
\qquad
v=(0,1,1).
$$
In this basis,
$$
\partial_2(1)=2v.
$$
Therefore
$$
H_1(X_2)
=
\langle u,v\rangle/
\langle2v\rangle
\cong
\ZZ\oplus\ZZ/2.
$$
The vector
$$
(0,2,2)
$$
is nonzero, so
$$
\partial_2
$$
is injective and
$$
H_2(X_2)=0.
$$
The quotient is connected, giving
$$
H_0(X_2)\cong\ZZ.
$$

:::

:::

::: {.pf-step #s1-10}

Collapsing the edge $a$ in the $1$-skeleton gives
$$
\boxed{
\pi_1(X_2)
\cong
\left\langle
b,c
\mid
bc^2b
\right\rangle
\cong
\left\langle
u,v
\mid
u^2v^2
\right\rangle.}
$$


::: pf-proof

The edge
$$
a
$$
joins the two vertices and is a maximal tree in the $1$-skeleton.
Collapsing a maximal tree is a homotopy equivalence and sends
$$
a
$$
to the constant path.

The attaching word
$$
abca^{-1}cb
$$
therefore becomes
$$
bc^2b.
$$
Van Kampen gives the first presentation.
The relator is cyclically conjugate to
$$
c^2b^2,
$$
which gives the standard nonorientable-genus-$2$ presentation after
renaming generators.

:::

:::

::: {.pf-step #s1-11}

The space $X_2$ is a closed $2$-manifold; in fact it is the Klein
bottle.


::: pf-proof

Again every boundary edge is paired exactly twice, so the quotient has
surface neighborhoods along edges and at the two quotient vertices.

Its Euler characteristic is
$$
\chi(X_2)
=
2-3+1
=
0.
$$
The two occurrences of
$$
b
$$
have the same boundary orientation, so the surface is nonorientable.
The unique closed connected nonorientable surface with Euler characteristic
$$
0
$$
has genus
$$
2,
$$
namely the Klein bottle.

:::

:::

::: {.pf-step #s1-12}

In the third diagram the six vertices again form two quotient
vertices
$$
P=\{v_0,v_2,v_4\},
\qquad
Q=\{v_1,v_3,v_5\},
$$
and there are two quotient edges
$$
a:P\to Q,
\qquad
b:Q\to P.
$$


::: pf-proof

All three $a$-edges are identified respecting their arrows, so all their
arrow-start vertices are identified and all their arrow-end vertices are
identified.
The same is true for the three $b$-edges.
Reading the arrows in the recovered diagram gives exactly the two alternating
vertex classes displayed.

:::

:::

::: {.pf-step #s1-13}

The cellular chain complex for $X_3$ has
$$
C_2\cong\ZZ,
\qquad
C_1\cong\ZZ^2,
\qquad
C_0\cong\ZZ^2,
$$
with
$$
\partial_1(x,y)
=
(x-y)(Q-P)
$$
and
$$
\boxed{
\partial_2(1)=(1,1)}.
$$


::: pf-proof

The $a$-edge goes from
$$
P
$$
to
$$
Q,
$$
while the $b$-edge goes from
$$
Q
$$
to
$$
P,
$$
giving the formula for
$$
\partial_1.
$$

In
$$
w_3=ababb^{-1}a^{-1},
$$
the exponent sum of
$$
a
$$
is
$$
1+1-1=1,
$$
and the exponent sum of
$$
b
$$
is likewise
$$
1+1-1=1.
$$
Thus
$$
\partial_2(1)=(1,1).
$$

:::

:::

::: {.pf-step #s1-14}

The homology of $X_3$ is
$$
\boxed{
H_0(X_3;\ZZ)\cong\ZZ,
\qquad
H_k(X_3;\ZZ)=0
\text{ for every }k\ge1.}
$$


::: pf-proof

One has
$$
\ker\partial_1
=
\langle(1,1)\rangle
=
\operatorname{im}\partial_2,
$$
so
$$
H_1(X_3)=0.
$$
The map
$$
\partial_2
$$
is injective, so
$$
H_2(X_3)=0.
$$
The $1$-skeleton is connected, so
$$
H_0(X_3)\cong\ZZ.
$$

:::

:::

::: {.pf-step #s1-15}

The fundamental group of $X_3$ is trivial.


::: pf-proof

Collapse the edge
$$
a
$$
in the $1$-skeleton; it is a maximal tree.
The remaining edge
$$
b
$$
is a loop.
Under this collapse the attaching word
$$
ababb^{-1}a^{-1}
$$
reduces to
$$
b.
$$
Thus
$$
\pi_1(X_3)
\cong
\langle b\mid b\rangle
=
1.
$$

:::

:::

::: {.pf-step #s1-16}

The space $X_3$ is not a $2$-manifold.


::: pf-proof

Take a point in the interior of the quotient edge
$$
a.
$$
Three distinct boundary edges of the original disk are identified to this
single edge.
Consequently a small neighborhood of the point is obtained by gluing
three half-disks along their boundary diameters.

The link of the point is therefore a theta-type graph with three arcs between
the two normal directions, not a circle.
An interior point of a topological $2$-manifold must have link
$$
S^1.
$$
Hence
$$
X_3
$$
is not locally Euclidean there.

:::

:::

::: {.pf-step #s1-17}

Therefore the complete answers are
$$
\boxed{
\begin{array}{c|c|c|c}
&\pi_1&H_1&\text{manifold?}\\
\hline
X_1&
\langle a,b,c\mid abacb^{-1}c^{-1}\rangle&
\ZZ^2\oplus\ZZ/2&
\text{yes, }\#^3\RP^2
\\
X_2&
\langle u,v\mid u^2v^2\rangle&
\ZZ\oplus\ZZ/2&
\text{yes, Klein bottle}
\\
X_3&
1&
0&
\text{no}
\end{array}}
$$
with
$$
H_0(X_i)\cong\ZZ
$$
for all three spaces and all other positive-dimensional homology groups
zero except the displayed
$$
H_1
$$
groups.


::: pf-proof

This summarizes steps [](#s1-3){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-17){.pf-ref} answers all three requested questions for all three quotient
spaces.

:::

:::

:::
