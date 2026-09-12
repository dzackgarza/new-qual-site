---
schema: qual/card@1
id: P-APAS24E
kind: problem
title: Schur's lemma for complex representations of finite groups
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Give a complete statement and proof of Schur's Lemma, in the category of complex finite-dimensional representations of finite groups.
:::

::: solution
**Schur's Lemma.** Let $V$ and $W$ be finite-dimensional irreducible complex representations of a finite group $G$.

1. Every $G$-equivariant linear map $T\colon V\to W$ is either $0$ or an isomorphism.
2. In particular, every $G$-equivariant endomorphism $T\colon V\to V$ is multiplication by a scalar.

For (1), both $\ker T\subseteq V$ and $\operatorname{im}T\subseteq W$ are $G$-stable subspaces. Since $V$ and $W$ are irreducible,
\[
\ker T\in\{0,V\},
\qquad
\operatorname{im}T\in\{0,W\}.
\]
If $T\ne0$, then $\ker T\ne V$ and $\operatorname{im}T\ne0$, so
\[
\ker T=0,
\qquad
\operatorname{im}T=W.
\]
Thus $T$ is an isomorphism.

For (2), let $T\in\operatorname{End}_G(V)$. Because the field is $\mathbb C$, $T$ has an eigenvalue $\lambda\in\mathbb C$. Then
\[
T-\lambda I
\]
is again $G$-equivariant and has nonzero kernel, so by part (1) it cannot be an isomorphism. Hence it must be the zero map. Therefore
\[
T=\lambda I.
\]
Thus
\[
\boxed{\operatorname{End}_G(V)=\mathbb C\,I.}
\]
:::
