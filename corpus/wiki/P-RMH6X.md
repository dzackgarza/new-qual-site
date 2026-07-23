---
schema: qual/card@1
id: P-RMH6X
kind: problem
title: "Horizontal strip to $\\mathbb{H}$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="Horizontal strip to $\mathbb{H}$"}
Find a conformal map from the strip $\theset{z\in \CC \suchthat 0 < \Im(z) < 1}$ to $\HH$.
:::

:::{.solution}
In steps:

- Dilate by $z\mapsto \pi z$ to get $0<\Im(z) < \pi$.
- Exponentiate by $z\mapsto e^z$ to get $\HH$.

Why $e^z$ works: apply $\Log$ to $\HH$, use polar coordinates to write $w=re^{i\theta}$ with $0<\theta<\pi$ and note
\[
\Log(w) = \ln\abs{w} +i\Arg(w) = \ln(r) + i\theta
,\]
and noting that the image of $\ln(\wait)$ is all of $\RR$.
:::

