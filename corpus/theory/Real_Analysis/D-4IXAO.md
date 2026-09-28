---
schema: qual/card@1
id: D-4IXAO
kind: definition
title: Orthonormal sequence
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Inner Product Spaces
relations: []
review: draft
---

::: {.definition}
Let $H$ be an inner product space with inner product $\inner{\cdot}{\cdot}$ and norm $\norm{u}\coloneqq\sqrt{\inner{u}{u}}$, and let $I$ be a countable index set.
A family $(u_i)_{i\in I}$ of elements of $H$ is \dfn{orthonormal} if

1. $\inner{u_i}{u_j} = 0$ for all $i,j\in I$ with $i \neq j$, and

2. $\norm{u_j} = 1$ for all $j\in I$.
:::
