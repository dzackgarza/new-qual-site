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
---

Consider the quotient space of a cube $I^3$ obtained by identifying each square face with the opposite square face via the right-handed screw motion consisting of a translation by one unit in the direction perpendicular to the face combined with a one-quarter twist of the face about its center point.
Show this quotient space $X$ is a cell complex with two 0 cells, four 1 cells, three 2 cells, and one 3 cell.
Using this structure, show that $\pi_1(X)$ is the quaternion group $\{\pm 1, \pm i, \pm j, \pm k\}$, of order eight.

::: {.solution}
<1>1. The eight vertices of the cube fall into two equivalence classes under the three screw identifications.
::: {.proof}
Each face pairing is a quarter-turn followed by translation to the opposite face.
Starting from one vertex and applying the three pairings reaches exactly the four vertices of one parity class; starting from an adjacent vertex reaches the other four.
No face pairing changes between these two classes.
Hence the quotient has exactly two $0$-cells, say $v_0,v_1$.
:::

<1>2. The twelve cube edges fall into four edge orbits, and the six faces fall into three face orbits.
Thus the quotient has four $1$-cells and three $2$-cells; the cube interior gives one $3$-cell.
::: {.proof}
Under a quarter-turn face pairing, an edge is carried to an edge on the opposite face.
Following the induced identifications partitions the twelve edges into four orbits of three edges each.
Similarly, each face is identified with its opposite face, giving three face orbits.
The open interior of the cube is not identified with any boundary point and therefore descends to a single open $3$-cell.
Together with <1>1 this gives the claimed cell counts
\[
2,\ 4,\ 3,\ 1.
\]
:::

<1>3. Label the four oriented $1$-cells $a,b,c,d$ from $v_0$ to $v_1$.
After collapsing the edge $a$ as a maximal tree, the $1$-skeleton has free fundamental group on
\[
i=ab^{-1},\qquad j=ac^{-1},\qquad k=ad^{-1}.
\]
::: {.proof}
The quotient $1$-skeleton is a connected graph with two vertices and four edges.
Collapsing any one edge joining the vertices is a homotopy equivalence from this graph to a wedge of
\[
4-2+1=3
\]
circles.
Taking $a$ as the tree edge gives the displayed three loops.
:::

<1>4. The three quotient $2$-cells impose the relations
\[
i^{-1}jk=1,\qquad
i^{-1}k^{-1}j=1,\qquad
jk^{-1}i=1.
\]
::: {.proof}
Trace the oriented boundary of one representative of each pair of opposite faces before collapsing the tree edge $a$.
With the edge orientations from <1>3, the three face words are
\[
bc^{-1}ad^{-1},\qquad
ba^{-1}dc^{-1},\qquad
ac^{-1}db^{-1}.
\]
Substituting the loops
\[
i=ab^{-1},\quad j=ac^{-1},\quad k=ad^{-1}
\]
after collapsing $a$ gives respectively
\[
i^{-1}jk,\qquad i^{-1}k^{-1}j,\qquad jk^{-1}i.
\]
Attaching a $2$-cell sets each of these loops equal to the identity.
:::

<1>5. Hence
\[
\pi_1(X)
\cong
\langle i,j,k\mid i=jk,\ j=ki,\ k=ij\rangle.
\]
::: {.proof}
The first relation in <1>4 is equivalent to $i=jk$.
The second is equivalent to $j=ki$.
For the third,
\[
jk^{-1}i=1
\iff
k j^{-1}=i
\iff
k=ij.
\]
The $3$-cell does not alter the fundamental group.
:::

<1>6. In this group,
\[
i^2=j^2=k^2=:z,
\qquad
z=ijk.
\]
::: {.proof}
From $i=jk$, multiplying on the left by $i$ gives
\[
i^2=ijk.
\]
From $k=ij$, multiplying on the right by $k$ gives
\[
k^2=ijk.
\]
Finally, $j=ki$ and $i=jk$ give
\[
j=k(jk)=kjk.
\]
Multiplying on the left by $j$ yields
\[
j^2=jkjk=(jk)^2=i^2.
\]
Thus all three squares equal the common element $z=ijk$.
:::

<1>7. The element $z$ is central and satisfies $z^2=1$.
::: {.proof}
Since
\[
z=i^2=j^2,
\]
it commutes with both generators $i$ and $j$, hence with the whole group because $k=ij$.

Also $i=jij$ follows from $i=jk$ and $k=ij$.
Squaring this equality and using centrality of $z$ gives
\[
z=i^2=(jij)^2
=jij^2ij
=jizij
=z\,ji^2j
=z^3.
\]
Cancelling $z$ yields
\[
z^2=1.
\]
:::

<1>8. Every element has one of the eight forms
\[
1,\ z,\ i,\ zi,\ j,\ zj,\ ij,\ zij.
\]
::: {.proof}
From <1>6--<1>7,
\[
i^2=j^2=z,\qquad z^2=1,
\]
and $z$ is central.
Moreover $k=ij$ and
\[
ji=z\,ij.
\]
Indeed $i=jij$ implies $ji=ij^{-1}$, while $j^{-1}=zj$ because $j^2=z=z^{-1}$.
Thus any word can first eliminate $k$, then move all $j$'s to the right of all $i$'s, collecting powers of the central element $z$, and finally reduce the exponents of $i,j,z$ modulo $2$.
This gives at most the eight displayed normal forms.
:::

<1>9. These eight elements are distinct and form the quaternion group $Q_8$.
::: {.proof}
Map the presented group to
\[
Q_8=\{\pm1,\pm\mathbf i,\pm\mathbf j,\pm\mathbf k\}
\]
by
\[
i\longmapsto\mathbf i,\qquad
j\longmapsto\mathbf j,\qquad
k\longmapsto\mathbf k.
\]
The quaternion multiplication rules give
\[
\mathbf i=\mathbf j\mathbf k,\qquad
\mathbf j=\mathbf k\mathbf i,\qquad
\mathbf k=\mathbf i\mathbf j,
\]
so this is a surjective homomorphism.
Hence the presented group has at least eight elements.
By <1>8 it has at most eight elements.
Therefore it has exactly eight elements and the surjection is an isomorphism.
:::

<1>10. Consequently
\[
\boxed{\pi_1(X)\cong Q_8.}
\]
::: {.proof}
Combine <1>5 and <1>9.
:::
:::
