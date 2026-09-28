---
schema: qual/card@1
id: FF-5GLOZ
kind: fact
title: Laurent expansion of $\csch z$ at $0$
slogan: '$\csch z$ has principal part $1/z$ at $0$, followed by an odd regular Laurent tail.'
prompts:
- What is the series expansion of $\csch(z)$?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
  - Laurent Series
relations: []
review: draft
---

::: {.fact}
The function $\csch z\coloneqq\frac{1}{\sinh z}$ has a simple pole at $0$, and for $0<\abs{z}<\pi$
$$
\csch z=\frac1z-\frac{z}{6}+\frac{7z^{3}}{360}-\frac{31z^{5}}{15120}+\cdots.
$$
:::
