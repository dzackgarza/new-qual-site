---
schema: qual/card@1
id: P-KGHOG
kind: problem
title: The Fourier transform of a compactly supported continuous function is entire
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - integrals
  - holomorphic-functions
relations: []
review: draft
solved: false
---

::: problem
Suppose that $f: \RR\to\RR$ is a continuous function that vanishes outside of some finite interval.
For each $z\in \CC$, define
\[
g(z) = \int_{-\infty}^\infty f(t) e^{-izt} \,dt
.\]

Show that $g$ is entire.
:::
