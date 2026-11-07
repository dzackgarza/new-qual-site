---
schema: qual/card@1
id: E-HAT-1.2-14
kind: problem
title: Cube with face identifications via screw motions has quaternion group as fundamental group
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - CW Complexes
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Tracked the vertex, edge, and face orbits under the quarter-turn identifications and reduced the resulting presentation to the eight-element quaternion presentation.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Review the cell count for the cube quotient and the eight-element bound; the closing step now says how the eight words multiply, instead of pointing at earlier steps.
---

::: {.problem}
Consider the quotient space of a cube $I^3$ obtained by identifying each square face with the opposite square face via the right-handed screw motion consisting of a translation by one unit in the direction perpendicular to the face combined with a one-quarter twist of the face about its center point.
Show this quotient space $X$ is a cell complex with two 0 cells, four 1 cells, three 2 cells, and one 3 cell.
Using this structure, show that $\pi_1(X)$ is the quaternion group $\{\pm 1, \pm i, \pm j, \pm k\}$, of order eight.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The eight vertices of the cube fall into two equivalence classes under the three screw identifications.

::: pf-proof

Write the vertices as triples $(x,y,z)\in\{0,1\}^3$ and take the three face pairings to be the quarter-turn screw motions
$$
(0,y,z)\sim(1,1-z,y),\qquad
(x,0,z)\sim(z,1,1-x),\qquad
(x,y,0)\sim(1-y,x,1),
$$
which carry a one-unit translation perpendicular to the face together with the same quarter turn in the three coordinate directions.

Each pairing carries even vertices to even vertices and odd to odd, and the three identifications
$$
000\sim110,\qquad 000\sim011,\qquad 000\sim101
$$
join the four even vertices, while
$$
001\sim100,\qquad 001\sim111,\qquad 001\sim010
$$
join the four odd ones. The remaining partner pairs -- $010\sim111$ and $011\sim101$ for the first pairing, $100\sim010$ and $101\sim110$ for the second, $100\sim111$ and $110\sim011$ for the third -- stay inside these two sets. Hence the quotient has exactly two $0$-cells,
$$
v_0=\{000,011,101,110\},\qquad v_1=\{001,010,100,111\}.
$$

:::

:::

::: {.pf-step #s2}

The twelve cube edges fall into four edge orbits, and the six faces fall into three face orbits.
Thus the quotient has four $1$-cells and three $2$-cells; the cube interior gives one $3$-cell.

::: pf-proof

Orient every cube edge from $v_0$ to $v_1$; this is consistent because no pairing exchanges the two classes, by step [](#s1){.pf-ref}. The twelve edges then fall into the four classes
$$
\begin{aligned}
a&=\{000\to001,\ 011\to111,\ 110\to100\},&
b&=\{000\to010,\ 101\to001,\ 110\to111\},\\
c&=\{011\to001,\ 110\to010,\ 101\to100\},&
d&=\{000\to100,\ 011\to010,\ 101\to111\}.
\end{aligned}
$$
The pairings send a representative of each class to the other two edges listed with it:
$$
\begin{aligned}
000\to001&\ \mapsto\ 110\to100\ (x=0\sim x=1),
&\quad 000\to001&\ \mapsto\ 011\to111\ (y=0\sim y=1),\\
000\to010&\ \mapsto\ 110\to111\ (x=0\sim x=1),
&\quad 000\to010&\ \mapsto\ 101\to001\ (z=0\sim z=1),\\
011\to001&\ \mapsto\ 101\to100\ (x=0\sim x=1),
&\quad 011\to001&\ \mapsto\ 110\to010\ (z=0\sim z=1),\\
000\to100&\ \mapsto\ 011\to010\ (y=0\sim y=1),
&\quad 000\to100&\ \mapsto\ 101\to111\ (z=0\sim z=1).
\end{aligned}
$$
An edge perpendicular to a pair of opposite faces is not moved to a further edge by that pairing, since the pairing then only moves the two endpoints. So the twelve edges form exactly these four orbits, giving four $1$-cells.

Each face is identified with its opposite face, so the six faces form three $2$-cells.
The open interior of the cube is not identified with any boundary point and therefore descends to a single open $3$-cell.
Together with step [](#s1){.pf-ref} this gives the claimed cell counts
$$
2,\ 4,\ 3,\ 1.
$$

:::

:::

::: {.pf-step #s3}

Label the four oriented $1$-cells $a,b,c,d$ from $v_0$ to $v_1$.
After collapsing the edge $a$ as a maximal tree, the $1$-skeleton has free fundamental group on
$$
i=ab^{-1},\qquad j=ac^{-1},\qquad k=ad^{-1}.
$$

::: pf-proof

The quotient $1$-skeleton is a connected graph with two vertices and four edges.
Collapsing any one edge joining the vertices is a homotopy equivalence from this graph to a wedge of
$$
4-2+1=3
$$
circles.
Taking $a$ as the tree edge gives the displayed three loops.

:::

:::

::: {.pf-step #s4}

The three quotient $2$-cells impose the relations
$$
i^{-1}jk=1,\qquad
i^{-1}k^{-1}j=1,\qquad
jk^{-1}i=1.
$$

::: pf-proof

Represent the three face orbits by the faces $x=0$, $y=0$, $z=0$. With the classes of step [](#s2){.pf-ref}, the four edges of each are
$$
x=0:\ a=[000,001],\ c=[001,011],\ d=[011,010],\ b=[010,000],
$$
$$
y=0:\ d=[000,100],\ c=[100,101],\ b=[101,001],\ a=[001,000],
$$
$$
z=0:\ d=[000,100],\ a=[100,110],\ c=[110,010],\ b=[010,000].
$$
Read each boundary in the direction
$$
000\to001\to011\to010,\qquad
000\to100\to101\to001,\qquad
000\to100\to110\to010
$$
respectively, and write a side as the inverse of its class whenever it is traversed against the even-to-odd orientation. The three oriented boundary words are
$$
a\,c^{-1}d\,b^{-1},\qquad d\,c^{-1}b\,a^{-1},\qquad d\,a^{-1}c\,b^{-1},
$$
which up to cyclic permutation and reversal are the three words claimed:
$$
b\,c^{-1}a\,d^{-1},\qquad b\,a^{-1}d\,c^{-1},\qquad a\,c^{-1}d\,b^{-1}.
$$
The loops $i=ab^{-1}$, $j=ac^{-1}$, $k=ad^{-1}$ give $b=i^{-1}a$, $c=j^{-1}a$, $d=k^{-1}a$, hence $b^{-1}=a^{-1}i$, $c^{-1}=a^{-1}j$, $d^{-1}=a^{-1}k$. Substituting into the three words in order,
$$
(i^{-1}a)(a^{-1}j)(a)(a^{-1}k)=i^{-1}jk,\qquad
(i^{-1}a)(a^{-1})(k^{-1}a)(a^{-1}j)=i^{-1}k^{-1}j,\qquad
(a)(a^{-1}j)(k^{-1}a)(a^{-1}i)=jk^{-1}i.
$$
Attaching a $2$-cell sets each of these loops equal to the identity.

:::

:::

::: {.pf-step #s5}

Hence
$$
\pi_1(X)
\cong
\langle i,j,k\mid i=jk,\ j=ki,\ k=ij\rangle.
$$

::: pf-proof

The first relation in step [](#s4){.pf-ref} is equivalent to $i=jk$.
The second is equivalent to $j=ki$.
For the third,
$$
jk^{-1}i=1
\iff
k j^{-1}=i
\iff
k=ij.
$$
The single $3$-cell does not alter the fundamental group: Proposition 1.26(b) (p. 50) applied with $X=X^2$ and $n=3$.

:::

:::

::: {.pf-step #s6}

In this group,
$$
i^2=j^2=k^2=:z,
\qquad
z=ijk.
$$

::: pf-proof

From $i=jk$, multiplying on the left by $i$ gives
$$
i^2=ijk.
$$
From $k=ij$, multiplying on the right by $k$ gives
$$
k^2=ijk.
$$
Finally, $j=ki$ and $i=jk$ give
$$
j=k(jk)=kjk.
$$
Multiplying on the left by $j$ yields
$$
j^2=jkjk=(jk)^2=i^2.
$$
Thus all three squares equal the common element $z=ijk$.

:::

:::

::: {.pf-step #s7}

The element $z$ is central and satisfies $z^2=1$.

::: pf-proof

Since
$$
z=i^2=j^2,
$$
it commutes with both generators $i$ and $j$, hence with the whole group because $k=ij$.

Also $i=jij$ follows from $i=jk$ and $k=ij$.
Squaring this equality and using centrality of $z$ gives
$$
z=i^2=(jij)^2
=jij^2ij
=jizij
=z\,ji^2j
=z^3.
$$
Cancelling $z$ yields
$$
z^2=1.
$$

:::

:::

::: {.pf-step #s8}

Every element has one of the eight forms
$$
1,\ z,\ i,\ zi,\ j,\ zj,\ ij,\ zij.
$$

::: pf-proof

From steps [](#s6){.pf-ref} and [](#s7){.pf-ref},
$$
i^2=j^2=z,\qquad z^2=1,
$$
and $z$ is central.
Moreover $k=ij$ and
$$
ji=z\,ij.
$$
Indeed $i=jij$ implies $ji=ij^{-1}$, while $j^{-1}=zj$ because $j^2=z=z^{-1}$.
Thus any word can first eliminate $k$, then move all $j$'s to the right of all $i$'s, collecting powers of the central element $z$, and finally reduce the exponents of $i,j,z$ modulo $2$.
This gives at most the eight displayed normal forms.

:::

:::

::: {.pf-step #s9}

These eight elements are distinct and form the quaternion group $Q_8$.

::: pf-proof

Map the presented group to
$$
Q_8=\{\pm1,\pm\mathbf i,\pm\mathbf j,\pm\mathbf k\}
$$
by
$$
i\longmapsto\mathbf i,\qquad
j\longmapsto\mathbf j,\qquad
k\longmapsto\mathbf k.
$$
The quaternion multiplication rules give
$$
\mathbf i=\mathbf j\mathbf k,\qquad
\mathbf j=\mathbf k\mathbf i,\qquad
\mathbf k=\mathbf i\mathbf j,
$$
so this is a surjective homomorphism.
Hence the presented group has at least eight elements.
By step [](#s8){.pf-ref} it has at most eight elements.
Therefore it has exactly eight elements and the surjection is an isomorphism.

:::

:::

::: pf-step

Consequently
$$
\boxed{\pi_1(X)\cong Q_8.}
$$

::: pf-proof

Step [](#s5){.pf-ref} presents $\pi_1(X)$ on three generators with three relations; step [](#s8){.pf-ref} writes every element of that group as one of eight words, and step [](#s9){.pf-ref} shows those eight words are distinct and multiply by the quaternion rules. Hence the presented group has exactly eight elements and is $Q_8$.

:::

:::

:::

:::
