---
schema: qual/card@1
id: E-HK-OAOP
kind: exercise
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
<1>1. $C = AB$ is a $2 \times 2$ matrix of rank at most $1$.
::: {.proof}
$A$ has rank at most $1$ (it is $2 \times 1$), and $\operatorname{rank}(AB) \le \operatorname{rank}(A) \le 1$.
:::

<1>2. A $2 \times 2$ matrix is invertible iff it has rank $2$.
::: {.proof}
standard.
:::

<1>3. Hence $C$ has rank $\le 1 < 2$, so $C$ is not invertible.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.
:::
:::
