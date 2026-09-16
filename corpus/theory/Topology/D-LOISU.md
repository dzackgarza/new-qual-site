---
schema: qual/card@1
id: D-LOISU
kind: definition
title: Dimension of a manifold
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
relations: []
review: draft
---

::: {.proposition}
Let $M$ be an $n$-[[D-UBWVX|manifold]] and $x\in M$.
Then $H_i(M, M\sm\ts{x};\ZZ)\cong\ZZ$ for $i = n$ and $H_i(M, M\sm\ts{x};\ZZ) = 0$ for $i\neq n$.
In particular, a nonempty space that is both an $m$-manifold and an $n$-manifold has $m = n$.
:::

::: {.definition}
Let $M$ be a nonempty space that is an $n$-manifold for some $n\geq 0$.
The \dfn{dimension} of $M$ is this integer $n$, equivalently the unique $i$ with $H_i(M, M\sm\ts{x};\ZZ)\neq 0$ for any $x\in M$.
:::

::: {.concept}
See [@Hat02, §2.2, Theorem 2.26].
:::
