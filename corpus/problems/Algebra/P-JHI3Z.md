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

::: problem
What is a nilpotent matrix?
:::

::: {.solution}
A square matrix $A$ over a ring or field is **nilpotent** if
\[
A^r=0
\]
for some integer $r\ge1$.

The least such $r$, when it exists, is the **nilpotency index** of $A$.

Over a field, the following are equivalent:

1. $A$ is nilpotent;
2. the minimal polynomial of $A$ is $x^r$ for some $r\ge1$;
3. over an algebraic closure, every eigenvalue of $A$ is $0$;
4. the Jordan form of $A$ consists entirely of nilpotent Jordan blocks $J_s(0)$.

In particular, an $n\times n$ nilpotent matrix satisfies $A^n=0$.
:::
