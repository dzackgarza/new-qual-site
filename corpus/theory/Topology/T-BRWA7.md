---
schema: qual/card@1
id: T-BRWA7
kind: theorem
title: The five lemma
slogan: 'Exact rows and isomorphisms on the neighboring terms force the middle map to be an isomorphism.'
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.theorem}
Suppose the rows in the commutative diagram
\begin{tikzcd}
A \ar[r,"f"] \ar[d,"\alpha"'] &
B \ar[r,"g"] \ar[d,"\beta"'] &
C \ar[r,"h"] \ar[d,"\gamma"'] &
D \ar[r,"i"] \ar[d,"\delta"'] &
E \ar[d,"\varepsilon"'] \\
A' \ar[r,"f'"'] & B' \ar[r,"g'"'] & C' \ar[r,"h'"'] & D' \ar[r,"i'"'] & E'
\end{tikzcd}
are exact.
If $\alpha$ is surjective, $\beta$ and $\delta$ are isomorphisms, and $\varepsilon$ is injective, then $\gamma$ is an isomorphism [@Hat02, §2.1, Five-Lemma].
:::
