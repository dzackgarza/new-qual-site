---
schema: qual/card@1
id: P-IHVQT
kind: problem
title: Tensor product
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Vector Spaces
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
What is a tensor product?
What is the universal property?
What do the tensors look like in the case of vector spaces?
:::

::: {.solution}
Let $V$ and $W$ be vector spaces over a field $k$.

::: pf

::: {.pf-step #construction}

The tensor product $V\otimes_k W$ is the quotient of the free vector space on the set $V\times W$ by the subspace spanned by
$$
\begin{aligned}
&(v+v',w)-(v,w)-(v',w), && (v,w+w')-(v,w)-(v,w'),\\
&(cv,w)-c(v,w), && (v,cw)-c(v,w),
\end{aligned}
$$
for $v,v'\in V$, $w,w'\in W$ and $c\in k$. The class of $(v,w)$ is written $v\otimes w$, and $\otimes\colon V\times W\to V\otimes_k W$ is bilinear.

::: pf-proof

The relations are exactly bilinearity of $(v,w)\mapsto v\otimes w$.

:::

:::

::: {.pf-step #universal}

(Universal property.) For every bilinear map $B\colon V\times W\to U$ there is a unique linear map $\widetilde B\colon V\otimes_k W\to U$ with $\widetilde B(v\otimes w)=B(v,w)$.

::: pf-proof

The linear map on the free vector space sending $(v,w)$ to $B(v,w)$ vanishes on the relations of step [](#construction){.pf-ref} because $B$ is bilinear, so it descends to the quotient. It is unique because the elements $v\otimes w$ span $V\otimes_k W$.

:::

:::

::: pf-step

If $\{e_i\}$ and $\{f_j\}$ are bases of $V$ and $W$, then $\{e_i\otimes f_j\}$ is a basis of $V\otimes_k W$, so every tensor is a finite sum $\sum_{i,j} c_{ij}\,e_i\otimes f_j$ with unique coefficients $c_{ij}\in k$.

::: pf-proof

Bilinearity expands each $v\otimes w$ as a combination of the $e_i\otimes f_j$, so they span.
For independence, fix $(i_0,j_0)$ and let $B(v,w)$ be the product of the $e_{i_0}$-coordinate of $v$ and the $f_{j_0}$-coordinate of $w$. This $B$ is bilinear, and by step [](#universal){.pf-ref} it induces a linear functional sending $e_i\otimes f_j$ to $1$ if $(i,j)=(i_0,j_0)$ and to $0$ otherwise. Applying these functionals to a vanishing combination shows that every coefficient is $0$.

:::

:::

:::

:::
