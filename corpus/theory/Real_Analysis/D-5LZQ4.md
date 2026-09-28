---
schema: qual/card@1
id: D-5LZQ4
kind: definition
title: Fourier transform
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
---

::: {.definition}
For $f\in L^1(\RR^n)$, the \dfn{Fourier transform} of $f$ is the function $\widehat f\colon\RR^n\to\CC$ given by
$$
\widehat f(\xi) \coloneqq \int_{\RR^n} f(x)e^{-2\pi i x\cdot\xi}\,dx, \qquad \xi\in\RR^n.
$$
:::
