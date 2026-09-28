---
schema: qual/card@1
id: PR-GXII2
kind: proposition
title: The trace pairing identifies $\Hom(V,W)$ with $\dualof{\Hom(W,V)}$
slogan: 'Trace of composition gives a perfect pairing between the two opposite Hom spaces.'
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Trace
  - Linear Algebra
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and $V, W$ finite-dimensional $k$-vector spaces.
The map
$$
\begin{aligned}
\Hom_k(V, W) &\to \dualof{\Hom_k(W, V)} \\
T &\mapsto \big(S \mapsto \Tr(T \circ S)\big)
\end{aligned}
$$
is an isomorphism of $k$-vector spaces, where $T \circ S\colon W \to W$.
:::
