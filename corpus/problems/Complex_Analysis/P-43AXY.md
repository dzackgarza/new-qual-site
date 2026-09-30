---
schema: qual/card@1
id: P-43AXY
kind: problem
title: Roots of $z^3+2z+4$ lie outside the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomials
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove that the following polynomial has its roots outside of the unit circle:
\[
p(z) = z^3 + 2z + 4
.\]

> Hint: What is the maximum value of the modulus of the first two terms if $\abs{z} \leq 1$?
:::

::: {.solution}
**Goal:** Prove that all roots of $p(z) = z^3 + 2z + 4$ lie outside the unit circle.

::: pf

::: {.pf-step #bound-first-two-terms}
On $\abs{z} = 1$, the modulus of the first two terms is at most $3$.

::: pf-proof
$\abs{z^3 + 2z} \leq \abs{z}^3 + 2\abs{z} = 1 + 2 = 3$ by the triangle inequality.
:::

:::

::: {.pf-step #strict-inequality}
On $\abs{z} = 1$, $\abs{z^3 + 2z} < \abs{4}$.

::: pf-proof
By step [](#bound-first-two-terms){.pf-ref}, $\abs{z^3 + 2z} \leq 3 < 4 = \abs{4}$.
:::

:::

::: {.pf-step #same-zero-count}
$p(z) = z^3 + 2z + 4$ has the same number of zeros in $\abs{z} < 1$ as the constant $4$.

::: pf-proof
Apply Rouch\'e's theorem to $f(z) = 4$ and $g(z) = z^3 + 2z$ on the circle $\abs{z} = 1$; the strict inequality $\abs{g(z)} < \abs{f(z)}$ from step [](#strict-inequality){.pf-ref} holds on the whole circle, so $f$ and $f + g = p$ have equally many zeros inside.
:::

:::

::: {.pf-step #no-zeros-in-disk}
$p$ has no zeros in $\abs{z} < 1$ and none on $\abs{z} = 1$.

::: pf-proof
The constant $4$ has no zeros, so by step [](#same-zero-count){.pf-ref} neither does $p$ inside the circle; and step [](#strict-inequality){.pf-ref} rules out zeros on the circle itself (there $\abs{p(z)} \geq \abs{4} - \abs{z^3 + 2z} \geq 4 - 3 = 1 > 0$).
:::

:::

::: pf-qed
Step [](#no-zeros-in-disk){.pf-ref} shows every root of $p$ satisfies $\abs{z} > 1$, i.e. lies strictly outside the unit circle.
:::

:::

:::
