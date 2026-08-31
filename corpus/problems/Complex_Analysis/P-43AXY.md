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

::: problem
Prove that the following polynomial has its roots outside of the unit circle:
\[
p(z) = z^3 + 2z + 4
.\]

> Hint: What is the maximum value of the modulus of the first two terms if $\abs{z} \leq 1$?
:::

::: {.solution}
**Goal:** Prove that all roots of $p(z) = z^3 + 2z + 4$ lie outside the unit circle.

<1>1. On $\abs{z} = 1$, the modulus of the first two terms is at most $3$.
    ::: {.proof}
    $\abs{z^3 + 2z} \leq \abs{z}^3 + 2\abs{z} = 1 + 2 = 3$ by the triangle inequality.
    :::

<1>2. On $\abs{z} = 1$, $\abs{z^3 + 2z} < \abs{4}$.
    ::: {.proof}
    By <1>1, $\abs{z^3 + 2z} \leq 3 < 4 = \abs{4}$.
    :::

<1>3. $p(z) = z^3 + 2z + 4$ has the same number of zeros in $\abs{z} < 1$ as the constant $4$.
    ::: {.proof}
    Apply Rouch\'e's theorem to $f(z) = 4$ and $g(z) = z^3 + 2z$ on the circle $\abs{z} = 1$; the strict inequality $\abs{g(z)} < \abs{f(z)}$ from <1>2 holds on the whole circle, so $f$ and $f + g = p$ have equally many zeros inside.
    :::

<1>4. $p$ has no zeros in $\abs{z} < 1$ and none on $\abs{z} = 1$.
    ::: {.proof}
    The constant $4$ has no zeros, so by <1>3 neither does $p$ inside the circle; and <1>2 rules out zeros on the circle itself (there $\abs{p(z)} \geq \abs{4} - \abs{z^3 + 2z} \geq 4 - 3 = 1 > 0$).
    :::

<1>5. Q.E.D.
    ::: {.proof}
    <1>4 shows every root of $p$ satisfies $\abs{z} > 1$, i.e. lies strictly outside the unit circle.
    :::

:::
