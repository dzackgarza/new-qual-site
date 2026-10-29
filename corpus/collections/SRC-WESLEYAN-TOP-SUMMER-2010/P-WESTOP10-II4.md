---
schema: qual/card@1
id: P-WESTOP10-II4
kind: problem
title: Four questions about three disk-identification spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The Markdown extraction loses the diagram, but direct inspection of page 10 of assets/attachments/topology_2006-2014.pdf recovers all labels and arrows. Clockwise from the top edge, the three boundary words are ababb^{-1}a^{-1}, abca^{-1}cb, and abcab^{-1}c^{-1}; in the first diagram each label occurs three times and all equally labeled edges are identified.
---

::: {.problem}
Consider three hexagonal disks with boundary edges identified according to the arrows in the source diagram.

For the first diagram, the three edges labeled $a$ are all identified respecting their arrows, and likewise the three edges labeled $b$; its clockwise boundary word is
\[
w_1=ababb^{-1}a^{-1}.
\]

For the second and third diagrams the paired-edge words, read clockwise from the top edge, are
\[
w_2=abca^{-1}cb,
\qquad
w_3=abcab^{-1}c^{-1}.
\]

For each source space:

1. compute the fundamental group;
2. compute the homology groups;
3. determine whether it is a manifold;
4. if it is a compact connected surface, identify it in the classification as $S^2$, a connected sum of tori, or a connected sum of real projective planes.
:::

::: {.solution}

Write the quotient spaces as
$$
X_1,qquad X_2,qquad X_3
$$
in the order shown in the source.

::: pf

::: {.pf-step #s1-1}

In $X_1$, the six boundary vertices collapse to two quotient vertices
$$
P=\{v_0,v_2,v_4\},
\qquad
Q=\{v_1,v_3,v_5\},
$$
and the quotient $1$-skeleton has two oriented edges
$$
a:P\to Q,
\qquad
b:Q\to P.
$$


::: pf-proof

All three $a$-edges are identified respecting their arrows, so all their
arrow-starts are identified and all their arrow-ends are identified.
The three $b$-edges give the same two alternating classes.

:::

:::

::: pf-step

The cellular chain complex of $X_1$ is
$$
0\to\ZZ
\xrightarrow{\partial_2}
\ZZ^2
\xrightarrow{\partial_1}
\ZZ^2
\to0,
$$
where
$$
\partial_1(x,y)=(x-y)(Q-P)
$$
and
$$
\boxed{\partial_2(1)=(1,1)}.
$$


::: pf-proof

The formula for
$$
\partial_1
$$
comes from the edge orientations in step [](#s1-1){.pf-ref}.

The attaching word is
$$
w_1=ababb^{-1}a^{-1}.
$$
Its exponent sums in
$$
a,b
$$
are both
$$
1,
$$
so the cellular boundary of the $2$-cell is
$$
(1,1).
$$

:::

:::

::: {.pf-step #s1-3}

The homology of $X_1$ is
$$
\boxed{
H_0(X_1;\ZZ)\cong\ZZ,
\qquad
H_k(X_1;\ZZ)=0\quad(k\ge1).}
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
H_1(X_1)=0.
$$
The map
$$
\partial_2
$$
is injective, hence
$$
H_2(X_1)=0.
$$
The $1$-skeleton is connected, giving
$$
H_0(X_1)\cong\ZZ.
$$
There are no higher-dimensional cells.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{\pi_1(X_1)=1}.
$$


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
is a single loop.
Under this collapse
$$
ababb^{-1}a^{-1}
$$
reduces to
$$
b.
$$
Thus van Kampen gives
$$
\pi_1(X_1)
\cong
\langle b\mid b\rangle
=1.
$$

:::

:::

::: {.pf-step #s1-5}

The space $X_1$ is not a manifold.


::: pf-proof

At an interior point of the quotient edge
$$
a,
$$
three distinct boundary edges of the original disk have been glued together.
A small neighborhood is therefore three half-disks glued along their boundary
diameters.
Its link is not a circle.
Hence the point has no neighborhood homeomorphic to
$$
\RR^2.
$$

:::

:::

::: {.pf-step #s1-6}

In $X_2$, the quotient has two vertices
$$
P=\{v_0,v_2,v_4\},
\qquad
Q=\{v_1,v_3,v_5\},
$$
and, with the source orientations,
$$
a,c:P\to Q,
\qquad
b:Q\to P.
$$


::: pf-proof

Read the endpoint identifications from
$$
w_2=abca^{-1}cb.
$$
The two $a$-occurrences have opposite boundary signs, whereas the two
$b$-occurrences and the two $c$-occurrences have the same signs.
The resulting equivalence classes are the alternating vertex sets displayed.

:::

:::

::: {.pf-step #s1-7}

The cellular boundary maps for $X_2$ satisfy
$$
\partial_1(x,y,z)
=(x-y+z)(Q-P)
$$
and
$$
\boxed{\partial_2(1)=(0,2,2)}
$$
in the edge basis
$$
(a,b,c).
$$


::: pf-proof

The first formula follows from step [](#s1-6){.pf-ref}.
The exponent sums of
$$
a,b,c
$$
in
$$
abca^{-1}cb
$$
are
$$
0,2,2,
$$
respectively.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
H_0(X_2;\ZZ)\cong\ZZ,
\quad
H_1(X_2;\ZZ)\cong\ZZ\oplus\ZZ/2,
\quad
H_k(X_2;\ZZ)=0\ (k\ge2).}
$$


::: pf-proof

A basis of
$$
\ker\partial_1
$$
is
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
\cong
\langle u,v\rangle/\langle2v\rangle
\cong
\ZZ\oplus\ZZ/2.
$$
The map
$$
\partial_2
$$
is injective, so
$$
H_2(X_2)=0.
$$
Connectedness gives the stated
$$
H_0.
$$

:::

:::

::: {.pf-step #s1-9}

The fundamental group of $X_2$ is
$$
\boxed{
\pi_1(X_2)
\cong
\langle u,v\mid u^2v^2\rangle.}
$$


::: pf-proof

Collapse the tree edge
$$
a.
$$
The attaching word becomes
$$
bc^2b,
$$
which is cyclically conjugate to
$$
c^2b^2.
$$
Van Kampen gives
$$
\langle b,c\mid c^2b^2\rangle,
$$
and renaming the generators gives the displayed presentation.

:::

:::

::: {.pf-step #s1-10}

The space $X_2$ is the Klein bottle.


::: pf-proof

Every boundary edge is paired with exactly one other edge.
The quotient edge neighborhoods are disks, and each quotient vertex has
circular link, so
$$
X_2
$$
is a closed connected surface.

Its Euler characteristic is
$$
\chi(X_2)=2-3+1=0.
$$
The two occurrences of
$$
b
$$
have the same boundary orientation, so the surface is nonorientable.
The closed nonorientable surface of Euler characteristic
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

::: {.pf-step #s1-11}

In $X_3$, all six boundary vertices are identified to one point.


::: pf-proof

The boundary word is
$$
w_3=abcab^{-1}c^{-1}.
$$
Aligning the arrows of the paired $a$-, $b$-, and $c$-edges and taking the
transitive closure of the endpoint identifications joins all six vertices.

:::

:::

::: {.pf-step #s1-12}

Thus $X_3$ has one $0$-cell, three $1$-cells
$$
a,b,c,
$$
and one $2$-cell attached by
$$
abcab^{-1}c^{-1}.
$$


::: pf-proof

Step [](#s1-11){.pf-ref} gives the single quotient vertex.
Each edge label gives one quotient $1$-cell, and the polygon interior gives
the unique $2$-cell.

:::

:::

::: {.pf-step #s1-13}

One has
$$
\boxed{
\pi_1(X_3)
\cong
\langle a,b,c\mid abcab^{-1}c^{-1}\rangle.}
$$


::: pf-proof

The $1$-skeleton is a wedge of three circles.
Van Kampen imposes the single relation given by the $2$-cell attaching map.

:::

:::

::: {.pf-step #s1-14}

The cellular boundary of the $2$-cell is
$$
\boxed{\partial_2(1)=(2,0,0)}
$$
in the basis
$$
(a,b,c),
$$
and
$$
\partial_1=0.
$$


::: pf-proof

There is only one $0$-cell, hence
$$
\partial_1=0.
$$
The exponent sums of
$$
a,b,c
$$
in
$$
abcab^{-1}c^{-1}
$$
are
$$
2,0,0.
$$

:::

:::

::: {.pf-step #s1-15}

Therefore
$$
\boxed{
H_0(X_3;\ZZ)\cong\ZZ,
\quad
H_1(X_3;\ZZ)\cong\ZZ^2\oplus\ZZ/2,
\quad
H_k(X_3;\ZZ)=0\ (k\ge2).}
$$


::: pf-proof

The map
$$
\partial_2:\ZZ\to\ZZ^3
$$
is injective, so
$$
H_2(X_3)=0.
$$
Also
$$
H_1(X_3)
=
\ZZ^3/\langle(2,0,0)\rangle
\cong
\ZZ^2\oplus\ZZ/2.
$$
Connectedness gives the stated
$$
H_0.
$$

:::

:::

::: {.pf-step #s1-16}

The space $X_3$ is the connected sum of three projective planes:
$$
\boxed{
X_3
\cong
\mathbb{RP}^2
\#\mathbb{RP}^2
\#\mathbb{RP}^2.}
$$


::: pf-proof

All boundary edges are paired exactly twice, so the quotient is a closed
surface.
Its Euler characteristic is
$$
\chi(X_3)=1-3+1=-1.
$$
The two $a$-edges occur with the same boundary orientation, so the surface is
nonorientable.
If its nonorientable genus is
$$
k,
$$
then
$$
2-k=-1,
$$
hence
$$
k=3.
$$

:::

:::

::: {.pf-step #s1-17}

Summarizing,
$$
\boxed{
\begin{array}{c|c|c|c}
&\pi_1&H_1&\text{type}\\
\hline
X_1&1&0&\text{not a manifold}\\
X_2&\langle u,v\mid u^2v^2\rangle&
\ZZ\oplus\ZZ/2&\text{Klein bottle}\\
X_3&\langle a,b,c\mid abcab^{-1}c^{-1}\rangle&
\ZZ^2\oplus\ZZ/2&\#^3\mathbb{RP}^2
\end{array}}
$$
with
$$
H_0(X_i)\cong\ZZ
$$
for all three and all unlisted positive-dimensional homology groups equal to
zero.


::: pf-proof

This is exactly the content of steps [](#s1-3){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-17){.pf-ref} answers parts (a)--(d).

:::

:::

:::
