---
schema: qual/card@1
id: D-B2JER
kind: definition
title: Cup product
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $R$ a ring, and $p, q\geq 0$.
For singular cochains $\varphi\in C^p(X;R)$ and $\psi\in C^q(X;R)$, the \dfn{cup product} $\varphi\smile\psi\in C^{p+q}(X;R)$ is the cochain whose value on a singular $(p+q)$-simplex $\sigma\colon[v_0, \ldots, v_{p+q}]\to X$ is
$$
(\varphi\smile\psi)(\sigma) \coloneqq \varphi\qty{\ro{\sigma}{[v_0, \ldots, v_p]}}\,\psi\qty{\ro{\sigma}{[v_p, \ldots, v_{p+q}]}}
,$$
where each face is identified with the standard simplex of its dimension by the order-preserving linear homeomorphism.
:::

::: {.remark}
The coboundary satisfies $\delta(\varphi\smile\psi) = \delta\varphi\smile\psi + (-1)^p\varphi\smile\delta\psi$, so the cup product of two cocycles is a cocycle and the cup product of a cocycle with a coboundary is a coboundary.
Hence it induces a bilinear map
$$
\smile\colon H^p(X;R)\cross H^q(X;R)\to H^{p+q}(X;R), \qquad [\varphi]\smile[\psi]\coloneqq[\varphi\smile\psi]
.$$
:::

::: {.concept}
[@Hat02, §3.2, p. 206].
:::
