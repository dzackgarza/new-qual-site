---
schema: qual/card@1
id: E-T4VAX
kind: problem
title: $z^5+3z+1$ has five zeros in $|z|\leq 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that $h(z) =z^5 + 3z + 1$ has 5 zeros in $\abs z \leq 2$.
:::

::: {.solution}
**Goal:** Show that $h(z) = z^5 + 3z + 1$ has exactly 5 zeros in $\abs{z} \le 2$.

::: pf

::: pf-step
Setup: write $h = f + g$ with $f(z) = z^5$ and $g(z) = 3z + 1$.

::: pf-proof
$h(z) = z^5 + 3z + 1$.
:::

:::

::: {.pf-step #g-lt-f-on-circle}
On $\abs{z} = 2$: $\abs{g(z)} < \abs{f(z)}$.

::: pf-proof
$\abs{g(z)} \le 3\abs{z} + 1 = 7$ on $\abs{z} = 2$, while $\abs{f(z)} = \abs{z}^5 = 32$.
Since $7 < 32$, the strict inequality holds everywhere on the circle.
:::

:::

::: {.pf-step #same-zero-count}
$h$ and $f$ have the same number of zeros inside $\abs{z} < 2$.

::: pf-proof
Rouch\'e's theorem with $f(z) = z^5$, $g(z) = 3z+1$, $\gamma = \abs{z}=2$, using step [](#g-lt-f-on-circle){.pf-ref}.
:::

:::

::: {.pf-step #f-five-zeros}
$f(z) = z^5$ has exactly 5 zeros in $\abs{z} < 2$ (counting multiplicity).

::: pf-proof
The only zero is $z = 0$ with multiplicity 5, and $0$ lies in the disk.
:::

:::

::: pf-qed
Steps [](#same-zero-count){.pf-ref} and [](#f-five-zeros){.pf-ref} give that $h$ has exactly $5$ zeros in $\abs{z} < 2$, hence in $\abs{z} \le 2$.
:::

:::

:::
