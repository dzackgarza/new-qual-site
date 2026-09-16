---
schema: qual/card@1
id: D-3UY5O
kind: definition
title: Lefschetz number
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a finite simplicial complex, or a retract of one, and let $f\colon X\to X$ be a continuous map.
The \dfn{Lefschetz number} of $f$ is
$$
\tau(f) \coloneqq \sum_{n\geq 0} (-1)^n \tr\qty{ f_*\colon H_n(X;\QQ) \to H_n(X;\QQ) }
.$$
:::

::: {.remark}
Since $\tr\qty{\id_{H_n(X;\QQ)}} = \dim_\QQ H_n(X;\QQ)$, the identity has $\tau(\id_X) = \chi(X)$, the [[D-QK5BM|Euler characteristic]].
By the Lefschetz fixed point theorem, if $\tau(f)\neq 0$, then $f$ has a fixed point.
:::

::: {.concept}
[@Hat02, §2.C, Theorem 2C.3, p. 179].
:::
