---
schema: qual/card@1
id: D-VUDRJ
kind: definition
title: "Relative homotopy groups"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Relative homotopy groups"}
For $x_0 \in A \subseteq X$ and $n\geq 1$,
\[
\pi_n(X, A, x_0) \da \ts{ f: (D^n, S^{n-1}, s_0) \to (X, A, x_0) } / \homotopic
,\]
homotopy classes through maps of triples.
This is a group for $n\geq 2$, abelian for $n\geq 3$, and only a pointed set for $n=1$.
It sits in a long exact sequence
\[
\cdots \to \pi_n(A, x_0) \to \pi_n(X, x_0) \to \pi_n(X, A, x_0) \mapsvia{\del} \pi_{n-1}(A, x_0)\to \cdots
.\]
:::

::: {.concept}
See Hatcher, §4.1, pp. 343-344.
:::
