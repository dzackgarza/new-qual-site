---
schema: qual/card@1
id: P-JHI3Z
kind: problem
title: Nilpotent matrix
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Matrices
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
What is a nilpotent matrix?
:::

::: {.solution}
A square matrix $A$ over a ring is [[D-HGMOW|nilpotent]] if $A^r=0$ for some integer $r\ge1$. The least such $r$ is the nilpotency index of $A$.
:::

::: {.remark}
For an $n\times n$ matrix $A$ over a field, the following are equivalent: $A$ is nilpotent; the minimal polynomial of $A$ is $x^r$ for some $r\ge1$; every eigenvalue of $A$ in an algebraic closure is $0$; the Jordan form of $A$ consists of blocks $J_s(0)$. In particular, a nilpotent $n\times n$ matrix over a field satisfies $A^n=0$, by the Cayley--Hamilton theorem applied to its characteristic polynomial $x^n$.
:::
