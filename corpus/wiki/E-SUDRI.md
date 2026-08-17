---
schema: qual/card@1
id: E-SUDRI
kind: exercise
title: "Show that if $f$ is entire and $f(z) \\convergesto{z\\to\\infty} \\infty$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - singularities
  - casorati-weierstrass
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Show that if $f$ is entire and $f(z) \convergesto{z\to\infty} \infty$ then $f$ is a polynomial.
:::

::: {.solution}
\envlist

- Set $g(z) \da f(1/z)$, so $g(z) \convergesto{z\to 0} \infty$ making $z=0$ a singularity.

- This is not an essential singularity by Casorati-Weierstrass.

- So this is a pole and $g(z) = \sum_{-N\leq k \leq 0} c_k z^k$ for $N$ the order of the pole

- Thus $f(z) = \sum_{0<k<N}c_k z^k$ is a polynomial.
:::
