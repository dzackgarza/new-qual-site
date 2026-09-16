---
schema: qual/card@1
id: PR-DEG36
kind: proposition
title: Finite fields are not algebraically closed
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Fields
relations: []
review: draft
---

::: {.proposition}
A finite field $F$ is not [[FD-3GZPO|algebraically closed]].
:::

::: {.proof}
Write $F = \theset{a_1, \ldots, a_q}$ and let $f(x) \coloneqq 1 + \prod_{i=1}^q (x - a_i) \in F[x]$.
Then $f$ is nonconstant, and $f(a_j) = 1 \neq 0$ for every $j$, so $f$ has no root in $F$.
:::
