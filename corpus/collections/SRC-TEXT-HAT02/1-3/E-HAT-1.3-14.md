---
schema: qual/card@1
id: E-HAT-1.3-14
kind: problem
title: "Connected covering spaces of $\\mathbb{RP}^2 \\vee \\mathbb{RP}^2$"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Classified all subgroups of the infinite dihedral group up to conjugacy and translated their Schreier graphs into the corresponding covers built from lifted RP2 and S2 pieces.
---

Find all the connected covering spaces of $\mathbb{RP}^2 \vee \mathbb{RP}^2$.

::: {.solution}
Write
\[
X=\mathbb{RP}^2\vee\mathbb{RP}^2
\]
and let $a,b$ be the two order-two generators coming from the two summands.
Then
\[
\pi_1(X)=\langle a,b\mid a^2=b^2=1\rangle
\cong C_2*C_2=:D_\infty.
\]
Put
\[
r=ab.
\]

<1>1. Every subgroup of $D_\infty$ is one of the following types:
\[
1,
\qquad
\langle r^n\rangle\ (n\ge1),
\qquad
\langle r^k a\rangle,
\qquad
\langle r^n,r^k a\rangle\ (n\ge1).
\]
::: {.proof}
The infinite cyclic subgroup
\[
\langle r\rangle\cong\mathbb Z
\]
has index two in $D_\infty$, and every element outside it is a reflection $r^k a$ of order two.

Let $H\le D_\infty$.
If $H\subseteq\langle r\rangle$, then $H=1$ or $H=\langle r^n\rangle$ for a unique $n\ge1$.
Otherwise choose a reflection $r^k a\in H$.
The intersection
\[
H\cap\langle r\rangle
\]
is either trivial or $\langle r^n\rangle$.
In the first case $H=\langle r^k a\rangle$; in the second every element of $H$ is in either $\langle r^n\rangle$ or its coset by $r^k a$, so
\[
H=\langle r^n,r^k a\rangle.
\]
:::

<1>2. Up to conjugacy, the reflection subgroups give exactly two infinite-sheeted covers:
\[
\langle a\rangle
\qquad\text{and}\qquad
\langle b\rangle.
\]
::: {.proof}
Conjugation by $r^m$ changes
\[
r^k a\longmapsto r^{k+2m}a,
\]
while conjugation by a reflection changes $k$ to its negative modulo an even shift.
Thus parity of $k$ is the only conjugacy invariant.
Even $k$ gives the class of $a$, and odd $k$ the class of $b$.
:::

<1>3. For the finite-index dihedral subgroups
\[
H_{n,k}=\langle r^n,r^k a\rangle,
\]
the index is $n$.
For odd $n$ there is one conjugacy class; for even $n$ there are two, represented by
\[
H_{n,0}
\qquad\text{and}\qquad
H_{n,1}.
\]
::: {.proof}
The cosets are represented by
\[
1,r,\dots,r^{n-1},
\]
so the index is $n$.
Conjugation changes $k$ by an even integer and by sign, modulo $n$.
If $n$ is odd, adding even integers modulo $n$ reaches every residue class, so all $k$ are conjugate.
If $n$ is even, parity is preserved and gives exactly two classes.
:::

<1>4. The cyclic subgroup $\langle r^n\rangle$ has index $2n$ and gives one normal $2n$-sheeted cover for every $n\ge1$.
::: {.proof}
The quotient
\[
D_\infty/\langle r^n\rangle
\]
has representatives
\[
1,r,\dots,r^{n-1},a,ra,\dots,r^{n-1}a,
\]
so it has $2n$ elements.
The subgroup is normal because conjugation sends $r^n$ to $r^{\pm n}$.
:::

<1>5. These subgroup types have a direct geometric description.
For each lift of the wedge point, an $a$-orbit of two vertices is joined by a lifted copy of $S^2\to\mathbb{RP}^2$ from the first summand, while an $a$-fixed vertex carries a copy of $\mathbb{RP}^2$ itself; similarly for $b$ and the second summand.
::: {.proof}
Use the standard CW structure
\[
\mathbb{RP}^2=e^0\cup e^1\cup e^2,
\]
where the $2$-cell is attached by the degree-two word $a^2$ (or $b^2$).
In a covering, if the monodromy involution $a$ exchanges two sheets, the two lifted $a$-edges and their lifted $2$-cells form the standard double cover
\[
S^2\to\mathbb{RP}^2
\]
between those two lifted wedge points.
If $a$ fixes a sheet, the corresponding summand lifts homeomorphically as $\mathbb{RP}^2$ attached at that vertex.
The same statement holds for $b$.
:::

<1>6. The trivial subgroup gives the universal cover: a bi-infinite line of lifted wedge points with alternating $a$- and $b$-copies of $S^2$ between consecutive points.
::: {.proof}
The Schreier graph of the free action of $D_\infty$ on itself has vertices indexed by the group elements and alternating $a$- and $b$-adjacencies.
It is a bi-infinite line.
No generator fixes a vertex, so <1>5 replaces every adjacency by an $S^2$ piece.
The incidence graph is a tree, hence the resulting tree of simply connected spheres is simply connected.
:::

<1>7. The two reflection subgroups $\langle a\rangle$ and $\langle b\rangle$ give two infinite-sheeted ray covers.
::: {.proof}
For $\langle a\rangle$, the Schreier graph is a ray whose endpoint is fixed by $a$; therefore the endpoint carries an $a$-type $\mathbb{RP}^2$, followed by an infinite alternating chain of $S^2$ pieces.
For $\langle b\rangle$, the same construction has a $b$-type $\mathbb{RP}^2$ at the endpoint.
The two covers are not isomorphic over $X$ because the two endpoint projective planes map to different wedge summands.
:::

<1>8. The subgroup $\langle r^n\rangle$ gives a cyclic necklace of $2n$ lifted wedge points with alternating $a$- and $b$-copies of $S^2$ between consecutive points.
::: {.proof}
Its Schreier graph is a $2n$-cycle with alternating $a,b$ adjacencies and no fixed vertices.
Apply <1>5.
:::

<1>9. For $n\ge2$, the subgroup $H_{n,k}$ gives a finite path of $n$ lifted wedge points, with $S^2$ pieces along the path and projective-plane pieces at the two ends.
If $n$ is odd, one endpoint is of $a$-type and the other of $b$-type.
If $n$ is even, both endpoints have the same type, giving the two nonisomorphic covers according as both are $a$-type or both are $b$-type.
::: {.proof}
The Schreier graph on the $n$ cosets of $H_{n,k}$ is a path.
Interior vertices are exchanged by both involutions, while each endpoint is fixed by the involution whose labelled edge is missing there.
Along a path the labels alternate.
If $n$ is even, the path has odd edge-length $n-1$, so its first and last edge labels are the same; consequently the same opposite involution fixes both endpoints.
If $n$ is odd, the path has even edge-length, so the first and last edge labels are different and the two fixed endpoint involutions are different.
Equivalently, a direct coset calculation gives one $a$- and one $b$-fixed endpoint for odd $n$, and two endpoints of the same type for even $n$.
The two same-type possibilities for even $n$ are precisely the two conjugacy classes in <1>3.
:::

<1>10. For $n=1$, $H_{1,0}=D_\infty$ and the corresponding one-sheeted cover is $X$ itself.
::: {.proof}
There is one lifted wedge point fixed by both $a$ and $b$, so both projective-plane summands occur at that point.
:::

<1>11. The list in <1>6--<1>10 contains every connected covering space of $\mathbb{RP}^2\vee\mathbb{RP}^2$, up to unbased covering isomorphism.
::: {.proof}
Connected unbased covering spaces correspond to conjugacy classes of subgroups of $\pi_1(X)$.
The subgroup classification is <1>1--<1>4, and <1>6--<1>10 translates each conjugacy class into its covering space.
:::
:::
