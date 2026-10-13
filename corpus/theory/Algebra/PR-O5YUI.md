---
schema: qual/card@1
id: PR-O5YUI
kind: proposition
title: Tensor bases correspond to matrix units in $\Hom_k(V,W)$
slogan: 'Under $V^*\otimes W\cong\Hom(V,W)$, dual-basis tensors are matrix units.'
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Tensor Products
  - Linear Algebra
relations:
- kind: related-to
  target: PR-LPJLD
review: draft
---

::: {.proposition}
Let $k$ be a field and let $V$ and $W$ be finite-dimensional $k$-vector spaces.
Choose a basis $e_1,\ldots,e_n$ of $V$ with dual basis $e_1^*,\ldots,e_n^*$, and a basis $f_1,\ldots,f_m$ of $W$.
Under the canonical isomorphism [[PR-LPJLD]]
$$
\begin{aligned}
\Phi\colon V\dual\tensor_k W &\to \Hom_k(V,W),\\
\tilde v\tensor_k w &\mapsto \big(v\mapsto \tilde v(v)\,w\big),
\end{aligned}
$$
one has
$$
\Phi(e_i^*\tensor_k f_j)=E_{ji},
$$
where $E_{ji}$ is the linear map with $E_{ji}(e_i)=f_j$ and $E_{ji}(e_\ell)=0$ for $\ell\neq i$.
Consequently, if
$$
T(e_i)=\sum_{j=1}^m T_{ji}f_j,
$$
then
$$
\Phi^{-1}(T)=\sum_{i=1}^n\sum_{j=1}^m T_{ji}\,e_i^*\tensor_k f_j.
:::

::: {.proof}
By the definition of $\Phi$,
$$
\Phi(e_i^*\tensor_k f_j)(e_\ell)
=e_i^*(e_\ell)f_j
=\delta_{i\ell}f_j,
$$
which is exactly $E_{ji}$.
The displayed formula for $\Phi^{-1}(T)$ follows by linearity from the matrix expansion
$$
T=\sum_{i,j}T_{ji}E_{ji}.
$$
:::
