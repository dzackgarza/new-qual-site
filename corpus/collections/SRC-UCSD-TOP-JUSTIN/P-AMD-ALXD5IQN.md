---
schema: qual/card@1
id: P-AMD-ALXD5IQN
kind: problem
title: The fundamental group of a product is the product of the fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show $\pi_1(X\times Y, (x_0, y_0)) \cong \pi_1(X,x_0) \times \pi_1(Y, y_0)$.
:::

::: {.solution}
**Goal:** Let $(X, x_0)$ and $(Y, y_0)$ be pointed topological spaces.
Prove that the canonical map $\Phi \colon \pi_1(X \times Y, (x_0, y_0)) \to \pi_1(X, x_0) \times \pi_1(Y, y_0)$ given by $[\gamma] \mapsto ((p_X)_*[\gamma], (p_Y)_*[\gamma])$ is an isomorphism of groups.

::: pf

::: pf-step
Definition of the projection maps and homomorphism $\Phi$.

::: pf-proof

::: pf-step
Let $p_X \colon X \times Y \to X$ and $p_Y \colon X \times Y \to Y$ be the standard continuous projection maps.
:::

::: pf-step
The induced maps on fundamental groups $(p_X)_* \colon \pi_1(X \times Y, (x_0, y_0)) \to \pi_1(X, x_0)$ and $(p_Y)_* \colon \pi_1(X \times Y, (x_0, y_0)) \to \pi_1(Y, y_0)$ are group homomorphisms by functoriality of $\pi_1$.
:::

::: pf-step
Define $\Phi \colon \pi_1(X \times Y, (x_0, y_0)) \to \pi_1(X, x_0) \times \pi_1(Y, y_0)$ by: $$\Phi([\gamma]) = ((p_X)_*[\gamma], (p_Y)_*[\gamma]) = ([p_X \circ \gamma], [p_Y \circ \gamma]).$$
:::

::: pf-step
Since both components are homomorphisms, $\Phi$ is a group homomorphism.

::: pf-proof
The induced maps $(p_X)_*$ and $(p_Y)_*$ are homomorphisms by functoriality of $\pi_1$, and the product of two homomorphisms is a homomorphism, so $\Phi$ is a group homomorphism.
:::

:::

:::

:::

::: pf-step
Prove that $\Phi$ is surjective.

::: pf-proof

::: pf-step
Let $([\alpha], [\beta]) \in \pi_1(X, x_0) \times \pi_1(Y, y_0)$, where $\alpha \colon [0, 1] \to X$ is a loop based at $x_0$ and $\beta \colon [0, 1] \to Y$ is a loop based at $y_0$.
:::

::: pf-step
Define $\gamma \colon [0, 1] \to X \times Y$ by $\gamma(t) = (\alpha(t), \beta(t))$.
:::

::: pf-step
By the universal property of the product topology, $\gamma$ is continuous since its component paths $p_X \circ \gamma = \alpha$ and $p_Y \circ \gamma = \beta$ are continuous.
:::

::: pf-step
Furthermore, $\gamma(0) = (\alpha(0), \beta(0)) = (x_0, y_0)$ and $\gamma(1) = (\alpha(1), \beta(1)) = (x_0, y_0)$, so $\gamma$ is a loop in $X \times Y$ based at $(x_0, y_0)$.
:::

::: pf-step
Then $\Phi([\gamma]) = ([p_X \circ \gamma], [p_Y \circ \gamma]) = ([\alpha], [\beta])$.
:::

::: pf-qed
The loop $\gamma(t) = (\alpha(t), \beta(t))$ is continuous by the universal property of the product topology, is based at $(x_0, y_0)$ because $\alpha$ and $\beta$ are based at $x_0$ and $y_0$, and satisfies $p_X \circ \gamma = \alpha$ and $p_Y \circ \gamma = \beta$; hence $\Phi([\gamma]) = ([\alpha], [\beta])$.
:::

:::

:::

::: {.pf-step #s3}
Prove that $\Phi$ is injective.

::: pf-proof

::: pf-step
Suppose $[\gamma] \in \ker(\Phi)$, so $\Phi([\gamma]) = ([c_{x_0}], [c_{y_0}])$, where $c_{x_0}, c_{y_0}$ are constant loops.
:::

::: pf-step
This means there exist path homotopies:

- $F \colon [0, 1] \times [0, 1] \to X$ between $p_X \circ \gamma$ and $c_{x_0}$ relative to $\{0, 1\}$,

- $G \colon [0, 1] \times [0, 1] \to Y$ between $p_Y \circ \gamma$ and $c_{y_0}$ relative to $\{0, 1\}$.
:::

::: pf-step
Define $H \colon [0, 1] \times [0, 1] \to X \times Y$ by $H(t, s) = (F(t, s), G(t, s))$.
:::

::: pf-step
$H$ is continuous because its component functions $F$ and $G$ are continuous.
:::

::: {.pf-step #s3-5}
Check boundary conditions:

- $H(t, 0) = (F(t, 0), G(t, 0)) = (p_X(\gamma(t)), p_Y(\gamma(t))) = \gamma(t)$,

- $H(t, 1) = (F(t, 1), G(t, 1)) = (x_0, y_0) = c_{(x_0, y_0)}(t)$,

- For all $s \in [0, 1]$, $H(0, s) = (F(0, s), G(0, s)) = (x_0, y_0)$ and $H(1, s) = (F(1, s), G(1, s)) = (x_0, y_0)$.
:::

::: pf-step
Thus $H$ is a path homotopy in $X \times Y$ between $\gamma$ and the constant loop $c_{(x_0, y_0)}$, so $[\gamma] = 1 \in \pi_1(X \times Y, (x_0, y_0))$.
:::

::: pf-qed
The homotopy $H(t, s) = (F(t, s), G(t, s))$ is continuous because $F$ and $G$ are, and its boundary conditions in step [](#s3-5){.pf-ref} show it is a path homotopy from $\gamma$ to the constant loop; hence $\ker(\Phi) = \{1\}$, so $\Phi$ is injective.
:::

:::

:::

::: pf-qed
$\Phi$ is a bijective group homomorphism, hence an isomorphism: $\pi_1(X \times Y, (x_0, y_0)) \cong \pi_1(X, x_0) \times \pi_1(Y, y_0)$.
:::

:::
:::
