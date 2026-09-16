---
schema: qual/card@1
id: FD-QFRSI
kind: definition
title: Field of rational functions $K(x)$
prompts:
- What are the elements of the field of rational functions $K(x)$?
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Polynomials
relations:
- kind: variant-of
  target: FD-24RNF
review: draft
---

::: {.definition}
Let $K$ be a [[D-UI6CU|field]].
The \dfn{field of rational functions} in the variable $x$ over $K$ is the field of fractions of the polynomial ring $K[x]$:
$$
K(x)\coloneqq\theset{\frac{P(x)}{Q(x)} \st P,Q \in K[x],\ Q\neq 0}.
$$
:::

::: {.example}
$\CC(x)$ is the field of meromorphic functions on the Riemann sphere $\hat\CC=\CC\cup\theset{\infty}$.
Every rational function is meromorphic on $\hat\CC$.
Conversely, a meromorphic function $h$ on the compact surface $\hat\CC$ has finitely many poles; subtracting from $h$ its principal parts at the poles in $\CC$, which are rational functions, and the polynomial principal part at $\infty$ leaves a holomorphic function on $\hat\CC$, which is constant by Liouville's theorem, so $h\in\CC(x)$.
:::
