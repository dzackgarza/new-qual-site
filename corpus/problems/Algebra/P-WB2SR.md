---
schema: qual/card@1
id: P-WB2SR
kind: problem
title: A basis of $V$ yields a basis of $V^{\oplus m}$
classification:
  areas:
  - algebra
  topics:
  - Bases
  - Vector Spaces
  - Direct Products
relations: []
review: draft
---

::: problem
Let $V$ be an $n$-dimensional vector space with basis $\mathcal B=\{b_1,\ldots,b_n\}$. Construct a basis of $V^{\oplus m}$ and compute its dimension.
:::

::: solution
For $1\le i\le m$ and $1\le k\le n$, let
\[
e_{i,k}=(0,\ldots,0,b_k,0,\ldots,0)\in V^{\oplus m},
\]
where $b_k$ occurs in the $i$th summand. Set
\[
\mathcal B^{(m)}=\{e_{i,k}:1\le i\le m,\ 1\le k\le n\}.
\]

To see that it spans, let $v=(v_1,\ldots,v_m)$. Write
\[
v_i=\sum_{k=1}^n a_{i,k}b_k.
\]
Then
\[
v=\sum_{i=1}^m\sum_{k=1}^n a_{i,k}e_{i,k}.
\]

For linear independence, suppose
\[
\sum_{i,k}a_{i,k}e_{i,k}=0.
\]
Looking in the $i$th summand gives
\[
\sum_{k=1}^n a_{i,k}b_k=0.
\]
Since $\mathcal B$ is a basis, every $a_{i,k}=0$.

Hence $\mathcal B^{(m)}$ is a basis and
\[
\dim(V^{\oplus m})=mn=m\dim V.
\]
:::
