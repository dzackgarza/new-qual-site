---
schema: qual/card@1
id: P-C2FE5
kind: problem
title: Short five lemma
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: problem
Let $R$ be a ring with the following commutative diagram of $R\dash$modules, where each row represents a short exact sequence of $R\dash$modules:

\begin{tikzcd}
0 \ar[r] & A \ar[d, "\alpha"] \ar[r, "f"] & B \ar[d, "\beta"] \ar[r, "g"] & C \ar[r] \ar[d, "\gamma"] & 0 \\
0 \ar[r] & A' \ar[r, "f'"] & B'\ar[r, "g'"] & C' \ar[r] & 0 
\end{tikzcd}

Prove that if $\alpha$ and $\gamma$ are isomorphisms then $\beta$ is an isomorphism.
:::
