---
schema: qual/card@1
id: P-3QUC7
kind: problem
title: Maps $S^1\to X$ extend over $D^2$ when $\pi_1(X)=0$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Quotient Spaces
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Let $X$ be a path-connected topological space such that $\pi_1(X) = 0$. Prove that every continuous map $f: S^1 \to X$ can be extended to a continuous map $F: D^2 \to X$ (where $S^1 = \partial D^2$).
:::

::: solution
**Goal:** Prove that if $\pi_1(X) = 0$, every continuous map $f: S^1 \to X$ extends continuously to $F: D^2 \to X$.

<1>1. Realization of the 2-disk $D^2$ as a quotient cone of the cylinder $S^1 \times [0, 1]$:
    *Proof:*
    <2>1. Define the continuous map $q: S^1 \times [0, 1] \to D^2$ by
    $$q(z, t) = (1 - t)z \quad \text{for } z \in S^1 \subset \mathbb{C}, \, t \in [0, 1].$$
    <2>2. The map $q$ is surjective: for any point $w \in D^2$, if $w = 0$, $q(z, 1) = 0$ for any $z \in S^1$; if $w \neq 0$, $w = r e^{i\theta} = (1 - (1 - r)) e^{i\theta} = q(e^{i\theta}, 1 - r)$.
    <2>3. The fibers of $q$ are singletons $\{(z, t)\}$ for $t < 1$, and the top circle $S^1 \times \{1\}$ is mapped to the single point $0 \in D^2$.
    <2>4. Since the cylinder $S^1 \times [0, 1]$ is compact and $D^2$ is Hausdorff, the continuous surjection $q$ is a closed map, hence a quotient map.
    <2>5. Therefore $q$ induces a homeomorphism $(S^1 \times [0, 1]) / (S^1 \times \{1\}) \cong D^2$.

<1>2. Existence of a null-homotopy from the triviality of $\pi_1(X)$:
    *Proof:*
    <2>1. Fix a basepoint $s_0 \in S^1$ and let $x_0 = f(s_0) \in X$.
    <2>2. The map $f: S^1 \to X$ is a loop based at $x_0$, representing a homotopy class $[f] \in \pi_1(X, x_0)$.
    <2>3. By hypothesis, $\pi_1(X, x_0) = 0$, so $[f] = 0$.
    <2>4. Thus $f$ is homotopic relative to $s_0$ (and freely homotopic) to the constant loop $c_{x_0}(z) = x_0$: there exists a continuous map $H: S^1 \times [0, 1] \to X$ such that
    $$H(z, 0) = f(z) \quad \text{and} \quad H(z, 1) = x_0 \quad \text{for all } z \in S^1.$$

<1>3. Factoring the homotopy through the quotient to define the extension $F$:
    *Proof:*
    <2>1. On the collapsed subspace $S^1 \times \{1\}$, the homotopy $H$ satisfies $H(z, 1) = x_0$ for all $z \in S^1$, so $H$ is constant on $S^1 \times \{1\}$.
    <2>2. By the universal property of quotient maps, since $H$ is constant on the fibers of the quotient map $q: S^1 \times [0, 1] \to D^2$, there exists a unique continuous map $F: D^2 \to X$ making the diagram commute:
    $$F(q(z, t)) = H(z, t) \quad \text{for all } (z, t) \in S^1 \times [0, 1].$$
    <2>3. On the boundary circle $\partial D^2 = S^1$, points are represented by $w = z = q(z, 0)$ for $z \in S^1$.
    <2>4. Evaluating $F$ on the boundary:
    $$F(z) = F(q(z, 0)) = H(z, 0) = f(z) \quad \text{for all } z \in S^1.$$
    <2>5. Thus $F: D^2 \to X$ is a continuous extension of $f$.

<1>4. Conclusion:
    *Proof:*
    Every continuous map $f: S^1 \to X$ extends to a continuous map $F: D^2 \to X$.
:::
