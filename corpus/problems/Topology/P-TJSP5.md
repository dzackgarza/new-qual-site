---
schema: qual/card@1
id: P-TJSP5
kind: problem
title: $\chi(\Sigma_g+\Sigma_h)=\chi(\Sigma_g)+\chi(\Sigma_h)-2$
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Surfaces
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source writes only 'Show that chi(Sigma_g + Sigma_h) = chi(Sigma_g) + chi(Sigma_h) - 2'; the statement now defines Sigma_g and the sum as connected sum."
---

::: {.problem}
Let $\Sigma_g$ denote the closed orientable surface of genus $g$, and let $\Sigma_g + \Sigma_h$ denote the connected sum of $\Sigma_g$ and $\Sigma_h$.
Show that $\chi(\Sigma_g + \Sigma_h) = \chi(\Sigma_g) + \chi(\Sigma_h) - 2$.
:::

::: {.solution}

::: pf

::: pf-step

For closed orientable surfaces, $\chi(\Sigma_g)=2-2g$.

::: pf-proof

The standard CW structure on $\Sigma_g$ has one $0$-cell, $2g$ $1$-cells, and one $2$-cell, so $\chi(\Sigma_g) = 1 - 2g + 1$.

:::

:::

::: pf-step

The connected sum satisfies $\Sigma_g+\Sigma_h\cong\Sigma_{g+h}$.

::: pf-proof

By the classification of surfaces, the connected sum of orientable surfaces is orientable and its genus is the sum of the genera.

:::

:::

::: pf-step

Hence
$$\boxed{\chi(\Sigma_g+\Sigma_h)=\chi(\Sigma_g)+\chi(\Sigma_h)-2.}$$

::: pf-proof

The left side is $2-2(g+h)$, while the right side is $(2-2g)+(2-2h)-2=2-2g-2h$.

:::

:::

:::

:::
