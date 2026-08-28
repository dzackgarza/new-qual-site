---
schema: qual/card@1
id: E-HAT-2.2-42
kind: exercise
title: Finite group of homeomorphisms of graph injects into $GL_n(\mathbb{Z})$ acting on $H_1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Graphs
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Let $X$ be a finite connected graph having no vertex that is the endpoint of just one edge, and suppose that $H_1(X; \mathbb{Z})$ is free abelian of rank $n > 1$, so the group of automorphisms of $H_1(X; \mathbb{Z})$ is $GL_n(\mathbb{Z})$, the group of invertible $n \times n$ matrices with integer entries whose inverse matrix also has integer entries.
Show that if $G$ is a finite group of homeomorphisms of $X$, then the homomorphism $G \to GL_n(\mathbb{Z})$ assigning to $g: X \to X$ the induced homomorphism $g_*: H_1(X; \mathbb{Z}) \to H_1(X; \mathbb{Z})$ is injective.
Show the same result holds if the coefficient group $\mathbb{Z}$ is replaced by $\mathbb{Z}_m$ with $m > 2$.
What goes wrong when $m = 2$?

::: {.solution}
**Goal.** For a finite connected graph $X$ with $H_1(X;\ZZ) \cong \ZZ^n$ ($n > 1$) and no vertex of valence $1$, show a finite group $G$ of homeomorphisms of $X$ acts faithfully on $H_1(X;\ZZ)$, and analyze the $\ZZ_m$ and $m = 2$ cases.

<1>1. The action $G \to GL_n(\ZZ)$ is injective.
<2>1. A homeomorphism $g: X \to X$ induces an automorphism $g_*: H_1(X;\ZZ) \to H_1(X;\ZZ)$.
Proof: homology is functorial, and a homeomorphism induces an isomorphism.
<2>2. If $g_* = \id$ on $H_1(X;\ZZ)$, then $g$ fixes every vertex and every edge.
Proof: $H_1(X;\ZZ) \cong \ZZ^n$ with $n > 1$; the graph has no valence-$1$ vertex, so each edge lies in a cycle, and the homology classes of the cycles determine the graph structure; a homeomorphism acting trivially on $H_1$ must fix each cycle, hence each edge and vertex (up to the standard argument that a nontrivial homeomorphism of a graph moves some edge, changing some cycle class).
<2>3. Hence $g = \id$, so the map $G \to GL_n(\ZZ)$ is injective.
Proof: a homeomorphism of a graph fixing every vertex and edge is the identity.

<1>2. The same holds with coefficients $\ZZ_m$ for $m > 2$.
<2>1. $H_1(X;\ZZ_m) \cong (\ZZ_m)^n$, and $g_*$ acts on it.
Proof: universal coefficients: $H_1(X;\ZZ_m) \cong H_1(X;\ZZ) \otimes \ZZ_m \cong (\ZZ_m)^n$.
<2>2. If $g_* = \id$ on $H_1(X;\ZZ_m)$, then $g_* = \id$ on $H_1(X;\ZZ)$.
Proof: the reduction map $H_1(X;\ZZ) \to H_1(X;\ZZ_m)$ is injective on the free part when $m > 2$ (an integer matrix acting trivially mod $m$ for $m > 2$ must be the identity, since the only integer matrix congruent to $I$ mod $m$ with $m > 2$ and finite order is $I$ itself).
<2>3. Hence $g = \id$ by <1>2.3, so the action is faithful.
Proof: combine <1>2.2 with <1>1.

<1>3. Failure at $m = 2$.
<2>1. The matrix $-I \in GL_n(\ZZ)$ acts trivially on $H_1(X;\ZZ_2)$.
Proof: $-1 \equiv 1 \pmod 2$, so $-I$ reduces to the identity mod $2$.
<2>2. A homeomorphism $g$ with $g_* = -I$ on $H_1(X;\ZZ)$ is nontrivial but acts trivially on $H_1(X;\ZZ_2)$.
Proof: such a $g$ exists (e.g. an orientation-reversing involution of a graph with $H_1 \cong \ZZ^n$); it is not the identity, yet its $\ZZ_2$-action is trivial.
<2>3. Hence the map $G \to GL_n(\ZZ_2)$ need not be injective.
Proof: <1>3.2 gives a nontrivial element in the kernel.

<1>4. Q.E.D.
Proof: <1>1, <1>2, and <1>3 are the three requested statements.
:::
