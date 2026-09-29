---
schema: qual/card@1
id: E-HK-OAOP
kind: problem
title: Product of non-square matrices is not invertible
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Suppose $A$ is a $2 \times 1$ matrix and that $B$ is a $1 \times 2$ matrix.
Prove that $C = AB$ is not invertible.
:::

::: {.solution}

::: pf

::: {.pf-step #c-has-rank-at-most-1}
$C = AB$ is a $2 \times 2$ matrix of rank at most $1$.

::: pf-proof
$A$ has rank at most $1$ (it is $2 \times 1$), and $\operatorname{rank}(AB) \le \operatorname{rank}(A) \le 1$.
:::

:::

::: {.pf-step #square-2x2-invertible-iff-rank-2}
A $2 \times 2$ matrix is invertible iff it has rank $2$.

::: pf-proof
standard.
:::

:::

::: {.pf-step #c-not-invertible}
Hence $C$ has rank $\le 1 < 2$, so $C$ is not invertible.

::: pf-proof
Steps [](#c-has-rank-at-most-1){.pf-ref} and [](#square-2x2-invertible-iff-rank-2){.pf-ref}.
:::

:::

::: pf-qed
Step [](#c-not-invertible){.pf-ref}.
:::

:::

:::
