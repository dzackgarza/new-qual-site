---
schema: qual/card@1
id: E-XOCPO
kind: problem
title: Laurent expanding exponentials
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion that converges for $\abs{z} > 1$ of
\[
f(z) \definedas {1 \over e^{1-z}}
.\]

:::

::: {.solution}
\[
f(z) = e^{-(1-z)} = e^{z-1} = \inverseof{e} e^z = \inverseof{e}\sum_{k\geq 0} {z^k\over k!}
.\]
Since $e^z$ is entire, this converges on $\CC$.
:::
