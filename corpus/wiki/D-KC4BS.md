---
schema: qual/card@1
id: D-KC4BS
kind: definition
title: "Moore Space"
classification:
  areas:
  - topology
  topics:
  - homology
  - cell-complexes
relations: []
review: draft
---

::: {.definition title="Moore Space"}
For $G$ abelian and $n\geq 1$, a **Moore space** $M(G,n)$ is a CW complex with
\[
\tilde H_i(M(G,n);\ZZ) =
\begin{cases}
G & i = n, \\
0 & i \neq n.
\end{cases}
\]
One exists for every such $G$ and $n$, built by attaching $(n+1)\dash$cells to a wedge of $n\dash$spheres along a presentation of $G$; e.g. $M(\ZZ, n) = S^n$ and $M(\ZZ/m, n) = S^n \union_{\times m} e^{n+1}$.
:::

::: {.concept}
See Hatcher, §2.2, Example 2.40, p. 143.
:::
