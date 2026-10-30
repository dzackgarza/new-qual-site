---
schema: qual/card@1
id: E-WNTXK
kind: problem
title: An entire function with values in $\HH$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is entire and $f(\CC) \subseteq \HH$.
Show that $f$ must be constant.
:::

::: {.solution}
Let $T(w)=\frac{w-i}{w+i}$, the Cayley map, which maps $\HH$ bijectively onto $\DD$.

::: pf

::: {.pf-step #bounded}
$F\coloneqq T\circ f$ is entire and bounded.

::: pf-proof
$f(\CC)\subseteq\HH$ avoids the pole $-i$ of $T$, so $F$ is entire, and $F(\CC)\subseteq\DD$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#bounded){.pf-ref} and Liouville's theorem, $F\equiv c$ for some $c\in\DD$, so $f = T^{-1}\circ F\equiv T^{-1}(c)$.
:::

:::

:::

:::
