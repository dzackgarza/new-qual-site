---
schema: qual/card@1
id: D-O4WWN
kind: definition
title: Nondegenerate bilinear form
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Vector Spaces
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field, $V$ a $k$-vector space, and $b\colon V\times V \to k$ a bilinear form.
The form $b$ is \dfn{nondegenerate} if its adjoint map
$$
\begin{aligned}
V &\to V^{\vee} \\
x &\mapsto b(x, \wait)
\end{aligned}
$$
is injective.
:::

::: {.remark}
The kernel of the adjoint map is $\theset{ x \in V \st b(x,y) = 0 \text{ for all } y \in V }$, so $b$ is nondegenerate if and only if this subspace is zero.
If $\dim_k V = n< \infty$, then $\dim_k V^{\vee}=n$, so the adjoint map is injective if and only if it is an isomorphism; with respect to a basis $e_1,\ldots,e_n$ of $V$ and its dual basis, the adjoint map has matrix the transpose of the [[D-H4TDM|Gram matrix]] $\bigl(b(e_i,e_j)\bigr)_{i,j}$, so $b$ is nondegenerate if and only if a Gram matrix of $b$ is invertible.
:::

::: {.concept}
See Artin, *Algebra*, ch. 8.
:::
