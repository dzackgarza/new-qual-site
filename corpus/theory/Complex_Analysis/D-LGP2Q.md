---
schema: qual/card@1
id: D-LGP2Q
kind: definition
title: The Weierstrass $\wp$ function
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $\omega_1,\omega_2\in\CC$ be linearly independent over $\RR$, and let $\Lambda\coloneqq\ZZ\omega_1+\ZZ\omega_2$.
The \dfn{Weierstrass $\wp$ function} of $\Lambda$ is
$$
\wp(z)\coloneqq\frac{1}{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\qty{\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}},\qquad z\in\CC\setminus\Lambda.
$$
:::

::: {.proposition}
The series defining $\wp$ converges absolutely and uniformly on compact subsets of $\CC\setminus\Lambda$, and $\wp$ is [[D-7DFVJ|meromorphic]] on $\CC$ with a [[D-AUD6K|pole of order $2$]] at each point of $\Lambda$ and no other poles.
:::
