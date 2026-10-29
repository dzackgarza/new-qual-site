---
schema: qual/card@1
id: E-WNNSK
kind: problem
title: Real part of $\frac{z+2}{z-1}$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.exercise}
Find $\Re\qty{z+2\over z-1}$.

:::

::: {.solution}
Write $z = x+iy$ with $z\neq1$.

::: pf

::: {.pf-step #conj}
$\frac{z+2}{z-1} = 1 + \frac{3(\bar z - 1)}{\abs{z-1}^2}$.

::: pf-proof
$\frac{z+2}{z-1} = 1 + \frac{3}{z-1}$, and $\frac{1}{z-1} = \frac{\overline{z-1}}{\abs{z-1}^2}$.
:::

:::

::: pf-step
$$
\Re\qty{z+2\over z-1} = \boxed{\frac{(x-1)(x+2) + y^2}{(x-1)^2 + y^2}}.
$$

::: pf-proof
By step [](#conj){.pf-ref} the real part is $1 + \frac{3(x-1)}{(x-1)^2+y^2} = \frac{(x-1)^2 + 3(x-1) + y^2}{(x-1)^2+y^2}$, and $(x-1)^2+3(x-1) = (x-1)(x+2)$.
:::

:::

:::

:::
