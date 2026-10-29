---
schema: qual/card@1
id: P-INJCV
kind: problem
title: Abelian groups of order 16
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
What are the abelian groups of order 16?
:::

::: {.solution}
Write $C_n$ for the cyclic group of order $n$.

::: pf

::: pf-step

Up to isomorphism, the abelian groups of order $16$ are exactly the five pairwise nonisomorphic groups
$$
\boxed{C_{16},
\qquad
C_8\times C_2,
\qquad
C_4\times C_4,
\qquad
C_4\times C_2\times C_2,
\qquad
C_2^4.}
$$

::: pf-proof

Since $16=2^4$, the classification theorem for finite abelian groups puts the isomorphism types of abelian groups of order $16$ in bijection with the partitions of $4$, a partition $4=a_1+\cdots+a_r$ corresponding to $C_{2^{a_1}}\times\cdots\times C_{2^{a_r}}$.
The partitions $4$, $3+1$, $2+2$, $2+1+1$ and $1+1+1+1$ give the five groups in the order listed.

:::

:::

:::

:::
