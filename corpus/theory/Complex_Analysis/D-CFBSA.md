---
schema: qual/card@1
id: D-CFBSA
kind: definition
title: Laplacian and harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - PDEs
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\RR^2$ be open and let $u\colon\Omega\to\RR$ be a $C^2$ function of $(x,y)$.
The \dfn{Laplacian} of $u$ is
$$
\Delta u\coloneqq\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2},
$$
and $u$ is \dfn{harmonic} on $\Omega$ if $\Delta u=0$ on $\Omega$.

This is [@Ahl73, ch. 4, §6.1, Definition and Basic Properties], which calls a real-valued function harmonic when it is continuous with its first two partial derivatives and satisfies Laplace's equation (51) there; the $C^2$ hypothesis above is the same regularity, the book noting that it can be weakened.
:::
