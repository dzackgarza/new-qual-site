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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card put its verdict ('No such matrix exists.') as its
    *first* step with no proof, followed by the rank argument; the verdict is now the closing
    step and follows from the rank inequality. Added: the reason an identity matrix has full
    rank, and the observation that the condition A^t A = I_2 is not needed. The answer is
    unchanged. Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---

::: {.problem}
Does there exist a $3 \times 2$ complex matrix $A$ such that $A^t A = I_2$ and $A A^t = I_3$?
If so, give an example; if not, prove it.
Here $I_k$ is the $k \times k$ identity matrix.
:::

::: {.solution}
Throughout $A$ is a $3 \times 2$ complex matrix, $A^{t}$ its transpose, $I_{k}$ the $k \times k$ identity, and $\operatorname{rank}$ the rank of the linear map it represents. The collection's `provenance` is the Spring 2003 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #rank}
For every $3 \times 2$ complex matrix $A$ one has $\operatorname{rank}(AA^{t}) \le \operatorname{rank}(A) \le 2$.

::: pf-proof
For $x \in \CC^{3}$ one has $AA^{t}x = A(A^{t}x)$, so the image of $AA^{t}$ is contained in the image of $A$; the rank is the dimension of the image, so $\operatorname{rank}(AA^{t}) \le \operatorname{rank}(A)$. The matrix $A$ has two columns, so its image is spanned by two vectors and has dimension at most $2$.

:::

:::

::: pf-step
No such matrix exists: there is no $3 \times 2$ complex $A$ with $AA^{t} = I_{3}$ and $A^{t}A = I_{2}$.

::: pf-proof
If $AA^{t} = I_{3}$ then $\operatorname{rank}(AA^{t}) = \operatorname{rank}(I_{3}) = 3$, since the identity has full rank. But step [](#rank){.pf-ref} gives $\operatorname{rank}(AA^{t}) \le 2$, a contradiction. Hence no such $A$ exists, and the answer to the question is no; the second condition $A^{t}A = I_{2}$ is not even needed for the argument.

:::

:::

:::
:::
