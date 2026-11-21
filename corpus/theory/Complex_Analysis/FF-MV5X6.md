---
schema: qual/card@1
id: FF-MV5X6
kind: fact
title: $\sin z = \frac{1}{i}\sinh(iz)$
slogan: 'Circular and hyperbolic sine differ by the imaginary change of variable: $\sin z=\sinh(iz)/i$.'
prompts:
- How is $\sin(z)$ written in terms of $\sinh$?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
  - Trigonometry
relations: []
review: draft
---

::: {.fact}
For every $z\in\CC$,
$$
\sin(z) = {1\over i} \sinh(iz).
$$

This is the other expression asked for in [@Ahl73, ch. 2, §3.2, The Trigonometric Functions]: with $\sinh w=(e^{w}-e^{-w})/2$ and $w=iz$, the right side is $\frac1i\cdot\frac{e^{iz}-e^{-iz}}{2}=\sin z$.
:::
