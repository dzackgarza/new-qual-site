---
schema: qual/card@1
id: E-VI5ZS
kind: exercise
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
---

:::{.exercise}
Show that $\del_{\log}(fg) = \del_{\log} f + \del_{\log} g$, i.e. 
\[
{ (fg)' \over fg} = {f'\over f} + {g' \over g}
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that $\del_{\log}(fg) = \del_{\log} f + \del_{\log} g$, i.e. $(fg)'/(fg) = f'/f + g'/g$, wherever $f, g$ are nonzero holomorphic functions.

<1>1. Differentiate $fg$ by the product rule.
    Proof: $(fg)' = f'g + fg'$.

<1>2. Divide both sides by $fg \neq 0$.
    Proof: $\frac{(fg)'}{fg} = \frac{f'g + fg'}{fg} = \frac{f'g}{fg} + \frac{fg'}{fg} = \frac{f'}{f} + \frac{g'}{g}$.

<1>3. Q.E.D.
    Proof: <1>1 and <1>2 establish the identity, valid on any region where $f, g$ are holomorphic and $fg \neq 0$.

:::
