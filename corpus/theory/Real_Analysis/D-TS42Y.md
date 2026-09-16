---
schema: qual/card@1
id: D-TS42Y
kind: definition
title: Convolution of functions on $\RR^n$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
relations: []
review: draft
---

::: {.definition}
Let $f,g\colon\RR^n\to\CC$ be measurable.
The \dfn{convolution} of $f$ and $g$ is the function
$$
(f * g)(x) \coloneqq \int_{\RR^n} f(x-y)\, g(y) \, dy,
$$
defined at every $x\in\RR^n$ for which the integral converges absolutely.
:::
