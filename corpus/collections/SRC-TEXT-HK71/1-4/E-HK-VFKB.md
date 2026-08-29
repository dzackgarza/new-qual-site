---
schema: qual/card@1
id: E-HK-VFKB
kind: exercise
title: Inconsistent system of two equations in two unknowns
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
Give an example of a system of two linear equations in two unknowns which has no solution.
:::

::: {.solution}
<1>1. The system
$$\begin{cases} x + y = 1 \\ x + y = 2 \end{cases}$$
has no solution.
Proof: the two equations are inconsistent.

<1>2. Justification: subtracting the first equation from the second gives $0 = 1$, a contradiction.
Proof: $(x + y) - (x + y) = 2 - 1$, i.e. $0 = 1$.

<1>3. Hence no pair $(x, y)$ satisfies both equations.
Proof: <1>2.

<1>4. Q.E.D.
Proof: <1>3.
:::
