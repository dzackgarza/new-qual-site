---
schema: qual/card@1
id: E-HAT-1.1-11
kind: exercise
title: Inclusion of path-component induces isomorphism on $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Path Components
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
If $X_0$ is the path-component of a space $X$ containing the basepoint $x_0$, show that the inclusion $i: X_0 \hookrightarrow X$ induces an isomorphism $i_*: \pi_1(X_0, x_0) \to \pi_1(X, x_0)$.
:::

::: solution
**Goal:** Prove that the inclusion $i: X_0 \hookrightarrow X$ induces an isomorphism $i_*: \pi_1(X_0, x_0) \to \pi_1(X, x_0)$ on fundamental groups.

<1>1. Key Lemma: Any continuous map from a path-connected space into $X$ sending a basepoint to $x_0$ has image contained in $X_0$.
    *Proof:*
    <2>1. Let $Y$ be a path-connected space, $y_0 \in Y$, and let $f: Y \to X$ be a continuous map with $f(y_0) = x_0$.
    <2>2. For any point $y \in Y$, there exists a continuous path $\gamma: [0, 1] \to Y$ with $\gamma(0) = y_0$ and $\gamma(1) = y$.
    <2>3. The composite $f \circ \gamma: [0, 1] \to X$ is a continuous path in $X$ starting at $(f \circ \gamma)(0) = f(y_0) = x_0$ and ending at $(f \circ \gamma)(1) = f(y)$.
    <2>4. Since $X_0$ is the path-component of $x_0$, by definition $X_0$ contains all points in $X$ path-connected to $x_0$.
    <2>5. Therefore $f(y) \in X_0$ for every $y \in Y$, so $f(Y) \subseteq X_0$.

<1>2. Surjectivity of $i_*: \pi_1(X_0, x_0) \to \pi_1(X, x_0)$:
    *Proof:*
    <2>1. Let $[\gamma] \in \pi_1(X, x_0)$ be represented by a continuous loop $\gamma: [0, 1] \to X$ with $\gamma(0) = \gamma(1) = x_0$.
    <2>2. Since the unit interval $[0, 1]$ is path-connected and $\gamma(0) = x_0$, <1>1 implies $\gamma([0, 1]) \subseteq X_0$.
    <2>3. Thus $\gamma$ restricts to a well-defined continuous loop $\gamma_0: [0, 1] \to X_0$ based at $x_0$.
    <2>4. The homotopy class $[\gamma_0] \in \pi_1(X_0, x_0)$ satisfies $i_*([\gamma_0]) = [i \circ \gamma_0] = [\gamma]$.
    <2>5. Therefore $i_*$ is surjective.

<1>3. Injectivity of $i_*: \pi_1(X_0, x_0) \to \pi_1(X, x_0)$:
    *Proof:*
    <2>1. Let $[\alpha], [\beta] \in \pi_1(X_0, x_0)$ and suppose $i_*([\alpha]) = i_*([\beta])$ in $\pi_1(X, x_0)$.
    <2>2. By definition of path homotopy in $X$, there exists a continuous map $H: [0, 1] \times [0, 1] \to X$ such that:
    $$H(s, 0) = \alpha(s), \quad H(s, 1) = \beta(s), \quad H(0, t) = x_0, \quad H(1, t) = x_0 \quad \text{for all } s, t \in [0, 1].$$
    <2>3. Since the square $I^2 = [0, 1] \times [0, 1]$ is path-connected and $H(0, 0) = x_0$, <1>1 implies $H(I^2) \subseteq X_0$.
    <2>4. Thus $H$ is a continuous map into $X_0$, which constitutes a valid basepoint-preserving path homotopy between $\alpha$ and $\beta$ inside $X_0$.
    <2>5. Therefore $[\alpha] = [\beta]$ in $\pi_1(X_0, x_0)$, proving that $i_*$ is injective.

<1>4. Conclusion:
    *Proof:*
    The map $i_*: \pi_1(X_0, x_0) \to \pi_1(X, x_0)$ is a bijective group homomorphism, hence an isomorphism of groups.
:::
