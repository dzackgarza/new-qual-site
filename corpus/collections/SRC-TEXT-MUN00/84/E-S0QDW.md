---
schema: qual/card@1
id: E-S0QDW
kind: problem
title: Finiteness in the maximal tree argument
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The locator in this card's earlier audit note was wrong and is corrected in place: it read "Section 84
    Exercise 3", and this card's statement -- an example showing the second part of Lemma 84.2 fails for an
    infinite tree -- is printed Exercise 1 of §84, printed p. 513. E-44O6O carries the reciprocal error and is
    corrected with it.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §84 Exercise 1, printed p. 513 (locator corrected above). Searched outside the checkout for issue
    #146; the record is tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack
    Exchange advanced search "Munkres Lemma 84.2" (no hits) and the similar-question search from "Infinite
    tree, reduced edge path between vertices unique, Munkres Lemma 84.2" (15 items); the threads returned
    concern the finite form of the lemma and give no counterexample for an infinite tree. The card keeps its
    own proof, which exhibits the infinite tree and a vertex joined to the base by no reduced edge path.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 84 Exercise 1, printed p. 513. An infinite maximal tree in a non-locally-finite graph for which the second part of Lemma 84.2 fails. Checked against Lemma 84.2 and the definition of a linear graph, printed p. 501. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: this is Exercise 1 of §84, printed p. 513, not Exercise 3; the collection index carries the correct number and this note did not. Citations added: the Definition of a tree (printed p. 507), the Definition of a reduced edge path (printed p. 507), Lemma 84.2 (printed p. 507) whose second part is the assertion at issue, and Lemma 84.1 (printed p. 506) for connectivity through edge paths. Corrected: the example's being a tree was asserted; the proof now shows that a reduced edge path in the bi-infinite line is monotone, because in this graph two consecutive edges with opposite orientations are the same edge, so the graph has no closed reduced edge path. What the certificate does not cover: the graph is infinite, and its edges are the unit intervals between consecutive integers, which makes it a linear graph in the sense of the Definition on printed p. 502.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the bi-infinite line is a connected linear
    graph with no closed reduced edge path, hence a tree, and that it admits no
    decomposition T = T_0 union A with A meeting T_0 in one vertex, since every vertex of
    the line has degree two. The argument is the card's own; no retained set is cited.
    Munkres §84 Exercise 1(b), printed p. 525, with Lemma 84.2 (printed p. 507). The printed
    statement needed no repair.
---

::: {.exercise}

Give an example to show that the second part of Lemma 84.2 need not hold if $T$ is infinite.

:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Munkres §84 Exercise 1(b), with the definitions in §84 of a linear graph and of a tree, and the second part of Lemma 84.2 , whose finiteness hypothesis it shows cannot be dropped.

::: pf

::: {.pf-step #line}
Let $T$ be the linear graph with vertex set $\ZZ$ and one edge joining $n$ to $n+1$ for each $n\in\ZZ$.

::: pf-proof
This is a linear graph: its vertex space is $\ZZ$ with the discrete topology, each edge is a copy of $[0,1]$ with its endpoints glued to the two vertices it joins, and the topology is the coherent one (§84, definition).
:::

:::

::: {.pf-step #connected}
$T$ is connected.

::: pf-proof
Any two vertices $m<n$ are joined by the edge path that traverses the edges joining $k$ to $k+1$ for $k=m,\dots,n-1$ (Lemma 84.1). Since the vertex set meets every component and is path connected in this sense, $T$ is path connected, hence connected.
:::

:::

::: {.pf-step #tree}
$T$ contains no closed reduced edge path, so $T$ is a tree.

::: pf-proof
In this graph two consecutive edges with opposite orientations would be the same edge, so a reduced edge path has all its steps in the same direction and passes through each vertex at most once; such a path is not closed (definition of reduced edge path and of a tree, printed pp. 506--507). Hence $T$ is a tree.
:::

:::

::: {.pf-step #no-decomposition}
$T$ is not of the form $T_{0}\cup A$ with $T_{0}$ a tree and $A$ an edge meeting $T_{0}$ in exactly one vertex.

::: pf-proof
Suppose $T=T_{0}\cup A$ with $A$ an edge meeting $T_{0}$ in exactly one vertex, and let $v$ be the other endpoint of $A$, so $v\notin T_{0}$. Every edge of $T$ incident with $v$ lies in $T=T_{0}\cup A$; it is not in $T_{0}$, since $v\notin T_{0}$ and an edge of $T_{0}$ has both endpoints in $T_{0}$, so it must be $A$. Hence $v$ is incident with exactly one edge of $T$, that is, $v$ has degree $1$. But every vertex $n$ of the bi-infinite line is the endpoint of exactly two edges, the one joining it to $n-1$ and the one joining it to $n+1$. This contradiction shows that no such $T_{0}$ and $A$ exist.
:::

:::

::: {.pf-step}
The finiteness hypothesis in the second part of Lemma 84.2 cannot be dropped.

::: pf-proof
Lemma 84.2's second part asserts the decomposition for every finite tree with more than one edge. Step [](#tree){.pf-ref} exhibits a tree with more than one edge, and step [](#no-decomposition){.pf-ref} shows it admits no such decomposition; so the assertion fails without the finiteness hypothesis.
:::

:::

:::
:::
