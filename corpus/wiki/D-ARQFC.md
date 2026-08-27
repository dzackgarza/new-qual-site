---
schema: qual/card@1
id: D-ARQFC
kind: definition
title: Approximations to the identity
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
relations: []
review: draft
---

::: {.definition}
For $\phi\in L^1$, the dilations satisfy $\int \phi_{t} = \int \phi$, and if $\int \phi = 1$ then $\phi$ is an **approximate identity**.

Some properties that approximate identities enjoy:

- $\int \phi_t = \norm{\phi_t}_1 = 1$ for every $t$.

- $\sup_t \norm{\phi_t}_1 < \infty$

- For every $h>0$, $\lim_{t\to\infty} \int_{\abs x \geq h} \abs{\phi_t(x)}\dx = 0$.
:::
