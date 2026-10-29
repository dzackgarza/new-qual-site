---
schema: qual/card@1
id: E-VI5ZS
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source states the identity without hypotheses; the statement adds that f and g are holomorphic where fg is nonzero.
---

::: {.exercise}
Let $f$ and $g$ be holomorphic on a region where $fg\neq0$. Show that $\del_{\log}(fg) = \del_{\log} f + \del_{\log} g$, i.e. 
$$
{ (fg)' \over fg} = {f'\over f} + {g' \over g}.
$$
:::

::: {.solution}
::: pf

::: {.pf-step #product-rule}
$(fg)' = f'g + fg'$.

::: pf-proof
This is the product rule.
:::

:::

::: pf-step
$\frac{(fg)'}{fg} = \frac{f'}{f} + \frac{g'}{g}$ wherever $fg\neq0$.

::: pf-proof
Divide step [](#product-rule){.pf-ref} by $fg$: $\frac{f'g + fg'}{fg} = \frac{f'}{f} + \frac{g'}{g}$.
:::

:::

:::

:::
