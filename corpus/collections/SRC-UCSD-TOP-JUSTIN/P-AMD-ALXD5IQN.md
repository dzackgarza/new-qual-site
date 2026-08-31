---
schema: qual/card@1
id: P-AMD-ALXD5IQN
kind: problem
title: Show $\pi_1(X\times Y, (x_0, y_0)) \cong \pi_1(X,x_0) \times \pi_1(Y, y_0)$.
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

<1>1. Definition of the projection maps and homomorphism $\Phi$.
<2>1. Let $p_X \colon X \times Y \to X$ and $p_Y \colon X \times Y \to Y$ be the standard continuous projection maps.
<2>2. The induced maps on fundamental groups $(p_X)_* \colon \pi_1(X \times Y, (x_0, y_0)) \to \pi_1(X, x_0)$ and $(p_Y)_* \colon \pi_1(X \times Y, (x_0, y_0)) \to \pi_1(Y, y_0)$ are group homomorphisms by functoriality of $\pi_1$.
<2>3. Define $\Phi \colon \pi_1(X \times Y, (x_0, y_0)) \to \pi_1(X, x_0) \times \pi_1(Y, y_0)$ by: $$\Phi([\gamma]) = ((p_X)_*[\gamma], (p_Y)_*[\gamma]) = ([p_X \circ \gamma], [p_Y \circ \gamma]).$$ <2>4. Since both components are homomorphisms, $\Phi$ is a group homomorphism.
::: {.proof}
<2>5. The induced maps $(p_X)_*$ and $(p_Y)_*$ are homomorphisms by functoriality of $\pi_1$, and the product of two homomorphisms is a homomorphism, so $\Phi$ is a group homomorphism.
:::

<1>2. Prove that $\Phi$ is surjective.
<2>1. Let $([\alpha], [\beta]) \in \pi_1(X, x_0) \times \pi_1(Y, y_0)$, where $\alpha \colon [0, 1] \to X$ is a loop based at $x_0$ and $\beta \colon [0, 1] \to Y$ is a loop based at $y_0$.
<2>2. Define $\gamma \colon [0, 1] \to X \times Y$ by $\gamma(t) = (\alpha(t), \beta(t))$.
<2>3. By the universal property of the product topology, $\gamma$ is continuous since its component paths $p_X \circ \gamma = \alpha$ and $p_Y \circ \gamma = \beta$ are continuous.
<2>4. Furthermore, $\gamma(0) = (\alpha(0), \beta(0)) = (x_0, y_0)$ and $\gamma(1) = (\alpha(1), \beta(1)) = (x_0, y_0)$, so $\gamma$ is a loop in $X \times Y$ based at $(x_0, y_0)$.
<2>5. Then $\Phi([\gamma]) = ([p_X \circ \gamma], [p_Y \circ \gamma]) = ([\alpha], [\beta])$.
::: {.proof}
<2>6. The loop $\gamma(t) = (\alpha(t), \beta(t))$ is continuous by the universal property of the product topology, is based at $(x_0, y_0)$ because $\alpha$ and $\beta$ are based at $x_0$ and $y_0$, and satisfies $p_X \circ \gamma = \alpha$ and $p_Y \circ \gamma = \beta$; hence $\Phi([\gamma]) = ([\alpha], [\beta])$.
:::

<1>3. Prove that $\Phi$ is injective.
<2>1. Suppose $[\gamma] \in \ker(\Phi)$, so $\Phi([\gamma]) = ([c_{x_0}], [c_{y_0}])$, where $c_{x_0}, c_{y_0}$ are constant loops.
<2>2. This means there exist path homotopies:

- $F \colon [0, 1] \times [0, 1] \to X$ between $p_X \circ \gamma$ and $c_{x_0}$ relative to $\{0, 1\}$,

- $G \colon [0, 1] \times [0, 1] \to Y$ between $p_Y \circ \gamma$ and $c_{y_0}$ relative to $\{0, 1\}$.
  <2>3. Define $H \colon [0, 1] \times [0, 1] \to X \times Y$ by $H(t, s) = (F(t, s), G(t, s))$.
  <2>4. $H$ is continuous because its component functions $F$ and $G$ are continuous.
  <2>5. Check boundary conditions:

- $H(t, 0) = (F(t, 0), G(t, 0)) = (p_X(\gamma(t)), p_Y(\gamma(t))) = \gamma(t)$,

- $H(t, 1) = (F(t, 1), G(t, 1)) = (x_0, y_0) = c_{(x_0, y_0)}(t)$,

- For all $s \in [0, 1]$, $H(0, s) = (F(0, s), G(0, s)) = (x_0, y_0)$ and $H(1, s) = (F(1, s), G(1, s)) = (x_0, y_0)$.
  <2>6. Thus $H$ is a path homotopy in $X \times Y$ between $\gamma$ and the constant loop $c_{(x_0, y_0)}$, so $[\gamma] = 1 \in \pi_1(X \times Y, (x_0, y_0))$.
::: {.proof}
  <2>7. The homotopy $H(t, s) = (F(t, s), G(t, s))$ is continuous because $F$ and $G$ are, and its boundary conditions in <2>5 show it is a path homotopy from $\gamma$ to the constant loop; hence $\ker(\Phi) = \{1\}$, so $\Phi$ is injective.
:::

<1>4. Q.E.D.
::: {.proof}
<2>1. $\Phi$ is a bijective group homomorphism, hence an isomorphism: $\pi_1(X \times Y, (x_0, y_0)) \cong \pi_1(X, x_0) \times \pi_1(Y, y_0)$.
:::
:::
