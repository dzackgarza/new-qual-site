---
schema: qual/card@1
id: P-5AXU3
kind: problem
title: Maps $X\to S^1$ are nullhomotopic when $\pi_1(X)$ is finite
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Show that if $X$ is a path-connected, locally path-connected topological space with finite fundamental group $\pi_1(X, x_0)$, then every continuous map $f : X \to S^1$ is **homotopic to a constant map** (nullhomotopic).
:::

::: solution
**Goal:** Prove that every continuous map $f: X \to S^1$ lifts to the contractible universal covering space $\mathbb{R} \to S^1$ because $f_*(\pi_1(X))$ must be trivial.

<1>1. The Universal Covering Space $p: \mathbb{R} \to S^1$:
    *Proof:*
    <2>1. The standard exponential map $p: \mathbb{R} \to S^1$ given by $p(t) = e^{2\pi i t}$ is the **universal covering space** of the circle $S^1$.
    <2>2. The real line $\mathbb{R}$ is **contractible** ($\pi_1(\mathbb{R}) = 0$, $\mathbb{R} \simeq \{*\}$).
    <2>3. The subgroup of $\pi_1(S^1, 1) \cong \mathbb{Z}$ corresponding to the covering $p$ is the trivial subgroup $p_*(\pi_1(\mathbb{R})) = \{0\}$.

<1>2. Triviality of the Induced Homomorphism $f_*: \pi_1(X, x_0) \to \pi_1(S^1, f(x_0))$:
    *Proof:*
    <2>1. The induced map on fundamental groups is a group homomorphism:
        $$f_*: \pi_1(X, x_0) \longrightarrow \pi_1(S^1, f(x_0)) \cong \mathbb{Z}.$$
    <2>2. By the First Isomorphism Theorem for groups:
        $$\operatorname{im}(f_*) \cong \pi_1(X, x_0) / \ker(f_*).$$
    <2>3. Since $\pi_1(X, x_0)$ is a finite group of order $N < \infty$, the image $\operatorname{im}(f_*) \le \mathbb{Z}$ must be a **finite subgroup of $\mathbb{Z}$**.
    <2>4. The only finite subgroup of the infinite cyclic group $\mathbb{Z}$ is the trivial subgroup $\{0\}$.
    <2>5. Therefore, $\operatorname{im}(f_*) = \{0\}$, which means:
        $$f_*(\pi_1(X, x_0)) = \{0\} \subseteq p_*(\pi_1(\mathbb{R}, 0)).$$

<1>3. Existence of a Continuous Lift $\tilde{f}: X \to \mathbb{R}$:
    *Proof:*
    <2>1. Since $X$ is path-connected and locally path-connected, and $f_*(\pi_1(X, x_0)) \subseteq p_*(\pi_1(\mathbb{R})) = \{0\}$, by the **Lifting Criterion for Covering Spaces**:
        $$\text{There exists a continuous map } \tilde{f}: X \to \mathbb{R} \text{ such that } p \circ \tilde{f} = f.$$

<1>4. Homotopy to a Constant Map:
    *Proof:*
    <2>1. Since the target space $\mathbb{R}$ is contractible, the lift $\tilde{f}: X \to \mathbb{R}$ is homotopic to the constant map $c_0(x) = \tilde{f}(x_0)$ via the straight-line homotopy:
        $$H: X \times [0, 1] \longrightarrow \mathbb{R}, \qquad H(x, s) = (1 - s)\tilde{f}(x) + s \tilde{f}(x_0).$$
    <2>2. Composing the homotopy $H$ with the covering projection $p: \mathbb{R} \to S^1$:
        $$F: X \times [0, 1] \longrightarrow S^1, \qquad F(x, s) = (p \circ H)(x, s) = p\left( (1 - s)\tilde{f}(x) + s \tilde{f}(x_0) \right).$$
    <2>3. At $s = 0$: $F(x, 0) = p(\tilde{f}(x)) = f(x)$.
    <2>4. At $s = 1$: $F(x, 1) = p(\tilde{f}(x_0)) = f(x_0)$, which is a constant map on $X$.
    <2>5. Since $p$ and $H$ are continuous, $F$ is a continuous homotopy from $f$ to the constant map $f(x_0)$.

<1>5. Conclusion:
    $f$ is nullhomotopic. Q.E.D.
:::
