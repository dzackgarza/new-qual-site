---
schema: qual/card@1
id: PR-ZO73V
kind: proposition
title: Tower law for field degrees
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.proposition}
Let $k\subseteq F\subseteq L$ be field extensions with $[L:F]$ and $[F:k]$ finite.
Then $[L:k]$ is finite and
$$
[L : k] = [L: F]\,[F: k].
$$
:::

::: {.proof}
Let $\alpha_1,\ldots,\alpha_m$ be a basis of $F$ over $k$ and $\beta_1,\ldots,\beta_n$ a basis of $L$ over $F$.
Every $x\in L$ is $\sum_j c_j\beta_j$ with $c_j\in F$, and each $c_j=\sum_i a_{ij}\alpha_i$ with $a_{ij}\in k$, so the $\alpha_i\beta_j$ span $L$ over $k$.
If $\sum_{i,j}a_{ij}\alpha_i\beta_j=0$ with $a_{ij}\in k$, then linear independence of the $\beta_j$ over $F$ gives $\sum_ia_{ij}\alpha_i=0$ for each $j$, and linear independence of the $\alpha_i$ over $k$ gives $a_{ij}=0$.
So the $mn$ products $\alpha_i\beta_j$ form a basis of $L$ over $k$.
:::
