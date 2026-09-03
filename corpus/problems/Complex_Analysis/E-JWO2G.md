---
schema: qual/card@1
id: E-JWO2G
kind: problem
title: Modulus of $e^z$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Entire Functions
relations: []
review: draft
---

:::{.exercise}
Show that $\abs{e^z} = e^{\Re(z)}$.

:::

:::{.solution}
Write $z=x+iy$, so $\Re(z) = x$.
Then
\[
\abs{e^z} = \abs{e^{x+iy}} = \abs{e^x}\abs{e^{iy}} = \abs{e^x}
,\]
using that $e^x>0$ for all $x\in \RR$.
:::
