---
schema: qual/card@1
id: P-BW6LF
kind: problem
title: A space with $H_*(X)\cong(\ZZ,0,0,0,0,\ZZ_4,0,\ldots)$
classification:
  areas:
  - topology
  topics:
  - homology
  - cell-complexes
relations: []
review: draft
solved: true
---
Construct a space having $H_*(X) = [\ZZ, 0, 0, 0, 0, \ZZ_4, 0, \cdots]$.

:::{.solution}

\envlist
:::{.concept}
\envlist

- Construction of Moore Spaces
- $\tilde H_n(\Sigma X) = \tilde H_{n-1}(X)$, using $\Sigma X = C_X \union_X C_X$ and Mayer-Vietoris.
:::

Take $X = e^0 \union_{\Phi_1} e^5 \union_{\Phi_2} e^6$, where
\[
\Phi_1: \del B^5 = S^4 \mapsvia{z~\mapsto z^0} e^0 \\
\Phi_2: \del B^6 = S^5 \mapsvia{z~\mapsto z^4} e^5
.\]

where $\deg \Phi_2 = 4$.
:::
