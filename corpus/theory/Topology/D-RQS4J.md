---
schema: qual/card@1
id: D-RQS4J
kind: definition
title: Cap product
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homology
  - Poincaré Duality
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $R$ a commutative ring, and $0\leq q\leq p$.
For a singular $p$-simplex $\sigma\colon\Delta^p=[v_0,\ldots,v_p]\to X$ and $0\leq i\leq j\leq p$, write $\sigma|_{[v_i,\ldots,v_j]}$ for the singular $(j-i)$-simplex obtained by restricting $\sigma$ to the face $[v_i,\ldots,v_j]$, identified with $\Delta^{j-i}$ preserving the order of the vertices.
The \dfn{cap product} on chains and cochains is the $R$-bilinear map
$$
\frown\colon C_p(X;R)\times C^q(X;R)\to C_{p-q}(X;R),\qquad \sigma\frown\psi\coloneqq\psi\qty{\sigma|_{[v_0,\ldots,v_q]}}\,\sigma|_{[v_q,\ldots,v_p]}
$$
on singular $p$-simplices $\sigma$ and [[D-R6LA3|singular $q$-cochains]] $\psi$, extended linearly in $\sigma$ [@Hat02, p. 239].
:::

::: {.proposition}
For $\sigma\in C_p(X;R)$ and $\psi\in C^q(X;R)$,
$$
\del(\sigma\frown\psi)=(-1)^q\qty{\del\sigma\frown\psi-\sigma\frown\delta\psi},
$$
so the cap product of a cycle and a cocycle is a cycle, and it induces an $R$-bilinear map
$$
\frown\colon H_p(X;R)\times H^q(X;R)\to H_{p-q}(X;R)
$$
[@Hat02, p. 239].
:::
