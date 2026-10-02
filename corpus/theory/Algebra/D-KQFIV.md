---
schema: qual/card@1
id: D-KQFIV
kind: definition
title: Perfect fields
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
relations: []
review: draft
---

::: {.definition}
A field $k$ is \dfn{perfect} if every irreducible polynomial in $k[x]$ is [[D-ZT46D|separable]].
:::

::: {.proposition}
For a field $k$, the following are equivalent:

1. $k$ is perfect;

2. every finite extension $F/k$ is [[D-JGYLA|separable]].
:::

::: {.proof}
If $k$ is perfect and $F/k$ is finite, then the minimal polynomial over $k$ of every $\alpha\in F$ is irreducible and therefore separable, so $F/k$ is separable.

Conversely, suppose every finite extension of $k$ is separable. If $f\in k[x]$ is irreducible and $\alpha$ is a root of $f$, then $k(\alpha)/k$ is finite and separable. Hence $\alpha$ is separable over $k$, so its minimal polynomial $f$ is separable. Thus $k$ is perfect.
:::
