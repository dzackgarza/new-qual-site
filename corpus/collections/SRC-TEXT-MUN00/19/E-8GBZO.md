---
schema: qual/card@1
id: E-8GBZO
kind: exercise
title: The box topology implication in the maps-into-products theorem
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

One of the implications stated in Theorem 19.6 holds for the box topology.
Which one?
:::

::: solution
**Goal:** Identify which implication of Theorem 19.6 (Maps into Products) holds when the product carries the box topology, and prove both the valid implication and the failure of the converse.

<1>1. Statement of the two implications in Theorem 19.6:
    Let $f: A \to \prod_{\alpha \in J} X_\alpha$ be given by $f(a) = (f_\alpha(a))_{\alpha \in J}$, where $f_\alpha = \pi_\alpha \circ f$.
    - **Implication 1 ($\implies$):** If $f$ is continuous, then each component function $f_\alpha$ is continuous.
    - **Implication 2 ($\impliedby$):** If each component function $f_\alpha$ is continuous, then $f$ is continuous.

<1>2. Implication 1 ($\implies$) holds for the box topology:
    *Proof:*
    <2>1. In the box topology on $\prod_{\alpha \in J} X_\alpha$, each canonical projection map $\pi_\alpha: \prod X_\beta \to X_\alpha$ is continuous.
    <2>2. Indeed, for any open subset $U \subseteq X_\alpha$, the preimage is:
        $$\pi_\alpha^{-1}(U) = U \times \prod_{\beta \neq \alpha} X_\beta,$$
        which is a basic open set in the box topology because each factor in the product is open in its respective space ($U$ in $X_\alpha$, and $X_\beta$ in $X_\beta$).
    <2>3. Because the composition of continuous functions is continuous, if $f: A \to \prod_{\text{box}} X_\alpha$ is continuous, then each coordinate function $f_\alpha = \pi_\alpha \circ f: A \to X_\alpha$ is continuous.

<1>3. Implication 2 ($\impliedby$) fails for the box topology:
    *Proof:*
    <2>1. Let $A = \mathbb{R}$ with the standard Euclidean topology, and let $\mathbb{R}^\omega = \prod_{n=1}^\infty \mathbb{R}$ carry the box topology.
    <2>2. Define $f: \mathbb{R} \to \mathbb{R}^\omega$ by $f(t) = (t, t, t, \dots)$.
    <2>3. Each component function $f_n(t) = t$ is the identity map, which is continuous.
    <2>4. Consider the box-open neighborhood of the origin:
        $$B = (-1, 1) \times \left(-\frac{1}{2}, \frac{1}{2}\right) \times \left(-\frac{1}{3}, \frac{1}{3}\right) \times \dots = \prod_{n=1}^\infty \left(-\frac{1}{n}, \frac{1}{n}\right).$$
    <2>5. The preimage under $f$ is:
        $$f^{-1}(B) = \bigcap_{n=1}^\infty f_n^{-1}\left(-\frac{1}{n}, \frac{1}{n}\right) = \bigcap_{n=1}^\infty \left(-\frac{1}{n}, \frac{1}{n}\right) = \{0\}.$$
    <2>6. The singleton $\{0\}$ is not open in $\mathbb{R}$, so $f$ is not continuous in the box topology.

<1>4. Conclusion:
    The implication **"If $f$ is continuous, then each coordinate function $f_\alpha$ is continuous"** holds for the box topology. Q.E.D.
:::
