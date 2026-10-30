---
schema: qual/card@1
id: P-MOL6S
kind: problem
title: $n$th derivative of $xe^{2x}$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f:\RR\to\RR$ be defined by $f(x)=xe^{2x}$. Find a general formula for the $n$th derivative $f^{(n)}(x)$, and prove it by induction.
:::

::: {.solution}

::: pf

::: {.pf-step #base}

The formula $f^{(n)}(x) = (2^n x + n2^{n-1})e^{2x}$ holds for $n = 0$.

::: pf-proof

For $n = 0$ the right side is $(x + 0)e^{2x} = f(x)$.

:::

:::

::: {.pf-step #induct}

If $f^{(k)}(x) = (2^k x + k2^{k-1})e^{2x}$ for some $k \ge 0$, then $f^{(k+1)}(x) = (2^{k+1} x + (k+1)2^{k})e^{2x}$.

::: pf-proof

By the product rule,
$$
f^{(k+1)}(x) = 2^k e^{2x} + 2(2^k x + k2^{k-1})e^{2x} = \bigl(2^{k+1}x + (k+1)2^k\bigr)e^{2x}.
$$

:::

:::

::: pf-step

For every integer $n \ge 0$,
$$
\boxed{f^{(n)}(x) = (2^n x + n2^{n-1})e^{2x} = 2^{n-1}(2x + n)e^{2x}.}
$$

::: pf-proof

By induction on $n$, from steps [](#base){.pf-ref} and [](#induct){.pf-ref}.

:::

:::

:::

:::
