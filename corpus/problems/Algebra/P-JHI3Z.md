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
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks what
    a nilpotent matrix is, so its answer is a definition, not a proposition, and
    a structured proof has nothing to prove — no `pf` block was added, because
    one here would be invented structure rather than a proof. What was checked:
    the definition in the solution agrees with the one on the definition card
    D-GIGM2 (nilpotent element: r^n = 0 for some n >= 1), so the solution adds
    no second defining occurrence; the least such r is the nilpotency index, and
    that is a definition rather than a claim; the remark's assertions (minimal
    polynomial x^r, eigenvalues 0, Jordan blocks J_s(0), and A^n = 0 by
    Cayley-Hamilton) are standard and are stated as a remark, not as part of the
    solution. What was not checked: no source solution exists for this card and
    none was compared; the remark's equivalences were not proved here, since they
    are outside the solution section.
---

::: {.problem}
What is a nilpotent matrix?
:::

::: {.solution}
A square matrix $A$ over a ring is [[D-GIGM2|nilpotent]] if $A^r=0$ for some integer $r\ge1$. The least such $r$ is the nilpotency index of $A$.
:::

::: {.remark}
For an $n\times n$ matrix $A$ over a field, the following are equivalent: $A$ is nilpotent; the minimal polynomial of $A$ is $x^r$ for some $r\ge1$; every eigenvalue of $A$ in an algebraic closure is $0$; the Jordan form of $A$ consists of blocks $J_s(0)$. In particular, a nilpotent $n\times n$ matrix over a field satisfies $A^n=0$, by the Cayley--Hamilton theorem applied to its characteristic polynomial $x^n$.
:::
