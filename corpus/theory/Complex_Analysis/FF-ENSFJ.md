---
schema: qual/card@1
id: FF-ENSFJ
kind: fact
title: Taylor series of $\sech z$ at $0$
prompts:
- What is the series expansion of $\sech(z)$?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
  - Power Series
relations: []
review: draft
---

::: {.fact}
For $z\in\CC$ with $\abs{z}<\pi/2$,
$$
\sech z = \frac{1}{\cosh z} = 1-\frac{z^{2}}{2}+\frac{5 z^{4}}{24}-\frac{61 z^{6}}{720}+\cdots.
$$
The radius of convergence is $\pi/2$, the distance from $0$ to the nearest zeros $\pm i\pi/2$ of $\cosh$.
:::
