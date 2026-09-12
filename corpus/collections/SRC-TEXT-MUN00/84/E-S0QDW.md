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
---

::: {.exercise}

Give an example to show that the second part of Lemma 84.2 need not hold if $T$ is infinite.
:::

::: {.solution}
Let \(T\) be the bi-infinite linear graph with vertex set \(\mathbb Z\) and one edge joining \(n\) to \(n+1\) for each integer \(n\). This graph is connected and contains no closed reduced edge path, so it is a tree.

Suppose the converse conclusion of Lemma 84.2 held: suppose
\[
T=T_0\cup A,
\]
where \(T_0\) is a tree and the edge \(A\) meets \(T_0\) in exactly one vertex. Let the other endpoint of \(A\) be \(v\). Since \(v\notin T_0\), every edge of \(T\) incident to \(v\) must equal \(A\). Thus \(v\) would have degree \(1\) in \(T\).

But every vertex of the bi-infinite line has degree \(2\). This contradiction shows that no such decomposition exists. Hence the finiteness hypothesis in the second part of Lemma 84.2 is essential.
:::
