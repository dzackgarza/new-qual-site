---
schema: qual/card@1
id: PR-O5YUI
kind: proposition
title: $V\dual\tensor_k W\cong\Hom_k(V,W)$ for finite-dimensional $V$ and $W$
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Tensor Products
  - Linear Algebra
relations:
- kind: variant-of
  target: PR-LPJLD
review: draft
---

::: {.proposition}
Let $k$ be a field and let $V$ and $W$ be finite-dimensional $k$-vector spaces.
The $k$-linear map
$$
\begin{aligned}
\Phi\colon V\dual\tensor_k W &\to \Hom_k(V,W),\\
\tilde v\tensor w &\mapsto \big(v\mapsto \tilde v(v)\,w\big),
\end{aligned}
$$
is an isomorphism.
:::

::: {.proof}
The map $V\dual\times W\to\Hom_k(V,W)$, $(\tilde v,w)\mapsto \tilde v(\wait)\,w$, is $k$-bilinear, so $\Phi$ is well defined by the universal property of the tensor product.
Let $e_1,\ldots,e_n$ be a basis of $V$ with dual basis $e_1^*,\ldots,e_n^*$ of $V\dual$, and let $f_1,\ldots,f_m$ be a basis of $W$.
The elements $e_i^*\tensor f_j$ form a basis of $V\dual\tensor_k W$.
The map $\Phi(e_i^*\tensor f_j)$ sends $e_i$ to $f_j$ and $e_l$ to $0$ for $l\neq i$; in these bases its matrix is the matrix unit $E_{ji}$.
The matrix units $E_{ji}$ form a basis of $\Hom_k(V,W)$, so $\Phi$ sends a basis to a basis and is an isomorphism.
:::
