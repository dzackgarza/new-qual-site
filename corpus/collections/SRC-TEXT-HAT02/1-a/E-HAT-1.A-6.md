---
schema: qual/card@1
id: E-HAT-1.A-6
kind: problem
title: Free generators for commutator subgroup of free group via covering space
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the square-lattice cover for ker(F2 -> Z2), chose a spanning tree of all horizontal edges plus the vertical axis, and read the non-tree-edge loops as a free basis.
---

Let $F$ be the free group on two generators and let $F'$ be its commutator subgroup.
Find a set of free generators for $F'$ by considering the covering space of the graph $S^1 \lor S^1$ corresponding to $F'$.


::: {.solution}
Let
\[
F=\langle a,b\rangle
\]
be the free group on two generators.
Its commutator subgroup is the kernel of the abelianization map
\[
F\longrightarrow\mathbb Z^2,
\qquad
a\longmapsto(1,0),
\quad
b\longmapsto(0,1).
\]

<1>1. The covering graph corresponding to $F'$ is the square lattice with vertex set
\[
\mathbb Z^2,
\]
horizontal $a$-edges
\[
(m,n)\longrightarrow(m+1,n),
\]
and vertical $b$-edges
\[
(m,n)\longrightarrow(m,n+1).
\]
::: {.proof}
The cover corresponding to a normal subgroup $H\triangleleft F$ is the Cayley graph of the quotient $F/H$ with respect to the images of the free generators.
Here
\[
F/F'\cong\mathbb Z^2,
\]
so the Cayley graph is exactly the square lattice.
:::

<1>2. Let $T$ be the subgraph consisting of all horizontal edges together with all vertical edges on the line $m=0$.
Then $T$ is a spanning tree of the lattice graph.
::: {.proof}
Every vertex $(m,n)$ is joined to $(0,0)$ by first moving vertically along the line $m=0$ to $(0,n)$ and then horizontally to $(m,n)$, so $T$ is connected and spanning.
Any cycle would have to contain a vertical edge away from the line $m=0$, but $T$ contains no such edge.
Hence $T$ is acyclic.
:::

<1>3. The edges outside $T$ are precisely the vertical $b$-edges
\[
e_{m,n}:(m,n)\to(m,n+1)
\]
with
\[
m\ne0,
\qquad n\in\mathbb Z.
\]
::: {.proof}
All horizontal edges belong to $T$, and among vertical edges exactly those on the axis $m=0$ belong to $T$.
:::

<1>4. The basis loop associated to $e_{m,n}$ reads the word
\[
\gamma_{m,n}
=b^n a^m b a^{-m}b^{-n-1}.
\]
::: {.proof}
Starting at $(0,0)$, the unique path in $T$ to $(m,n)$ first traverses $b^n$ along the vertical axis and then $a^m$ along the horizontal row.
Next traverse the non-tree edge $b$ from $(m,n)$ to $(m,n+1)$.
The unique return path in $T$ goes horizontally by $a^{-m}$ to $(0,n+1)$ and then vertically by $b^{-n-1}$ to the origin.
Concatenating gives the displayed word.
:::

<1>5. Therefore
\[
\boxed{
F'=F\bigl(\gamma_{m,n}:m\in\mathbb Z\setminus\{0\},\ n\in\mathbb Z\bigr)
}
\]
freely, where
\[
\gamma_{m,n}=b^n a^m b a^{-m}b^{-n-1}.
\]
::: {.proof}
For any connected graph, choosing a maximal tree gives a free basis for the fundamental group indexed by the edges outside the tree.
By <1>1 the fundamental group of this covering graph is exactly the subgroup $F'$, and by <1>2--<1>4 the corresponding basis is the displayed family.
Each word has trivial abelianization, as expected.
:::
:::
