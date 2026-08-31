---
schema: qual/card@1
id: P-KFPX5
kind: problem
title: Covering maps inject on $\pi_1$ and are homeomorphisms if they induce $\pi_1$-isomorphisms
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Homotopy
relations: []
review: draft
---

::: problem
(a) Give the definition of a **covering space** $\widetilde{X}$ (and **covering map** $p: \widetilde{X} \to X$) for a topological space $X$.

(b) State the **homotopy lifting property** of covering spaces. Use it to show that a covering map $p: \widetilde{X} \to X$ induces an injective group homomorphism
$$
p_*: \pi_1(\widetilde{X}, \widetilde{x}_0) \to \pi_1(X, p(\widetilde{x}_0))
$$
on fundamental groups.

(c) Let $p: \widetilde{X} \to X$ be a covering map with $\widetilde{X}$ and $X$ path-connected. Suppose that the induced homomorphism $p_*$ on fundamental groups is an isomorphism. Prove that $p$ is a homeomorphism.
:::

::: solution
**Goal:** Define covering spaces and the homotopy lifting property, prove that covering maps induce injections on $\pi_1$, and prove that a $\pi_1$-isomorphism between path-connected spaces makes the covering map a homeomorphism.

<1>1. Part (a): Definition of covering space and covering map.
    *Proof:*
    <2>1. Let $X$ be a topological space. A covering space of $X$ consists of a topological space $\widetilde{X}$ and a continuous surjective map $p: \widetilde{X} \to X$ such that every point $x \in X$ has an open neighborhood $U \subseteq X$ that is evenly covered by $p$.
    <2>2. An open set $U \subseteq X$ is evenly covered if the preimage $p^{-1}(U)$ can be expressed as a disjoint union of open subsets in $\widetilde{X}$:
    $$p^{-1}(U) = \bigsqcup_{\alpha \in A} V_\alpha,$$
    such that for each index $\alpha \in A$, the restriction $p|_{V_\alpha}: V_\alpha \to U$ is a homeomorphism.
    <2>3. The map $p$ is called a covering map, $X$ is the base space, and the sets $V_\alpha$ are called the sheets of the covering over $U$.

<1>2. Part (b): Statement of the Homotopy Lifting Property (HLP).
    *Proof:*
    <2>1. Let $p: \widetilde{X} \to X$ be a covering map, let $Y$ be a topological space, let $f: Y \to \widetilde{X}$ be a continuous map, and let $H: Y \times [0, 1] \to X$ be a continuous homotopy such that $H(y, 0) = p(f(y))$ for all $y \in Y$.
    <2>2. Then there exists a unique continuous homotopy $\widetilde{H}: Y \times [0, 1] \to \widetilde{X}$ such that $\widetilde{H}(y, 0) = f(y)$ for all $y \in Y$ and $p \circ \widetilde{H} = H$.

<1>3. Part (b): Proof that $p_*: \pi_1(\widetilde{X}, \widetilde{x}_0) \to \pi_1(X, x_0)$ is injective.
    *Proof:*
    <2>1. Let $x_0 = p(\widetilde{x}_0)$. Let $[\gamma] \in \pi_1(\widetilde{X}, \widetilde{x}_0)$ be represented by a continuous loop $\gamma: [0, 1] \to \widetilde{X}$ with $\gamma(0) = \gamma(1) = \widetilde{x}_0$.
    <2>2. Suppose $[\gamma] \in \ker p_*$, which means $p_*([\gamma]) = [p \circ \gamma] = [c_{x_0}] \in \pi_1(X, x_0)$, where $c_{x_0}$ is the constant loop at $x_0$.
    <2>3. This means there is a basepoint-preserving homotopy of paths $H: [0, 1] \times [0, 1] \to X$ such that:
    $$H(s, 0) = (p \circ \gamma)(s), \quad H(s, 1) = x_0, \quad H(0, t) = x_0, \quad H(1, t) = x_0 \quad \text{for all } s, t \in [0, 1].$$
    <2>4. Applying the Homotopy Lifting Property with $Y = [0, 1]$ and initial map $\gamma: [0, 1] \to \widetilde{X}$, there exists a unique continuous lift $\widetilde{H}: [0, 1] \times [0, 1] \to \widetilde{X}$ with $\widetilde{H}(s, 0) = \gamma(s)$ and $p \circ \widetilde{H} = H$.
    <2>5. Consider the path $t \mapsto \widetilde{H}(0, t)$. It is a lift of the constant path $t \mapsto H(0, t) = x_0$ starting at $\widetilde{H}(0, 0) = \gamma(0) = \widetilde{x}_0$. By uniqueness of path lifting, $\widetilde{H}(0, t) = \widetilde{x}_0$ for all $t \in [0, 1]$.
    <2>6. Similarly, the path $t \mapsto \widetilde{H}(1, t)$ is a lift of the constant path $t \mapsto H(1, t) = x_0$ starting at $\widetilde{H}(1, 0) = \gamma(1) = \widetilde{x}_0$, so $\widetilde{H}(1, t) = \widetilde{x}_0$ for all $t \in [0, 1]$.
    <2>7. At $t = 1$, $s \mapsto \widetilde{H}(s, 1)$ is a lift of the constant path $s \mapsto H(s, 1) = x_0$ starting at $\widetilde{H}(0, 1) = \widetilde{x}_0$, so $\widetilde{H}(s, 1) = \widetilde{x}_0$ for all $s \in [0, 1]$.
    <2>8. Thus $\widetilde{H}$ is a basepoint-preserving homotopy of loops in $\widetilde{X}$ between $\gamma$ and the constant loop $c_{\widetilde{x}_0}$, proving $[\gamma] = 0 \in \pi_1(\widetilde{X}, \widetilde{x}_0)$.
    <2>9. Therefore $\ker p_* = \{0\}$, so $p_*$ is injective.

<1>4. Part (c): Bijectivity of the covering map $p$.
    *Proof:*
    <2>1. Fix a basepoint $\widetilde{x}_0 \in \widetilde{X}$ and let $x_0 = p(\widetilde{x}_0)$. We show that the fiber $p^{-1}(x_0)$ consists only of the single point $\widetilde{x}_0$.
    <2>2. Let $\widetilde{x}_1 \in p^{-1}(x_0)$ be any point in the fiber.
    <2>3. Since $\widetilde{X}$ is path-connected, there exists a continuous path $\widetilde{\alpha}: [0, 1] \to \widetilde{X}$ from $\widetilde{x}_0$ to $\widetilde{x}_1$ (so $\widetilde{\alpha}(0) = \widetilde{x}_0$ and $\widetilde{\alpha}(1) = \widetilde{x}_1$).
    <2>4. The projected path $\alpha = p \circ \widetilde{\alpha}: [0, 1] \to X$ satisfies $\alpha(0) = p(\widetilde{x}_0) = x_0$ and $\alpha(1) = p(\widetilde{x}_1) = x_0$, so $\alpha$ is a loop based at $x_0$, representing $[\alpha] \in \pi_1(X, x_0)$.
    <2>5. By hypothesis, $p_*: \pi_1(\widetilde{X}, \widetilde{x}_0) \to \pi_1(X, x_0)$ is an isomorphism, so it is surjective. Thus there exists a loop class $[\beta] \in \pi_1(\widetilde{X}, \widetilde{x}_0)$ such that $p_*([\beta]) = [\alpha]$.
    <2>6. This means the loop $p \circ \beta$ is path-homotopic to $\alpha$ in $X$ via a path-homotopy $H: [0, 1] \times [0, 1] \to X$ with $H(s, 0) = \alpha(s)$ and $H(s, 1) = (p \circ \beta)(s)$, keeping endpoints fixed at $x_0$.
    <2>7. By the Homotopy Lifting Property, $H$ lifts to a homotopy $\widetilde{H}: [0, 1] \times [0, 1] \to \widetilde{X}$ with $\widetilde{H}(s, 0) = \widetilde{\alpha}(s)$.
    <2>8. The lift of $p \circ \beta$ starting at $\widetilde{x}_0$ is the loop $\beta$, so $\widetilde{H}(1, 1) = \beta(1) = \widetilde{x}_0$.
    <2>9. Since $\widetilde{H}(1, t)$ must be constant in the discrete fiber $p^{-1}(x_0)$, $\widetilde{x}_1 = \widetilde{\alpha}(1) = \widetilde{H}(1, 0) = \widetilde{H}(1, 1) = \widetilde{x}_0$.
    <2>10. Thus $p^{-1}(x_0) = \{\widetilde{x}_0\}$ is a singleton.
    <2>11. Since $X$ is path-connected and the cardinality of the fiber $p^{-1}(x)$ is locally constant, $|p^{-1}(x)| = 1$ for all $x \in X$. Thus $p$ is a bijection.

<1>5. Part (c): Bijective covering map is a homeomorphism.
    *Proof:*
    <2>1. The map $p: \widetilde{X} \to X$ is continuous and bijective by <1>4.
    <2>2. To show that $p$ is a homeomorphism, it suffices to prove that $p$ is an open map.
    <2>3. Let $W \subseteq \widetilde{X}$ be an open set, and let $x \in p(W)$. Choose $\widetilde{w} \in W$ such that $p(\widetilde{w}) = x$.
    <2>4. Let $U$ be an evenly covered open neighborhood of $x$ in $X$. Since $|p^{-1}(x)| = 1$, $p^{-1}(U) = V$ consists of a single open sheet $V \subseteq \widetilde{X}$, and $p|_V: V \to U$ is a homeomorphism.
    <2>5. The set $W \cap V$ is an open neighborhood of $\widetilde{w}$ in $V$.
    <2>6. Since $p|_V$ is a homeomorphism, $p(W \cap V)$ is open in $U$, and hence open in $X$.
    <2>7. Since $x = p(\widetilde{w}) \in p(W \cap V) \subseteq p(W)$, $p(W)$ is a neighborhood of each of its points, so $p(W)$ is open in $X$.
    <2>8. Therefore $p$ is an open continuous bijection, so $p$ is a homeomorphism.

<1>6. Conclusion:
    *Proof:*
    Covering maps induce injective homomorphisms on fundamental groups via the homotopy lifting property, and every covering map between path-connected spaces that induces an isomorphism on $\pi_1$ is a homeomorphism.
:::
