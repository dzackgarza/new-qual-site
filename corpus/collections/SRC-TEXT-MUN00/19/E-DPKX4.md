---
schema: qual/card@1
id: E-DPKX4
kind: exercise
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
<1>1. Define $h : (X_1 \times \cdots \times X_{n-1}) \times X_n \to X_1 \times \cdots \times X_n$ by
$$h((x_1, \ldots, x_{n-1}), x_n) = (x_1, \ldots, x_{n-1}, x_n).$$
Proof: definition.

<1>2. $h$ is a bijection.
Proof: the inverse is $h^{-1}(x_1, \ldots, x_n) = ((x_1, \ldots, x_{n-1}), x_n)$.

<1>3. $h$ is continuous.
Proof: a map into a product is continuous iff each coordinate is continuous; the coordinates of $h$ are the projections, which are continuous.

<1>4. $h^{-1}$ is continuous.
Proof: similarly, the coordinates of $h^{-1}$ are projections (and the tuple of the first $n-1$ projections), all continuous.

<1>5. Hence $h$ is a homeomorphism.
Proof: <1>2–<1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
