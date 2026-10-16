---
schema: qual/card@1
id: P-G5HVP
kind: problem
title: A finite separable extension is normal iff it is the splitting field of a polynomial
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $L/K$ be a finite separable extension. Show that $L/K$ is normal if and only if $L$ is the splitting field over $K$ of some polynomial in $K[x]$.
:::

::: {.solution}
If $L/K$ is finite, separable, and normal, choose generators
\[
L=K(\alpha_1,\ldots,\alpha_r).
\]
Let $m_i$ be the minimal polynomial of $\alpha_i$ over $K$. Normality implies each $m_i$ splits in $L$, so $L$ is the splitting field of
\[
f=\prod_i m_i.
\]
Conversely, a splitting field is normal, and separability of $L/K$ ensures the relevant irreducible factors are separable. Hence the equivalence.
:::