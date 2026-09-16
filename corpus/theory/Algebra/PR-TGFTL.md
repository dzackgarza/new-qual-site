---
schema: qual/card@1
id: PR-TGFTL
kind: proposition
title: The trace pairing identifies $\Hom(V,W)$ with $\Hom(W,V)\dual$
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Trace
  - Linear Algebra
relations:
- kind: variant-of
  target: PR-GXII2
review: draft
---

::: {.proposition}
Let $k$ be a field and let $V$ and $W$ be finite-dimensional $k$-vector spaces.
The map
$$
\begin{aligned}
\Hom_k(V, W) &\to \Hom_k(W, V)\dual,\\
T &\mapsto \big(S\mapsto\Tr(T \circ S)\big),
\end{aligned}
$$
is an isomorphism of $k$-vector spaces, where $T\circ S\colon W\to W$.
:::

::: {.proof}
The map is $k$-linear because the trace is, and both sides have dimension $\dim_k V\cdot\dim_k W$.
Choose bases, so that $T$ is an $m\times n$ matrix and $S$ an $n\times m$ matrix; then $\Tr(TS)=\sum_{a,b}T_{ab}S_{ba}$.
If $\Tr(TS)=0$ for all $S$, taking $S$ to be the matrix unit $E_{ba}$ gives $T_{ab}=0$ for all $a,b$, so $T=0$.
Thus the map is injective, hence an isomorphism.
:::
