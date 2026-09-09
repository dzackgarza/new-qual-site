---
schema: qual/card@1
id: E-HAT-1.A-3
kind: problem
title: Euler characteristic and rank of fundamental group of a finite graph
classification:
  areas:
  - topology
  topics:
  - Graphs
  - Euler Characteristic
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the edge-vertex count for trees and collapse of a maximal tree to a wedge of circles.
---

For a finite graph $X$ define the Euler characteristic $\chi(X)$ to be the number of vertices minus the number of edges.
Show that $\chi(X) = 1$ if $X$ is a tree, and that the rank (number of elements in a basis) of $\pi_1(X)$ is $1 - \chi(X)$ if $X$ is connected.


::: {.solution}
Write
\[
V=\#\{\text{vertices of }X\},
\qquad
E=\#\{\text{edges of }X\}.
\]

<1>1. A finite tree with $V$ vertices has exactly $V-1$ edges.
::: {.proof}
Induct on $V$.
For $V=1$ there are no edges.
If $V>1$, a finite tree has a leaf vertex $v$ of degree one.
Deleting $v$ and its unique incident edge leaves a tree with $V-1$ vertices.
By induction it has $V-2$ edges, so the original tree has
\[
(V-2)+1=V-1
\]
edges.
:::

<1>2. Hence if $X$ is a finite tree,
\[
\boxed{\chi(X)=1.}
\]
::: {.proof}
By <1>1,
\[
\chi(X)=V-E=V-(V-1)=1.
\]
:::

<1>3. Now suppose $X$ is a finite connected graph and let $T\subseteq X$ be a maximal tree.
Then $T$ contains all vertices of $X$ and has $V-1$ edges.
::: {.proof}
A maximal tree in a connected finite graph is spanning: if a vertex lay outside it, a shortest edge path from the tree to that vertex would allow one more edge and vertex to be adjoined without creating a cycle, contradicting maximality.
Then <1>1 gives $V-1$ edges in $T$.
:::

<1>4. Collapsing $T$ to a point gives a homotopy equivalence
\[
X\simeq \bigvee^{E-V+1}S^1.
\]
::: {.proof}
A tree is contractible, and collapsing a contractible subcomplex of a graph to a point is a homotopy equivalence.
Every edge of $X\setminus T$ becomes a circle after the collapse.
The number of such edges is
\[
E-(V-1)=E-V+1.
\]
:::

<1>5. Therefore
\[
\pi_1(X)\cong F_{E-V+1},
\]
so its rank is
\[
E-V+1=1-(V-E)=\boxed{1-\chi(X)}.
\]
::: {.proof}
The fundamental group of a wedge of $r$ circles is the free group of rank $r$.
Apply <1>4 and the definition
\[
\chi(X)=V-E.
\]
:::
:::
