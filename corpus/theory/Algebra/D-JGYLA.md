---
schema: qual/card@1
id: D-JGYLA
kind: definition
title: Separable field extension
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
Let $L/k$ be a field extension.
An element $\alpha\in L$ that is algebraic over $k$ is \dfn{separable} over $k$ if its minimal polynomial over $k$ is [[D-ZT46D|separable]].
An algebraic extension $L/k$ is \dfn{separable} if every $\alpha\in L$ is separable over $k$.
:::

::: {.proposition}
An algebraic extension $L/k$ is separable if and only if every finite subextension $k\subseteq L'\subseteq L$ is separable over $k$.
:::

::: {.proof}
If $L/k$ is separable, every element of a subextension $L'$ is an element of $L$, hence separable over $k$.
Conversely, each $\alpha\in L$ lies in the finite subextension $k(\alpha)$, which is separable by hypothesis, so $\alpha$ is separable over $k$.
:::
