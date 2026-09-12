---
schema: qual/card@1
id: P-X7AK4
kind: problem
title: A finite separable splitting field $L/K$ has $[L:K]=|\gal(L/K)|$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Separability
  - Splitting Fields
relations: []
review: draft
---

::: problem
Let $L/K$ be a finite separable extension which is the splitting field of a polynomial in $K[x]$. Prove
\[
[L:K]=|\operatorname{Gal}(L/K)|.
\]
:::

::: solution
Because $L/K$ is finite and separable, the primitive element theorem gives
\[
L=K(\alpha)
\]
for some $\alpha\in L$. Let $m_\alpha(x)$ be its minimal polynomial over $K$. Then
\[
\deg m_\alpha=[L:K].
\]

A $K$-embedding
\[
\sigma:L\hookrightarrow\overline K
\]
is determined by the image of $\alpha$, and $\sigma(\alpha)$ can be any root of $m_\alpha$. Since the extension is separable, $m_\alpha$ has exactly $[L:K]$ distinct roots. Hence there are exactly $[L:K]$ $K$-embeddings of $L$ into $\overline K$.

Because $L/K$ is a splitting field, it is normal. Therefore every $K$-embedding of $L$ into $\overline K$ has image equal to $L$, so every such embedding is a $K$-automorphism of $L$.

Thus
\[
|\operatorname{Gal}(L/K)|=[L:K].
\]
:::
