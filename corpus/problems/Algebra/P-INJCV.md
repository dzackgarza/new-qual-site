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

::: problem
What are the abelian groups of order 16?
:::


::: {.solution}
Since
\[
16=2^4,
\]
the finite abelian groups of order $16$ correspond to the partitions of $4$.
Thus there are exactly five isomorphism types:
\[
C_{16},
\qquad
C_8\times C_2,
\qquad
C_4\times C_4,
\qquad
C_4\times C_2\times C_2,
\qquad
C_2^4.
\]

These correspond respectively to the partitions
\[
4,\quad 3+1,\quad 2+2,\quad 2+1+1,\quad 1+1+1+1.
\]
By the classification theorem for finite abelian groups, the list is complete and the five groups are pairwise nonisomorphic.
:::
