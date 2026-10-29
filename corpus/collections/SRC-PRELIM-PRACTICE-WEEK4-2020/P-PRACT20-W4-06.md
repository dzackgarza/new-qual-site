---
schema: qual/card@1
id: P-PRACT20-W4-06
kind: problem
title: General solution of $y'''-3y''+3y'-y=0$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
Find the general solution of $y ^ { \prime \prime \prime } - 3 y ^ { \prime \prime } + 3 y ^ { \prime } - y = 0$
:::

::: {.solution}
Write $D$ for the differentiation operator $d/dx$.

::: pf

::: {.pf-step #factor}
The equation is $(D-1)^3y=0$.

::: pf-proof
$(D-1)^3 = D^3-3D^2+3D-1$, and the coefficients are constant, so the factors commute.
:::

:::

::: {.pf-step #conjugate}
For every three-times differentiable $u$, $(D-1)^3(e^xu) = e^xu'''$.

::: pf-proof
By the product rule, $(D-1)(e^xu) = e^xu + e^xu' - e^xu = e^xu'$.
Applying this three times gives $(D-1)^3(e^xu) = e^xu'''$.
:::

:::

::: pf-step
The general solution is $\boxed{y(x) = (C_0 + C_1x + C_2x^2)e^x}$ with constants $C_0, C_1, C_2$.

::: pf-proof
Every function $y$ can be written $y = e^xu$ with $u = e^{-x}y$.
By steps [](#factor){.pf-ref} and [](#conjugate){.pf-ref}, $y$ is a solution exactly when $e^xu'''=0$, that is, when $u'''=0$.
Integrating three times, $u'''=0$ exactly when $u = C_0 + C_1x + C_2x^2$.
:::

:::

:::

:::
