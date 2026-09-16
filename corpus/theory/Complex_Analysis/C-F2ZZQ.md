---
schema: qual/card@1
id: C-F2ZZQ
kind: corollary
title: Identity principle
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
---

::: {.corollary}
Let $\Omega\subseteq\CC$ be a connected open set and let $f,g$ be [[D-E7A5W|holomorphic]] on $\Omega$.
If $f=g$ on a subset of $\Omega$ that has a [[D-TFSPT|limit point]] in $\Omega$, then $f=g$ on $\Omega$.
:::

::: {.proof}
The function $f-g$ is holomorphic on $\Omega$, and its [[D-65VIK|zeros]] have a limit point in $\Omega$.
The zeros of a holomorphic function on a connected open set that is not identically zero are isolated, so $f-g\equiv0$.
:::
