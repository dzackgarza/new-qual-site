---
schema: qual/card@1
id: E-ZDVLE
kind: problem
title: Entire functions with nonnegative real part are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source did not say f is entire, and f(z) = |z|^2 is a nonconstant function with nonnegative real part; the statement now takes f entire.'
---

::: {.exercise}
Let $f$ be entire. Show that if $\Re(f(z)) \geq 0$ for all $z\in \CC$, then $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #bounded}
$g\coloneqq e^{-f}$ is entire with $\abs g\le1$.

::: pf-proof
$\abs{g(z)} = e^{-\Re f(z)}\le e^0 = 1$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#bounded){.pf-ref} and Liouville's theorem, $g$ is constant, so $0 = g' = -f'e^{-f}$.
Since $e^{-f}$ never vanishes, $f'\equiv0$, and $f$ is constant on the connected set $\CC$.
:::

:::

:::

:::
