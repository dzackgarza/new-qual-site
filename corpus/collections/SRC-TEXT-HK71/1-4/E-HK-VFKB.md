---
schema: qual/card@1
id: E-HK-VFKB
kind: problem
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

::: pf

::: pf-step
The system
$$\begin{cases} x + y = 1 \\ x + y = 2 \end{cases}$$
has no solution.

::: pf-proof
the two equations are inconsistent.
:::

:::

::: {.pf-step #subtracting-gives-0eq1}
Justification: subtracting the first equation from the second gives $0 = 1$, a contradiction.

::: pf-proof
$(x + y) - (x + y) = 2 - 1$, i.e. $0 = 1$.
:::

:::

::: {.pf-step #no-pair-satisfies-both}
Hence no pair $(x, y)$ satisfies both equations.

::: pf-proof
Step [](#subtracting-gives-0eq1){.pf-ref}.
:::

:::

::: pf-qed
Step [](#no-pair-satisfies-both){.pf-ref}.
:::

:::

:::
