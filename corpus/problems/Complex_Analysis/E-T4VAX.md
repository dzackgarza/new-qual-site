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
Write $h = f + g$ with $f(z) = z^5$ and $g(z) = 3z + 1$.

::: pf

::: {.pf-step #g-lt-f-on-circle}
On $\abs{z} = 2$: $\abs{g(z)} < \abs{f(z)}$.

::: pf-proof
$\abs{g(z)} \le 3\abs{z} + 1 = 7$ on $\abs{z} = 2$, while $\abs{f(z)} = \abs{z}^5 = 32$.
:::

:::

::: {.pf-step #same-zero-count}
$h$ and $f$ have the same number of zeros in $\abs{z} < 2$, counted with multiplicity.

::: pf-proof
Rouché's theorem on the circle $\abs{z}=2$, using step [](#g-lt-f-on-circle){.pf-ref}.
:::

:::

::: {.pf-step #f-five-zeros}
$f(z) = z^5$ has exactly 5 zeros in $\abs{z} < 2$, counted with multiplicity.

::: pf-proof
The only zero is $z = 0$, with multiplicity 5.
:::

:::

::: {.pf-step #none-on-circle}
$h$ has no zeros on $\abs{z}=2$.

::: pf-proof
There $\abs{h}\geq\abs{f}-\abs{g}>0$ by step [](#g-lt-f-on-circle){.pf-ref}.
:::

:::

::: pf-qed
By steps [](#same-zero-count){.pf-ref} and [](#f-five-zeros){.pf-ref}, $h$ has exactly $5$ zeros in $\abs{z} < 2$, and by step [](#none-on-circle){.pf-ref} these are all its zeros in $\abs{z} \le 2$.
:::

:::

:::
