---
schema: qual/card@1
id: D-MENR4
kind: definition
title: Eilenberg-MacLane Space
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cohomology
  - Cell Complexes
relations: []
review: draft
---

::: {.definition title="Eilenberg-MacLane Space"}
For $n\geq 1$ and a group $G$, abelian if $n\geq 2$, an **Eilenberg-MacLane space** $K(G,n)$ is a CW complex with
\[
\pi_i(K(G,n)) =
\begin{cases}
G & i = n, \\
0 & i \neq n.
\end{cases}
\]
It exists for every such pair and is unique up to homotopy equivalence, and it represents cohomology:
\[
H^n(X; G) \cong [X, K(G,n)]
\]
for $X$ a CW complex.
Examples: $K(\ZZ,1) = S^1$, $K(\ZZ,2) = \CP^\infty$, $K(\ZZ/2, 1) = \RP^\infty$.
:::

::: {.concept}
See Hatcher, §4.2, p. 365; $K(G,1)$ spaces are §1.B, p. 87.
:::
