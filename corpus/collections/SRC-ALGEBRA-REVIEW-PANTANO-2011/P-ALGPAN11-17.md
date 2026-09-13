---
schema: qual/card@1
id: P-ALGPAN11-17
kind: problem
title: Abelian groups of order 16 with exponent dividing 4
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
Up to isomorphism, how many additive abelian groups $G$ of order $16$ satisfy $4x=0$ for every $x\in G$?

![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-17.png)
:::

::: {.solution}
There are $\boxed{3}$ such groups, so the answer is $\boxed{\text{(D)}}$.

<1>1. Use the classification of finite abelian $2$-groups.
::: {.proof}
An abelian group of order $16=2^4$ is a product of cyclic groups corresponding to a partition of $4$.
The condition $4x=0$ for every $x$ says the exponent divides $4$, so no cyclic factor may have order $8$ or $16$.
Hence all parts of the partition are at most $2$.

The partitions are
\[
2+2,\qquad2+1+1,\qquad1+1+1+1,
\]
giving
\[
C_4\times C_4,
\qquad C_4\times C_2\times C_2,
\qquad C_2^4.
\]
These are pairwise nonisomorphic and exhaust the possibilities.
:::
:::
