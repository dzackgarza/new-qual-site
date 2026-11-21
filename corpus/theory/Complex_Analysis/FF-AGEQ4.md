---
schema: qual/card@1
id: FF-AGEQ4
kind: fact
title: $\cos z = \cosh(iz)$
slogan: 'Circular cosine is hyperbolic cosine on the imaginary axis: $\cos z=\cosh(iz)$.'
prompts:
- How is $\cos(z)$ written in terms of $\cosh$?
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
\cos(z) = \cosh(iz).
$$

This is one of the two expressions asked for in [@Ahl73, ch. 2, §3.2, The Trigonometric Functions], where $\cosh w=(e^{w}+e^{-w})/2$ is defined: substituting $w=iz$ and using $\cos z=(e^{iz}+e^{-iz})/2$ gives the identity.
:::
