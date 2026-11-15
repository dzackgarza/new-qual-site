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
---

::: {.exercise}

Give an example to show that the second part of Lemma 84.2 need not hold if $T$ is infinite.

:::

::: {.solution}

The second part of Lemma 84.2 (printed p. 507) is the converse: if $T$ is a finite tree in $X$ consisting of more than one edge, then $T=T_0\cup A$ where $T_0$ is a tree in $X$ and the edge $A$ meets $T_0$ in a single vertex.

Let $T$ be the linear graph with vertex set $\ZZ$ and one edge joining $n$ to $n+1$ for each integer $n$ (Definition of a linear graph, printed p. 502). It is connected: any two vertices are joined by an edge path along the line (Lemma 84.1, printed p. 506). It contains no closed reduced edge path: in this graph two consecutive edges with opposite orientations are the same edge, so a reduced edge path has all its steps in the same direction, traversing each vertex at most once, and no such path is closed. Hence $T$ is a tree (Definition, printed p. 507).

Suppose the conclusion of the second part of Lemma 84.2 held for this $T$: suppose
$$
T=T_0\cup A,
$$
where $T_0$ is a tree and the edge $A$ meets $T_0$ in exactly one vertex. Let $v$ be the other endpoint of $A$. Since $v\notin T_0$ and $T=T_0\cup A$, every edge of $T$ incident to $v$ must be $A$ itself. Thus $v$ would be incident with exactly one edge of $T$, that is, it would have degree $1$.

But every vertex of the bi-infinite line is the endpoint of exactly two edges, the one joining it to its predecessor and the one joining it to its successor. This contradiction shows that no such decomposition exists. Hence the finiteness hypothesis in the second part of Lemma 84.2 cannot be dropped.

:::
