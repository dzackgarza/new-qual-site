---
schema: qual/card@1
id: E-DPKX4
kind: problem
title: Associativity of finite products
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Show that $(X_1 \times \cdots \times X_{n-1}) \times X_n$ is homeomorphic with $X_1 \times \cdots \times X_n$.
:::

::: {.solution}
Write $P=X_1\times\cdots\times X_{n-1}$ with projections $p_i\colon P\to X_i$, let $q_1\colon P\times X_n\to P$ and $q_2\colon P\times X_n\to X_n$ be the projections, and let $\pi_i\colon X_1\times\cdots\times X_n\to X_i$ be the projections.
Define
$$
h\colon P\times X_n\to X_1\times\cdots\times X_n,\qquad h((x_1,\ldots,x_{n-1}),x_n)=(x_1,\ldots,x_n).
$$

<1>1. $h$ is a continuous bijection.

::: {.proof}
It has inverse $k(x_1,\ldots,x_n)=((x_1,\ldots,x_{n-1}),x_n)$.
Its coordinates are $\pi_i\circ h=p_i\circ q_1$ for $i<n$ and $\pi_n\circ h=q_2$, composites of continuous projections; a map into a product is continuous if and only if its coordinates are.
:::

<1>2. $k=h^{-1}$ is continuous.

::: {.proof}
Its coordinates are $q_1\circ k=(\pi_1,\ldots,\pi_{n-1})\colon X_1\times\cdots\times X_n\to P$, continuous because its coordinates $\pi_i$ are, and $q_2\circ k=\pi_n$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $h$ is a homeomorphism.
:::
:::
