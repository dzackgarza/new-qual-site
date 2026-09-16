---
schema: qual/card@1
id: FF-4WIMZ
kind: fact
title: Convolution $(f\ast g)(\xi) = \int f(\xi - y)g(y) \, dy$
prompts:
- How is the convolution $(f \ast g)(\xi)$ defined?
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
relations: []
review: draft
---

::: {.fact}
Let $f, g\colon\RR^n\to\CC$ be measurable.
At every $\xi\in\RR^n$ for which the integral converges absolutely, the [[D-TS42Y|convolution]] of $f$ and $g$ is
$$
(f\ast g)(\xi) = \int_{\RR^n} f(\xi - y)g(y) \, dy.
$$
:::
