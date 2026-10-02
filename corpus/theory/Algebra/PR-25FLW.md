---
schema: qual/card@1
id: PR-25FLW
kind: proposition
title: Algebraic extensions of perfect fields are separable
slogan: 'In characteristic zero or over a finite field, every algebraic extension is separable.'
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
  - Fields
relations:
- kind: uses
  target: D-KQFIV
review: draft
---

::: {.proposition}
Let $k$ be a [[D-KQFIV|perfect field]].
Then every algebraic extension $L/k$ is [[D-JGYLA|separable]].
In particular, this holds when $k$ has characteristic zero or when $k$ is finite.
:::

::: {.proof}
For $\alpha\in L$, the minimal polynomial of $\alpha$ over $k$ is irreducible in $k[x]$, hence separable, so $\alpha$ is separable over $k$.
:::
