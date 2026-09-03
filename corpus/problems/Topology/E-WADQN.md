---
schema: qual/card@1
id: E-WADQN
kind: problem
title: Extreme value theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Show that if $f: X \to \mathbb{R}$ is continuous and $X$ is a compact topological space, then $f(X)$ is bounded and $f$ attains its minimum and maximum on $X$.
:::

::: solution
**Goal:** Prove the Extreme Value Theorem: the image of a compact space under a continuous real-valued function is compact, hence closed and bounded in $\mathbb{R}$, containing its infimum and supremum.

<1>1. Step 1: The continuous image of a compact space is compact:
    *Proof:*
    <2>1. Let $\{V_\alpha\}_{\alpha \in I}$ be an open cover of the image $f(X) \subseteq \mathbb{R}$, so $f(X) \subseteq \bigcup_{\alpha \in I} V_\alpha$ with each $V_\alpha$ open in $\mathbb{R}$.
    <2>2. Since $f: X \to \mathbb{R}$ is continuous, each preimage $U_\alpha = f^{-1}(V_\alpha)$ is an open subset of $X$.
    <2>3. For every $x \in X$, $f(x) \in f(X) \subseteq \bigcup V_\alpha$, so $f(x) \in V_\alpha$ for some $\alpha$, which means $x \in f^{-1}(V_\alpha) = U_\alpha$.
    <2>4. Thus $\{U_\alpha\}_{\alpha \in I}$ is an open cover of $X$.
    <2>5. Since $X$ is compact, there exists a finite subcover $\{U_{\alpha_1}, \dots, U_{\alpha_n}\}$ such that $X = \bigcup_{j=1}^n U_{\alpha_j}$.
    <2>6. Applying $f$ to both sides:
        $$f(X) = f\left(\bigcup_{j=1}^n U_{\alpha_j}\right) = \bigcup_{j=1}^n f(U_{\alpha_j}) \subseteq \bigcup_{j=1}^n V_{\alpha_j}.$$
    <2>7. Thus $\{V_{\alpha_1}, \dots, V_{\alpha_n}\}$ is a finite subcover of $f(X)$.
    <2>8. Therefore, $f(X)$ is a compact subset of $\mathbb{R}$.

<1>2. Step 2: Compact subsets of $\mathbb{R}$ are closed and bounded (Heine–Borel):
    *Proof:*
    <2>1. By the Heine–Borel Theorem in Euclidean space $\mathbb{R}$, every compact subset $K \subset \mathbb{R}$ is closed and bounded.
    <2>2. Since $f(X)$ is compact in $\mathbb{R}$, $f(X)$ is bounded: there exist $m_0, M_0 \in \mathbb{R}$ such that $m_0 \le f(x) \le M_0$ for all $x \in X$.

<1>3. Step 3: $f$ attains its minimum and maximum:
    *Proof:*
    <2>1. Since $f(X)$ is non-empty and bounded, the supremum $M = \sup f(X) = \sup_{x \in X} f(x)$ and infimum $m = \inf f(X) = \inf_{x \in X} f(x)$ exist as real numbers.
    <2>2. By definition of the supremum, for every $\varepsilon > 0$, there exists $y \in f(X)$ such that $M - \varepsilon < y \le M$. Thus $M \in \overline{f(X)}$ (the closure of $f(X)$).
    <2>3. Because $f(X)$ is compact, it is closed in $\mathbb{R}$, so $\overline{f(X)} = f(X)$.
    <2>4. Therefore $M \in f(X)$, which means there exists some point $x_{\max} \in X$ such that $f(x_{\max}) = M = \sup_{x \in X} f(x)$.
    <2>5. Similarly, $m \in \overline{f(X)} = f(X)$, so there exists $x_{\min} \in X$ such that $f(x_{\min}) = m = \inf_{x \in X} f(x)$.

<1>4. Conclusion:
    $f$ is bounded on $X$ and achieves its minimum at $x_{\min} \in X$ and its maximum at $x_{\max} \in X$. Q.E.D.
:::
