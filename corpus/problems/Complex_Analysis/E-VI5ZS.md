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
---

::: {.exercise}
Show that $\del_{\log}(fg) = \del_{\log} f + \del_{\log} g$, i.e. 
\[
{ (fg)' \over fg} = {f'\over f} + {g' \over g}
.\]
:::

::: {.solution}
**Goal:** Show that $\del_{\log}(fg) = \del_{\log} f + \del_{\log} g$, i.e. $(fg)'/(fg) = f'/f + g'/g$, wherever $f, g$ are nonzero holomorphic functions.

::: pf

::: {.pf-step #product-rule}
Differentiate $fg$ by the product rule.

::: pf-proof
$(fg)' = f'g + fg'$.
:::

:::

::: {.pf-step #divide-by-fg}
Divide both sides by $fg \neq 0$.

::: pf-proof
$\frac{(fg)'}{fg} = \frac{f'g + fg'}{fg} = \frac{f'g}{fg} + \frac{fg'}{fg} = \frac{f'}{f} + \frac{g'}{g}$.
:::

:::

::: pf-qed
Steps [](#product-rule){.pf-ref} and [](#divide-by-fg){.pf-ref} establish the identity, valid on any region where $f, g$ are holomorphic and $fg \neq 0$.
:::

:::
