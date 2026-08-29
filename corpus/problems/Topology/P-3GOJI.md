---
schema: qual/card@1
id: P-3GOJI
kind: problem
title: One-point compactification is compact; path-connected implies connected
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) Show that for $X$ an arbitrary topological space, the one-point (Alexandroff) compactification $X^* = X \cup \{\infty\}$ is compact.

(2) Prove that every path-connected topological space is connected.
:::

::: solution
**Goal:** Prove that the one-point compactification $X^*$ is compact, and that path-connectedness implies connectedness.

<1>1. Part (1): One-point compactification $X^*$ is compact:
    *Proof:*
    <2>1. By definition, the topology on $X^* = X \cup \{\infty\}$ consists of:
        - All open subsets $U \subseteq X$, and
        - All subsets of the form $(X \setminus K) \cup \{\infty\}$ where $K \subseteq X$ is closed and compact in $X$.
    <2>2. Let $\mathcal{U} = \{V_\alpha\}_{\alpha \in I}$ be an open cover of $X^*$, so $X^* = \bigcup_{\alpha \in I} V_\alpha$.
    <2>3. Because $\infty \in X^*$, there exists some open set $V_{\alpha_0} \in \mathcal{U}$ containing the point $\infty$.
    <2>4. By definition of open neighborhoods of $\infty$, $V_{\alpha_0} = (X \setminus K) \cup \{\infty\}$ for some compact subset $K \subseteq X$.
    <2>5. The remaining points of $X^*$ to be covered lie in $X^* \setminus V_{\alpha_0} = K$.
    <2>6. Since $K \subseteq X^*$, the collection $\mathcal{U}$ is an open cover of $K$.
    <2>7. For each $x \in K$, choose an open set $V_\alpha \in \mathcal{U}$ containing $x$, and let $W_\alpha = V_\alpha \cap X$, which is open in $X$.
    <2>8. Then $\{W_\alpha\}_{\alpha \in I}$ is an open cover of the compact set $K$ in $X$.
    <2>9. By compactness of $K$, there exist finitely many indices $\alpha_1, \dots, \alpha_n \in I$ such that:
        $$K \subseteq \bigcup_{j=1}^n W_{\alpha_j} \subseteq \bigcup_{j=1}^n V_{\alpha_j}.$$
    <2>10. Therefore:
        $$X^* = V_{\alpha_0} \cup K \subseteq V_{\alpha_0} \cup V_{\alpha_1} \cup \cdots \cup V_{\alpha_n}.$$
    <2>11. Thus $\{V_{\alpha_0}, V_{\alpha_1}, \dots, V_{\alpha_n}\}$ is a finite subcover of $X^*$, which proves $X^*$ is compact.

<1>2. Part (2): Path-connected implies connected:
    *Proof:*
    <2>1. Let $X$ be a path-connected topological space.
    <2>2. Suppose, for contradiction, that $X$ is disconnected.
    <2>3. Then there exists a continuous surjective map $f: X \to \{0, 1\}$ (where $\{0, 1\}$ has the discrete topology).
    <2>4. Because $f$ is surjective, choose $x_0, x_1 \in X$ such that $f(x_0) = 0$ and $f(x_1) = 1$.
    <2>5. Because $X$ is path-connected, there exists a continuous path $\gamma: [0, 1] \to X$ such that $\gamma(0) = x_0$ and $\gamma(1) = x_1$.
    <2>6. Consider the composition $h = f \circ \gamma: [0, 1] \to \{0, 1\}$.
    <2>7. As a composition of continuous maps, $h$ is continuous.
    <2>8. The unit interval $[0, 1] \subset \mathbb{R}$ is connected, so its continuous image $h([0, 1]) \subseteq \{0, 1\}$ must be connected.
    <2>9. But $h(0) = f(x_0) = 0$ and $h(1) = f(x_1) = 1$, so $h([0, 1]) = \{0, 1\}$, which is disconnected!
    <2>10. This contradiction shows that no continuous surjection $f: X \to \{0, 1\}$ can exist, so $X$ is connected.

<1>3. Conclusion:
    $X^*$ is compact, and every path-connected space is connected. Q.E.D.
:::
