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
---

::: {.problem}
- Show that $\chi(\Sigma_g + \Sigma_h) = \chi(\Sigma_g)  + \chi(\Sigma_h) - 2$.
:::

::: {.solution}
<1>1. For closed orientable surfaces, $\chi(\Sigma_g)=2-2g$.
::: {.proof}
Use the standard CW structure with one $0$-cell, $2g$ $1$-cells, and one $2$-cell.
:::

<1>2. The connected sum satisfies $\Sigma_g\#\Sigma_h\cong\Sigma_{g+h}$.
::: {.proof}
Connected sum adds the numbers of handles.
:::

<1>3. Hence
$$\boxed{\chi(\Sigma_g\#\Sigma_h)=\chi(\Sigma_g)+\chi(\Sigma_h)-2.}$$
::: {.proof}
The left side is $2-2(g+h)$, while the right side is $(2-2g)+(2-2h)-2=2-2g-2h$.
:::
:::
