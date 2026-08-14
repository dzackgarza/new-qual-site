---
schema: qual/card@1
id: E-XOCPO
kind: exercise
title: "Laurent expanding exponentials"
classification:
  areas:
  - complex-analysis
  topics:
  - laurent-series
  - power-series
  - entire-functions
relations: []
review: draft
---
:::{.exercise title="Laurent expanding exponentials"}
Find a Laurent expansion that converges for $\abs{z} > 1$ of
\[
f(z) \da {1 \over e^{1-z}}
.\]

:::

:::{.solution}
\[
f(z) = e^{-(1-z)} = e^{z-1} = e\inv e^z = e\inv\sum_{k\geq 0} {z^k\over k!}
.\]
Since $e^z$ is entire, this converges on $\CC$.
:::

