---
schema: qual/card@1
id: PR-5PDNQ
kind: proposition
title: $V^*\otimes W^*\cong(V\otimes W)^*$ when one factor is finite-dimensional
slogan: 'With one finite-dimensional factor, dualizing a tensor product equals tensoring the duals.'
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Tensor Products
  - Vector Spaces
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and let $V, W$ be $k$-vector spaces, at least one of which is finite-dimensional.
The $k$-linear map
$$
\begin{aligned}
\dualof{V} \tensor_k \dualof{W} &\to \dualof{(V \tensor_k W)} \\
v \tensor w &\mapsto \big(x \tensor y \mapsto v(x)\, w(y)\big)
\end{aligned}
$$
is an isomorphism.
:::
