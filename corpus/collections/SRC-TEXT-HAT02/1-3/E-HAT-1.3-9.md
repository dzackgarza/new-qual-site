---
schema: qual/card@1
id: E-HAT-1.3-9
kind: exercise
title: "Maps to $S^1$ from spaces with finite fundamental group"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
Show that if a path-connected, locally path-connected space $X$ has $\pi_1(X)$ finite, then every map $f: X \to S^1$ is nullhomotopic.
:::

::: solution
**Goal:** Prove that every continuous map $f: X \to S^1$ from a path-connected, locally path-connected space with finite $\pi_1(X)$ is nullhomotopic, by lifting $f$ to the universal cover $\mathbb{R}$.

<1>1. Triviality of the induced homomorphism on fundamental groups:
    *Proof:*
    <2>1. Fix a basepoint $x_0 \in X$ and let $s_0 = f(x_0) \in S^1$.
    <2>2. The induced map $f_*: \pi_1(X, x_0) \to \pi_1(S^1, s_0) \cong \mathbb{Z}$ is a group homomorphism.
    <2>3. The image $f_*(\pi_1(X, x_0))$ is a subgroup of $\mathbb{Z}$.
    <2>4. By the First Isomorphism Theorem for groups, $|f_*(\pi_1(X, x_0))|$ divides $|\pi_1(X, x_0)| < \infty$, so the image is a finite subgroup of $\mathbb{Z}$.
    <2>5. Since $\mathbb{Z}$ is infinite cyclic and torsion-free, its only finite subgroup is the trivial subgroup $\{0\}$.
    <2>6. Thus $f_*(\pi_1(X, x_0)) = \{0\}$.

<1>2. Lifting $f$ to the universal cover $\mathbb{R}$:
    *Proof:*
    <2>1. Let $p: \mathbb{R} \to S^1$ be the standard universal covering map given by $p(t) = e^{2\pi i t}$, and choose $t_0 \in \mathbb{R}$ with $p(t_0) = s_0$.
    <2>2. The fundamental group of the total space is trivial: $p_*(\pi_1(\mathbb{R}, t_0)) = \{0\}$.
    <2>3. From <1>1, we have $f_*(\pi_1(X, x_0)) = \{0\} \subseteq p_*(\pi_1(\mathbb{R}, t_0))$.
    <2>4. Since $X$ is path-connected and locally path-connected, the Covering Space Lifting Criterion applies: there exists a unique continuous map $\widetilde{f}: X \to \mathbb{R}$ such that
    $$p \circ \widetilde{f} = f \quad \text{and} \quad \widetilde{f}(x_0) = t_0.$$

<1>3. Null-homotopy of $f$:
    *Proof:*
    <2>1. The codomain $\mathbb{R}$ is convex and contractible.
    <2>2. Define the straight-line homotopy $\widetilde{H}: X \times [0, 1] \to \mathbb{R}$ by
    $$\widetilde{H}(x, t) = (1 - t) \widetilde{f}(x) + t \cdot 0.$$
    <2>3. The map $\widetilde{H}$ is continuous, with $\widetilde{H}(x, 0) = \widetilde{f}(x)$ and $\widetilde{H}(x, 1) = 0$ (the constant map to $0 \in \mathbb{R}$).
    <2>4. Define $H: X \times [0, 1] \to S^1$ by post-composing with the covering map:
    $$H(x, t) = p(\widetilde{H}(x, t)) = e^{2\pi i \widetilde{H}(x, t)}.$$
    <2>5. Since $p$ and $\widetilde{H}$ are continuous, $H$ is a continuous homotopy.
    <2>6. Evaluating at the endpoints:
    $$H(x, 0) = p(\widetilde{f}(x)) = f(x), \qquad H(x, 1) = p(0) = e^0 = 1.$$
    <2>7. Thus $H$ is a homotopy between $f$ and the constant map $c_1(x) = 1$.

<1>4. Conclusion:
    *Proof:*
    Every continuous map $f: X \to S^1$ is nullhomotopic.
:::
