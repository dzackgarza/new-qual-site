---
schema: qual/card@1
id: E-HK-6WTC
kind: exercise
title: Inconsistent system of three equations in four unknowns
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
Show that the system

$$
\begin{array}{l} x _ {1} - 2 x _ {2} + x _ {3} + 2 x _ {4} = 1 \\ x _ {1} + x _ {2} - x _ {3} + x _ {4} = 2 \\ x _ {1} + 7 x _ {2} - 5 x _ {3} - x _ {4} = 3 \end{array}
$$

has no solution.
:::

::: {.solution}
<1>1. The third equation minus $3$ times the second equation plus $2$ times the first equation gives $0 = -1$.
<2>1. Left-hand side: $(x_1 + 7x_2 - 5x_3 - x_4) - 3(x_1 + x_2 - x_3 + x_4) + 2(x_1 - 2x_2 + x_3 + 2x_4) = 0$.
::: {.proof}
the coefficients cancel: $x_1 - 3x_1 + 2x_1 = 0$, $7x_2 - 3x_2 - 4x_2 = 0$, $-5x_3 + 3x_3 + 2x_3 = 0$, $-x_4 - 3x_4 + 4x_4 = 0$.
:::
<2>2. Right-hand side: $3 - 3(2) + 2(1) = 3 - 6 + 2 = -1$.
::: {.proof}
arithmetic.
:::

<1>2. Hence any solution would satisfy $0 = -1$, a contradiction.
::: {.proof}
<1>1.
:::

<1>3. Therefore the system has no solution.
::: {.proof}
<1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.
:::
:::
