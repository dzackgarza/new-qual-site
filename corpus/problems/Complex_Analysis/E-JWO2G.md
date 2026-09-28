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
Write $z=x+iy$, so $\Re(z) = x$.
Then
\[
\abs{e^z} = \abs{e^{x+iy}} = \abs{e^x}\abs{e^{iy}} = e^x
,\]
using that $\abs{e^{iy}}=\abs{\cos y+i\sin y}=1$ and $e^x>0$ for all $x\in \RR$.
:::
