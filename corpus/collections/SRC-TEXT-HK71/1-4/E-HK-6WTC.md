---
schema: qual/card@1
id: E-HK-6WTC
kind: problem
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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The collection index records this card as Hoffman and Kunze 1.4.6, and the
    system it carries is the one the card states. The printed book was not
    re-read in this pass; the check is of the card against its indexed exercise
    number.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The certificate is correct. Taking the third equation minus three times the
    second plus twice the first kills all four unknowns on the left, since
    1 - 3 + 2, 7 - 3 - 4, -5 + 3 + 2 and -1 - 3 + 4 all vanish, while the right
    side becomes 3 - 6 + 2 = -1; a solution would therefore force 0 = -1. Nothing
    was changed.
---

::: {.exercise}
Show that the system

$$
\begin{aligned}
x_1 - 2x_2 + x_3 + 2x_4 &= 1\\
x_1 + x_2 - x_3 + x_4 &= 2\\
x_1 + 7x_2 - 5x_3 - x_4 &= 3
\end{aligned}
$$

has no solution.
:::

::: {.solution}

::: pf

::: {.pf-step #combination-gives-contradiction}
The third equation minus $3$ times the second equation plus $2$ times the first equation gives $0 = -1$.

::: pf-proof

::: pf-step
Left-hand side: $(x_1 + 7x_2 - 5x_3 - x_4) - 3(x_1 + x_2 - x_3 + x_4) + 2(x_1 - 2x_2 + x_3 + 2x_4) = 0$.

::: pf-proof
the coefficients cancel: $x_1 - 3x_1 + 2x_1 = 0$, $7x_2 - 3x_2 - 4x_2 = 0$, $-5x_3 + 3x_3 + 2x_3 = 0$, $-x_4 - 3x_4 + 4x_4 = 0$.
:::

:::

::: pf-step
Right-hand side: $3 - 3(2) + 2(1) = 3 - 6 + 2 = -1$.

::: pf-proof
arithmetic.
:::

:::

:::

:::

::: {.pf-step #any-solution-gives-contradiction}
Hence any solution would satisfy $0 = -1$, a contradiction.

::: pf-proof
Step [](#combination-gives-contradiction){.pf-ref}.
:::

:::

::: {.pf-step #no-solution}
Therefore the system has no solution.

::: pf-proof
Step [](#any-solution-gives-contradiction){.pf-ref}.
:::

:::

::: pf-qed
Step [](#no-solution){.pf-ref}.
:::

:::

:::
