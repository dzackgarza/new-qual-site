---
schema: qual/card@1
id: T-BX4LD
kind: theorem
title: Lefschetz fixed point theorem
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homology
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a finite simplicial complex, or a retract of one, and let $f\colon X\to X$ be continuous with [[D-3UY5O|Lefschetz number]]
$$
\tau(f) = \sum_{k \geq 0} (-1)^k \tr\qty{f_*\colon H_k(X; \QQ) \to H_k(X; \QQ)}
.$$
If $\tau(f) \neq 0$, then $f$ has a fixed point [@Hat02].
:::
