---
schema: qual/card@1
id: PR-TGFTL
kind: proposition
title: Matrix-unit duality for the trace pairing
slogan: 'Opposite matrix units are dual under trace of composition.'
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Trace
  - Linear Algebra
relations:
- kind: related-to
  target: PR-GXII2
review: draft
---

::: {.proposition}
Let $k$ be a field and let $V$ and $W$ be finite-dimensional $k$-vector spaces.
Choose bases $e_1,\ldots,e_n$ of $V$ and $f_1,\ldots,f_m$ of $W$.
For $1\leq a\leq m$ and $1\leq i\leq n$, let $E_{ai}\colon V\to W$ send $e_i$ to $f_a$ and every other $e_j$ to $0$.
For $1\leq j\leq n$ and $1\leq b\leq m$, let $F_{jb}\colon W\to V$ send $f_b$ to $e_j$ and every other $f_c$ to $0$.
Then
$$
\Tr(E_{ai}\circ F_{jb})=\delta_{ij}\delta_{ab}.
$$
Thus the matrix-unit bases of $\Hom_k(V,W)$ and $\Hom_k(W,V)$ are dual under the trace pairing.
:::

::: {.proof}
The composite $E_{ai}\circ F_{jb}\colon W\to W$ vanishes on every basis vector except possibly $f_b$, and
$$
(E_{ai}\circ F_{jb})(f_b)
=E_{ai}(e_j)
=\delta_{ij}f_a.
$$
Its matrix therefore has a single possible nonzero entry, equal to $\delta_{ij}$ in row $a$, column $b$.
Its trace is $\delta_{ij}$ when $a=b$ and $0$ otherwise, namely $\delta_{ij}\delta_{ab}$.
:::
