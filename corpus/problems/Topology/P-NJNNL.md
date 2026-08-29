---
schema: qual/card@1
id: P-NJNNL
kind: problem
title: Continuous images of compact spaces, and compact metric spaces are complete
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) Let $X$ and $Y$ be topological spaces, and let $f: X \to Y$ be a continuous map.
Prove that if $X$ is **compact**, then its image $f(X) \subseteq Y$ is compact.
(2) Let $(X, d)$ be a metric space.
Prove that if $X$ is **compact**, then $(X, d)$ is **complete** (every Cauchy sequence in $X$ converges to a limit in $X$).
:::

::: solution
**Goal:** Prove that continuous images preserve compactness (via open covers) and that compact metric spaces are complete (via convergent subsequences).

<1>1. Part 1: Continuous Images of Compact Spaces are Compact:
    *Proof:*
    <2>1. Let $\{V_\alpha\}_{\alpha \in A}$ be an arbitrary **open cover** of the image $f(X)$ in $Y$, so:
        $$f(X) \subseteq \bigcup_{\alpha \in A} V_\alpha$$
        where each $V_\alpha \subseteq Y$ is open in $Y$.
    <2>2. For each $\alpha \in A$, since $f: X \to Y$ is continuous, the preimage:
        $$U_\alpha \coloneqq f^{-1}(V_\alpha)$$
        is an **open subset** of $X$.
    <2>3. We check that $\{U_\alpha\}_{\alpha \in A}$ covers $X$:
        $$X = f^{-1}(f(X)) \subseteq f^{-1}\left(\bigcup_{\alpha \in A} V_\alpha\right) = \bigcup_{\alpha \in A} f^{-1}(V_\alpha) = \bigcup_{\alpha \in A} U_\alpha.$$
    <2>4. Thus $\{U_\alpha\}_{\alpha \in A}$ is an open cover of $X$.
    <2>5. Since $X$ is **compact**, there exists a **finite subcover**: there exist finitely many indices $\alpha_1, \alpha_2, \dots, \alpha_n \in A$ such that:
        $$X \subseteq U_{\alpha_1} \cup U_{\alpha_2} \cup \cdots \cup U_{\alpha_n}.$$
    <2>6. Applying $f$ to both sides:
        $$f(X) \subseteq f\left(\bigcup_{i=1}^n U_{\alpha_i}\right) = \bigcup_{i=1}^n f(U_{\alpha_i}) = \bigcup_{i=1}^n f(f^{-1}(V_{\alpha_i})) \subseteq \bigcup_{i=1}^n V_{\alpha_i}.$$
    <2>7. Thus $\{V_{\alpha_1}, \dots, V_{\alpha_n}\}$ is a finite subcover of $f(X)$.
    <2>8. Since every open cover has a finite subcover, $f(X)$ is **compact**.

<1>2. Part 2: Compact Metric Spaces are Complete:
    *Proof:*
    <2>1. Let $(x_n)_{n=1}^\infty$ be an arbitrary **Cauchy sequence** in the metric space $(X, d)$.
    <2>2. **Sequential Compactness:**
        Since $(X, d)$ is a compact metric space, it is **sequentially compact**: every sequence in $X$ has a **convergent subsequence**.
    <2>3. Therefore, there exists a subsequence $(x_{n_k})_{k=1}^\infty$ converging to some point $x \in X$:
        $$\lim_{k \to \infty} x_{n_k} = x.$$
    <2>4. **Full Sequence Convergence from Cauchy Property:**
        Let $\varepsilon > 0$ be given.
        - Since $(x_n)$ is Cauchy, there exists $N_1 \in \mathbb{N}$ such that for all $n, m \ge N_1$:
          $$d(x_n, x_m) < \frac{\varepsilon}{2}.$$
        - Since $x_{n_k} \to x$, there exists $K \in \mathbb{N}$ such that for all $k \ge K$, $n_k \ge N_1$ and:
          $$d(x_{n_k}, x) < \frac{\varepsilon}{2}.$$
    <2>5. For any $n \ge N_1$, choosing $k \ge K$ so that $n_k \ge N_1$:
        $$d(x_n, x) \le d(x_n, x_{n_k}) + d(x_{n_k}, x) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
    <2>6. Thus $\lim_{n \to \infty} x_n = x \in X$.
    <2>7. Since every Cauchy sequence converges to a limit in $X$, $(X, d)$ is **complete**.

<1>3. Conclusion:
    $f(X)$ is compact by pullback of open covers, and compact metric spaces are complete because Cauchy sequences with convergent subsequences converge. Q.E.D.
:::
