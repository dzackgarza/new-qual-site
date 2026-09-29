---
schema: qual/card@1
id: P-SP3A3
kind: problem
title: No $3\times 2$ matrix satisfies $A^t A=I_2$ and $AA^t=I_3$
classification:
  areas:
  - prelim
  topics:
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Does there exist a $3 \times 2$ complex matrix $A$ such that $A^t A = I_2$ and $A A^t = I_3$?
If so, give an example; if not, prove it.
Here $I_k$ is the $k \times k$ identity matrix.
:::

::: {.solution}

::: pf

::: pf-step
No such matrix exists.
:::

::: {.pf-step #s2}
For every $3\times2$ matrix $A$,
\[
\operatorname{rank}(AA^t)\le \operatorname{rank}(A)\le 2.
\]

::: pf-proof
The image of the linear map represented by $AA^t$ is contained in the image of the linear map represented by $A$, because
\[
AA^t x=A(A^t x)
\]
for every $x\in\mathbb C^3$. Hence $\operatorname{rank}(AA^t)\le\operatorname{rank}(A)$. Since $A$ has only two columns, $\operatorname{rank}(A)\le2$.
:::

:::

::: {.pf-step #s3}
Therefore $AA^t\ne I_3$.

::: pf-proof
The identity matrix $I_3$ has rank $3$, whereas step [](#s2){.pf-ref} gives $\operatorname{rank}(AA^t)\le2$.
:::

:::

::: pf-step
Consequently there is no $3\times2$ complex matrix satisfying both $A^tA=I_2$ and $AA^t=I_3$.

::: pf-proof
The second required equality is already impossible by step [](#s3){.pf-ref}.
:::

:::

:::
:::
