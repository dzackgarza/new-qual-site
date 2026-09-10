---
schema: qual/card@1
id: P-3Q4IQ
kind: problem
title: Abelian groups of order 36
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

::: problem
How many abelian groups are there of order 36?
:::


::: {.solution}
Since
\[
36=2^2 3^2,
\]
the $2$-primary part of an abelian group of order $36$ is either $C_4$ or $C_2\oplus C_2$, and independently the $3$-primary part is either $C_9$ or $C_3\oplus C_3$.

<1>1. There are exactly four isomorphism classes.
::: {.proof}
The partitions of $2$ are $2$ and $1+1$. Thus there are two choices for the $2$-primary component and two choices for the $3$-primary component. Primary decomposition is unique, so the total number is
\[
2\cdot2=4.
\]
:::

<1>2. In invariant-factor form the four groups are
\[
C_{36},\qquad
C_3\oplus C_{12},\qquad
C_2\oplus C_{18},\qquad
C_6\oplus C_6.
\]
::: {.proof}
Combine the primary possibilities using the Chinese remainder theorem:
\[
C_4\oplus C_9\cong C_{36},
\]
\[
C_4\oplus C_3\oplus C_3\cong C_3\oplus C_{12},
\]
\[
C_2\oplus C_2\oplus C_9\cong C_2\oplus C_{18},
\]
and
\[
C_2\oplus C_2\oplus C_3\oplus C_3\cong C_6\oplus C_6.
\]
These invariant-factor lists are pairwise distinct, hence so are the groups.
:::
:::
