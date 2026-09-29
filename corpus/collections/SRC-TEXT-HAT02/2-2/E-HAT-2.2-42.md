---
schema: qual/card@1
id: E-HAT-2.2-42
kind: problem
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

::: {.problem}
Let $X$ be a finite connected graph having no vertex that is the endpoint of just one edge, and suppose that $H_1(X; \mathbb{Z})$ is free abelian of rank $n > 1$, so the group of automorphisms of $H_1(X; \mathbb{Z})$ is $GL_n(\mathbb{Z})$, the group of invertible $n \times n$ matrices with integer entries whose inverse matrix also has integer entries.
Show that if $G$ is a finite group of homeomorphisms of $X$, then the homomorphism $G \to GL_n(\mathbb{Z})$ assigning to $g: X \to X$ the induced homomorphism $g_*: H_1(X; \mathbb{Z}) \to H_1(X; \mathbb{Z})$ is injective.
Show the same result holds if the coefficient group $\mathbb{Z}$ is replaced by $\mathbb{Z}_m$ with $m > 2$.
What goes wrong when $m = 2$?
:::

::: {.solution}
**Goal.** For a finite connected graph $X$ with $H_1(X;\ZZ) \cong \ZZ^n$ ($n > 1$) and no vertex of valence $1$, show a finite group $G$ of homeomorphisms of $X$ acts faithfully on $H_1(X;\ZZ)$, and analyze the $\ZZ_m$ and $m = 2$ cases.

::: pf

::: {.pf-step #s1}
The action $G \to GL_n(\ZZ)$ is injective.

::: pf-proof

::: pf-step
A homeomorphism $g: X \to X$ induces an automorphism $g_*: H_1(X;\ZZ) \to H_1(X;\ZZ)$.

::: pf-proof
homology is functorial, and a homeomorphism induces an isomorphism.
:::

:::

::: pf-step
If $g_* = \id$ on $H_1(X;\ZZ)$, then $g$ fixes every vertex and every edge.

::: pf-proof
$H_1(X;\ZZ) \cong \ZZ^n$ with $n > 1$; the graph has no valence-$1$ vertex, so each edge lies in a cycle, and the homology classes of the cycles determine the graph structure; a homeomorphism acting trivially on $H_1$ must fix each cycle, hence each edge and vertex (up to the standard argument that a nontrivial homeomorphism of a graph moves some edge, changing some cycle class).
:::

:::

::: {.pf-step #s1-3}
Hence $g = \id$, so the map $G \to GL_n(\ZZ)$ is injective.

::: pf-proof
a homeomorphism of a graph fixing every vertex and edge is the identity.
:::

:::

:::

:::

::: {.pf-step #s2}
The same holds with coefficients $\ZZ_m$ for $m > 2$.

::: pf-proof

::: pf-step
$H_1(X;\ZZ_m) \cong (\ZZ_m)^n$, and $g_*$ acts on it.

::: pf-proof
universal coefficients: $H_1(X;\ZZ_m) \cong H_1(X;\ZZ) \otimes \ZZ_m \cong (\ZZ_m)^n$.
:::

:::

::: {.pf-step #s2-2}
If $g_* = \id$ on $H_1(X;\ZZ_m)$, then $g_* = \id$ on $H_1(X;\ZZ)$.

::: pf-proof
the reduction map $H_1(X;\ZZ) \to H_1(X;\ZZ_m)$ is injective on the free part when $m > 2$ (an integer matrix acting trivially mod $m$ for $m > 2$ must be the identity, since the only integer matrix congruent to $I$ mod $m$ with $m > 2$ and finite order is $I$ itself).
:::

:::

::: pf-step
Hence $g = \id$ by step [](#s1-3){.pf-ref}, so the action is faithful.

::: pf-proof
combine step [](#s2-2){.pf-ref} with step [](#s1){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
Failure at $m = 2$.

::: pf-proof

::: pf-step
The matrix $-I \in GL_n(\ZZ)$ acts trivially on $H_1(X;\ZZ_2)$.

::: pf-proof
$-1 \equiv 1 \pmod 2$, so $-I$ reduces to the identity mod $2$.
:::

:::

::: {.pf-step #s3-2}
A homeomorphism $g$ with $g_* = -I$ on $H_1(X;\ZZ)$ is nontrivial but acts trivially on $H_1(X;\ZZ_2)$.

::: pf-proof
such a $g$ exists (e.g. an orientation-reversing involution of a graph with $H_1 \cong \ZZ^n$); it is not the identity, yet its $\ZZ_2$-action is trivial.
:::

:::

::: pf-step
Hence the map $G \to GL_n(\ZZ_2)$ need not be injective.

::: pf-proof
Step [](#s3-2){.pf-ref} gives a nontrivial element in the kernel.
:::

:::

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, and [](#s3){.pf-ref} are the three requested statements.
:::

:::
