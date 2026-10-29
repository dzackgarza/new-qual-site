---
schema: qual/card@1
id: E-PWVJS
kind: problem
title: 'The logarithmic derivative of a product: $\frac{(fg)''}{fg}=\frac{f''}{f}+\frac{g''}{g}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Poles
  - Zeros
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source states the identity without saying where it holds; the statement adds that f and g are holomorphic and nonvanishing on an open set.
---

::: {.exercise}
Let $f$ and $g$ be holomorphic and nonvanishing on an open set $\Omega$.
Show that $\logd(fg) = \logd f + \logd g$ on $\Omega$, i.e.
$$
{ (fg)' \over fg} = {f'\over f} + {g' \over g}.
$$
:::

::: {.solution}

::: pf

::: pf-step
$\displaystyle\frac{(fg)'}{fg} = \frac{f'}{f}+\frac{g'}{g}$ on $\Omega$.

::: pf-proof
$fg$ does not vanish on $\Omega$, and by the product rule
$$
\frac{(fg)'}{fg} = \frac{f'g + fg'}{fg} = \frac{f'}{f} + \frac{g'}{g}.
$$
:::

:::

:::

:::
