---
schema: qual/card@1
id: E-69NKI
kind: problem
title: Homotopy of composites
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $h, h': X \to Y$ are homotopic and $k, k': Y \to Z$ are homotopic, then $k \circ h$ and $k' \circ h'$ are homotopic.
:::

::: {.solution}
::: pf

::: pf-step
Setting and given homotopies:
Let $F: X \times I \to Y$ be a continuous homotopy between $h$ and $h'$, so that:
$$F(x, 0) = h(x) \quad \text{and} \quad F(x, 1) = h'(x) \quad \text{for all } x \in X.$$
Let $G: Y \times I \to Z$ be a continuous homotopy between $k$ and $k'$, so that:
$$G(y, 0) = k(y) \quad \text{and} \quad G(y, 1) = k'(y) \quad \text{for all } y \in Y.$$
:::

::: pf-step
Construction of the composite homotopy:
Define the map $H: X \times I \to Z$ by:
$$H(x, t) = G(F(x, t), t).$$
:::

::: {.pf-step #s3}
Verification of continuity and boundary values:

::: pf-proof

::: pf-step
**Continuity:**
Consider the map $\Phi: X \times I \to Y \times I$ defined by $\Phi(x, t) = (F(x, t), t)$.
Since $F$ and the coordinate projection $(x, t) \mapsto t$ are continuous, $\Phi$ is continuous.
Because $H = G \circ \Phi$ is the composition of continuous maps, $H$ is continuous.
:::

::: pf-step
**Evaluation at $t = 0$:**
$$H(x, 0) = G(F(x, 0), 0) = G(h(x), 0) = k(h(x)) = (k \circ h)(x).$$
:::

::: pf-step
**Evaluation at $t = 1$:**
$$H(x, 1) = G(F(x, 1), 1) = G(h'(x), 1) = k'(h'(x)) = (k' \circ h')(x).$$
:::

:::

:::

::: pf-qed
By step [](#s3){.pf-ref}, $H$ is a continuous homotopy from $k \circ h$ to $k' \circ h'$, so $k \circ h \simeq k' \circ h'$.
:::

:::

:::
