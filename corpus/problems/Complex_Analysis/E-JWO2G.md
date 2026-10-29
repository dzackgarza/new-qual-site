---
schema: qual/card@1
id: E-JWO2G
kind: problem
title: $\abs{e^z}=e^{\Re z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Show that $\abs{e^z} = e^{\Re(z)}$.

:::

::: {.solution}
Write $z=x+iy$ with $x,y\in\RR$, so $\Re(z) = x$.

::: pf

::: {.pf-step #factors}
$\abs{e^{iy}}=1$ and $\abs{e^x}=e^x$.

::: pf-proof
$\abs{e^{iy}}^2=\cos^2y+\sin^2y=1$, and $e^x>0$ for real $x$.
:::

:::

::: pf-step
$\abs{e^z}=e^{\Re(z)}$.

::: pf-proof
Since $e^{z+w}=e^ze^w$, step [](#factors){.pf-ref} gives $\abs{e^z}=\abs{e^x}\abs{e^{iy}}=e^x$.
:::

:::

:::

:::
