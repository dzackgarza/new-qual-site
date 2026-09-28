---
schema: qual/card@1
id: PR-LPJLD
kind: proposition
title: $V^*\otimes W\cong\Hom(V,W)$ in finite dimensions
slogan: 'For finite-dimensional $V$, $V^*\otimes W$ is the space of linear maps $V\to W$.'
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Tensor Products
  - Linear Algebra
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and $V, W$ finite-dimensional $k$-vector spaces.
The $k$-linear map
$$
\begin{aligned}
\dualof{V} \tensor_k W &\to \Hom_k(V, W) \\
\tilde v \tensor w &\mapsto \big(x \mapsto \tilde v(x)\, w\big)
\end{aligned}
$$
is an isomorphism.
:::
