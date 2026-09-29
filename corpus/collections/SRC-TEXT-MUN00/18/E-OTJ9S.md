---
schema: qual/card@1
id: E-OTJ9S
kind: problem
title: Coordinate slices are imbeddings
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Given $x_0 \in X$ and $y_0 \in Y$, show that the maps $f: X \to X \times Y$ and $g: Y \to X \times Y$ defined by

$$
f(x) = x \times y_0 \quad \text{and} \quad g(y) = x_0 \times y
$$

are imbeddings.
:::

::: {.solution}
An imbedding is a map that is a homeomorphism onto its image.

::: pf

::: {.pf-step #f-continuous-injective}
$f$ is continuous and injective.

::: pf-proof
Its coordinates are $\pi_1\circ f=\operatorname{id}_X$ and the constant map $\pi_2\circ f\equiv y_0$, both continuous, and a map into a product is continuous if and only if its coordinates are.
If $f(x_1)=f(x_2)$, then $(x_1,y_0)=(x_2,y_0)$, so $x_1=x_2$.
:::

:::

::: {.pf-step #f-homeomorphism-onto-image}
$f$ is a homeomorphism onto $X\times\{y_0\}$.

::: pf-proof
The inverse of $f\colon X\to X\times\{y_0\}$ is the restriction of $\pi_1$ to $X\times\{y_0\}$, which is continuous.
:::

:::

::: {.pf-step #g-imbedding}
$g$ is an imbedding.

::: pf-proof
Exchange the roles of the factors in steps [](#f-continuous-injective){.pf-ref} and [](#f-homeomorphism-onto-image){.pf-ref}: $g$ has coordinates the constant map at $x_0$ and $\operatorname{id}_Y$, and its inverse on $\{x_0\}\times Y$ is the restriction of $\pi_2$.
:::

:::

::: pf-qed
Steps [](#f-continuous-injective){.pf-ref} and [](#f-homeomorphism-onto-image){.pf-ref} show that $f$ is an imbedding, and step [](#g-imbedding){.pf-ref} treats $g$.
:::

:::

:::
