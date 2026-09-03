---
schema: qual/card@1
id: E-2X3VM
kind: problem
title: Behavior of path connectedness under products, closures, images, and unions
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

(a) Is a product of path-connected spaces necessarily path connected?

(b) If $A \subset X$ and $A$ is path connected, is $\overline{A}$ necessarily path connected?

(c) If $f: X \to Y$ is continuous and $X$ is path connected, is $f(X)$ necessarily path connected?

(d) If $\ts{A_\alpha}$ is a collection of path-connected subspaces of $X$ and if $\bigcap A_\alpha \neq \varnothing$, is $\bigcup A_\alpha$ necessarily path connected?
:::

::: solution
**Goal:** Determine and prove the preservation properties of path-connectedness under products, closures, continuous images, and non-disjoint unions.

<1>1. Part (a): Arbitrary products of path-connected spaces are path-connected (YES).
    *Proof:*
    <2>1. Let $X = \prod_{\alpha \in J} X_\alpha$ where each $X_\alpha$ is path-connected.
    <2>2. Let $\mathbf{x} = (x_\alpha)_{\alpha \in J}$ and $\mathbf{y} = (y_\alpha)_{\alpha \in J}$ be arbitrary points in $X$.
    <2>3. For each $\alpha \in J$, path-connectedness of $X_\alpha$ gives a continuous path $\gamma_\alpha: [0, 1] \to X_\alpha$ with $\gamma_\alpha(0) = x_\alpha$ and $\gamma_\alpha(1) = y_\alpha$.
    <2>4. Define the product path $\gamma: [0, 1] \to X$ by $\gamma(t) = (\gamma_\alpha(t))_{\alpha \in J}$.
    <2>5. By the universal property of the product topology, $\gamma$ is continuous because each coordinate function $\pi_\alpha \circ \gamma = \gamma_\alpha$ is continuous.
    <2>6. Since $\gamma(0) = \mathbf{x}$ and $\gamma(1) = \mathbf{y}$, $\gamma$ is a path in $X$ connecting $\mathbf{x}$ to $\mathbf{y}$.

<1>2. Part (b): The closure of a path-connected set is not necessarily path-connected (NO).
    *Proof:*
    <2>1. Consider the topologist's sine curve in $\mathbb{R}^2$:
        $$A = \ts{\left(x, \sin\frac{1}{x}\right) \mid x \in (0, 1]}.$$
    <2>2. $A$ is homeomorphic to the interval $(0, 1]$ via $x \mapsto (x, \sin(1/x))$, hence $A$ is path-connected.
    <2>3. The closure is $\overline{A} = A \cup (\{0\} \times [-1, 1])$.
    <2>4. The space $\overline{A}$ is connected but fails to be path-connected: no continuous path in $\overline{A}$ can connect $(0, 0)$ to any point in $A$.

<1>3. Part (c): Continuous images of path-connected spaces are path-connected (YES).
    *Proof:*
    <2>1. Let $f: X \to Y$ be continuous and $X$ path-connected.
    <2>2. Let $y_1, y_2 \in f(X)$. Choose preimages $x_1, x_2 \in X$ such that $f(x_1) = y_1$ and $f(x_2) = y_2$.
    <2>3. Since $X$ is path-connected, there is a continuous path $\gamma: [0, 1] \to X$ with $\gamma(0) = x_1$ and $\gamma(1) = x_2$.
    <2>4. The composite $f \circ \gamma: [0, 1] \to f(X)$ is continuous, with $(f \circ \gamma)(0) = y_1$ and $(f \circ \gamma)(1) = y_2$.
    <2>5. Thus $f(X)$ is path-connected.

<1>4. Part (d): Unions of path-connected subspaces with non-empty intersection are path-connected (YES).
    *Proof:*
    <2>1. Let $\{A_\alpha\}_{\alpha \in J}$ be path-connected subspaces of $X$, and choose a basepoint $p \in \bigcap_{\alpha \in J} A_\alpha$.
    <2>2. Let $x, y \in \bigcup_{\alpha \in J} A_\alpha$. Then $x \in A_\beta$ and $y \in A_\delta$ for some indices $\beta, \delta \in J$.
    <2>3. Since $p, x \in A_\beta$, there exists a path $\gamma_1: [0, 1] \to A_\beta$ from $x$ to $p$.
    <2>4. Since $p, y \in A_\delta$, there exists a path $\gamma_2: [0, 1] \to A_\delta$ from $p$ to $y$.
    <2>5. The path product (concatenation) $\gamma_1 * \gamma_2: [0, 1] \to \bigcup_{\alpha \in J} A_\alpha$ is a continuous path from $x$ to $y$.
    <2>6. Thus $\bigcup_{\alpha \in J} A_\alpha$ is path-connected. Q.E.D.
:::
