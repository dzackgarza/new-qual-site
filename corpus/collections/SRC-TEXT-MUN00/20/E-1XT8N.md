---
schema: qual/card@1
id: E-1XT8N
kind: exercise
title: Continuity of the affine map in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the map $h: \mathbb{R}^\omega \to \mathbb{R}^\omega$ defined in Exercise 8 of §19; give $\mathbb{R}^\omega$ the uniform topology.
Under what conditions on the numbers $a_i$ and $b_i$ is $h$ continuous?
a homeomorphism?
:::

::: solution
**Goal:** Determine the precise necessary and sufficient conditions on the coefficients $(a_i)_{i=1}^\infty$ and $(b_i)_{i=1}^\infty$ for the affine coordinate map $h(\mathbf{x}) = (a_i x_i + b_i)_{i=1}^\infty$ on $(\mathbb{R}^\omega, \bar{\rho})$ to be continuous and to be a homeomorphism.

<1>1. Metric on $\mathbb{R}^\omega$:
    The uniform topology is induced by the uniform metric:
    $$\bar{\rho}(\mathbf{x}, \mathbf{y}) = \sup_{i \in \mathbb{Z}_+} \bar{d}(x_i, y_i) = \sup_{i \in \mathbb{Z}_+} \min\{|x_i - y_i|, 1\}.$$
    Translation by any sequence $\mathbf{b} = (b_i)_{i=1}^\infty$ is an isometry of $(\mathbb{R}^\omega, \bar{\rho})$:
    $$\bar{\rho}(\mathbf{x} + \mathbf{b}, \mathbf{y} + \mathbf{b}) = \sup_{i \in \mathbb{Z}_+} \min\{|(x_i + b_i) - (y_i + b_i)|, 1\} = \bar{\rho}(\mathbf{x}, \mathbf{y}).$$
    Hence the sequence $(b_i)$ imposes no restrictions on continuity or homeomorphism properties.

<1>2. Condition for continuity: $h$ is continuous if and only if the sequence $(a_i)$ is bounded ($\sup_{i \in \mathbb{Z}_+} |a_i| < \infty$).
    *Proof:*
    <2>1. Sufficiency ($\impliedby$):
        - Suppose $M = \sup_{i \in \mathbb{Z}_+} |a_i| < \infty$.
        - If $M = 0$, $h(\mathbf{x}) = \mathbf{b}$ is constant, hence continuous.
        - If $M > 0$, let $\varepsilon > 0$ (assume $\varepsilon \le 1$). Choose $\delta = \frac{\varepsilon}{M} > 0$.
        - If $\bar{\rho}(\mathbf{x}, \mathbf{y}) < \min\{\delta, 1\}$, then $|x_i - y_i| < \delta$ for all $i \in \mathbb{Z}_+$.
        - Then $|(a_i x_i + b_i) - (a_i y_i + b_i)| = |a_i| |x_i - y_i| \le M \delta = \varepsilon \le 1$.
        - Thus $\bar{\rho}(h(\mathbf{x}), h(\mathbf{y})) = \sup_i |a_i (x_i - y_i)| \le \varepsilon$.
        - Hence $h$ is continuous (in fact, Lipschitz continuous).
    <2>2. Necessity ($\implies$):
        - Suppose $(a_i)$ is unbounded.
        - Let $\varepsilon = \frac{1}{2}$. For any $\delta > 0$, choose an index $k \in \mathbb{Z}_+$ such that $|a_k| > \frac{1}{\delta}$.
        - Define $\mathbf{x} = \mathbf{0}$ and $\mathbf{y} = (0, \dots, 0, \frac{\delta}{2}, 0, \dots)$ where the non-zero entry is in the $k$-th position.
        - Then $\bar{\rho}(\mathbf{x}, \mathbf{y}) = \frac{\delta}{2} < \delta$.
        - However, the $k$-th coordinate difference of the images satisfies:
          $$|a_k y_k - a_k x_k| = |a_k| \frac{\delta}{2} > \frac{1}{\delta} \cdot \frac{\delta}{2} = \frac{1}{2} = \varepsilon.$$
        - Thus $\bar{\rho}(h(\mathbf{x}), h(\mathbf{y})) \ge \min\{|a_k| \frac{\delta}{2}, 1\} > \frac{1}{2} = \varepsilon$.
        - Hence $h$ is not continuous at $\mathbf{0}$.

<1>3. Condition for homeomorphism: $h$ is a homeomorphism if and only if there exist constants $m, M > 0$ such that $0 < m \le |a_i| \le M < \infty$ for all $i \in \mathbb{Z}_+$.
    *Proof:*
    <2>1. Bijectivity: $h$ is bijective if and only if each coordinate map $x_i \mapsto a_i x_i + b_i$ is bijective on $\mathbb{R}$, which holds if and only if $a_i \neq 0$ for all $i \in \mathbb{Z}_+$.
    <2>2. Inverse map: When $a_i \neq 0$ for all $i$, the inverse is $h^{-1}(\mathbf{y}) = (\frac{1}{a_i} y_i - \frac{b_i}{a_i})_{i=1}^\infty$.
    <2>3. By <1>2, $h$ is continuous if and only if $\sup_{i} |a_i| \le M < \infty$.
    <2>4. By <1>2 applied to $h^{-1}$, $h^{-1}$ is continuous if and only if $\sup_{i} |\frac{1}{a_i}| < \infty$, which is equivalent to $\inf_{i} |a_i| \ge m > 0$.
    <2>5. Therefore $h$ is a homeomorphism if and only if the sequence $(a_i)$ is bounded and bounded away from zero. Q.E.D.
:::
