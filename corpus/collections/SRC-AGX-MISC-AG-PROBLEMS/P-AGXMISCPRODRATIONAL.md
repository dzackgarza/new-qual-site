---
schema: qual/card@1
id: P-AGXMISCPRODRATIONAL
kind: problem
title: $\PP^n\cross \PP^m$ is a rational variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Varieties
  - Birational Maps
  - Projective Space
relations: []
review: draft
---

::: {.problem}
Show that $\PP^n\cross \PP^m$ is rational.
:::

::: {.solution}
Let $U \subseteq \PP^n \cross \PP^m$ be the dense open set $x_0 y_0 \neq 0$, and let $V \subseteq \PP^{n+m}$ be the dense open set $z_0 \neq 0$.

::: pf

::: {.pf-step #phi}
The map $\phi\colon U \to V$,
$$
[x_0: \ldots: x_n] \cross [y_0: \ldots: y_m] \mapsto \left[1: \frac{x_1}{x_0}: \ldots: \frac{x_n}{x_0}: \frac{y_1}{y_0}: \ldots: \frac{y_m}{y_0}\right],
$$
is a morphism.

::: pf-proof
Its coordinates are regular functions on $U$, and they do not depend on the choice of homogeneous coordinates.
:::

:::

::: {.pf-step #psi}
The map $\psi\colon V \to U$,
$$
[1: z_1: \ldots: z_{n+m}] \mapsto [1: z_1: \ldots: z_n] \cross [1: z_{n+1}: \ldots: z_{n+m}],
$$
is a morphism, and $\phi$ and $\psi$ are inverse to each other.

::: pf-proof
The coordinates $z_i / z_0$ are regular on $V$, and the image has $x_0 = y_0 = 1$, so it lies in $U$.
Both composites are the identity, by direct substitution.
:::

:::

::: pf-step
$\PP^n \cross \PP^m$ is rational.

::: pf-proof
By steps [](#phi){.pf-ref} and [](#psi){.pf-ref}, the dense opens $U$ and $V$ are isomorphic.
So $\PP^n \cross \PP^m$ is birational to $\PP^{n+m}$, which is rational.
:::

:::

:::
:::
