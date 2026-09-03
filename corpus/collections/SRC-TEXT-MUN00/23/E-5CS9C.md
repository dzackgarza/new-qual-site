---
schema: qual/card@1
id: E-5CS9C
kind: problem
title: R^omega in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Determine whether or not $\mathbb{R}^\omega$ is connected in the uniform topology.
:::

::: solution
**Goal:** Prove that $\mathbb{R}^\omega$ is **not connected** (is disconnected) in the uniform topology by constructing a non-trivial clopen subset.

<1>1. Definition of the uniform metric:
    The uniform topology on $\mathbb{R}^\omega$ is induced by the metric:
    $$\bar{\rho}(\mathbf{x}, \mathbf{y}) = \sup_{n \in \mathbb{Z}_+} \bar{d}(x_n, y_n), \quad \text{where } \bar{d}(a, b) = \min\{|a - b|, 1\}.$$

<1>2. Candidate clopen subset:
    Let $\mathcal{B} \subset \mathbb{R}^\omega$ be the subspace of all bounded sequences:
    $$\mathcal{B} = \left\{ \mathbf{x} = (x_n)_{n=1}^\infty \in \mathbb{R}^\omega \;\middle|\; \sup_{n \in \mathbb{Z}_+} |x_n| < \infty \right\}.$$

<1>3. $\mathcal{B}$ is an open subset of $\mathbb{R}^\omega$:
    *Proof:*
    <2>1. Let $\mathbf{x} \in \mathcal{B}$, so there exists $M < \infty$ with $|x_n| \le M$ for all $n \in \mathbb{Z}_+$.
    <2>2. Consider the open ball $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$.
    <2>3. For any $\mathbf{y} \in B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2})$, we have $\sup_{n} \bar{d}(x_n, y_n) < \frac{1}{2} < 1$, which forces $|x_n - y_n| < \frac{1}{2}$ for all $n \in \mathbb{Z}_+$.
    <2>4. By the triangle inequality, $|y_n| \le |x_n| + |y_n - x_n| < M + \frac{1}{2}$ for all $n \in \mathbb{Z}_+$.
    <2>5. Thus $\sup_n |y_n| \le M + \frac{1}{2} < \infty$, which means $\mathbf{y} \in \mathcal{B}$.
    <2>6. Hence $B_{\bar{\rho}}(\mathbf{x}, \frac{1}{2}) \subseteq \mathcal{B}$, so $\mathcal{B}$ is open in the uniform topology.

<1>4. $\mathcal{B}$ is a closed subset of $\mathbb{R}^\omega$:
    *Proof:*
    <2>1. Two sequences $\mathbf{x}, \mathbf{y} \in \mathbb{R}^\omega$ are equivalent ($\mathbf{x} \sim \mathbf{y}$) if $\sup_n |x_n - y_n| < \infty$.
    <2>2. By the same reasoning as in <1>3, for any $\mathbf{x} \in \mathbb{R}^\omega$, the equivalence class $[\mathbf{x}] = \{\mathbf{y} \in \mathbb{R}^\omega \mid \mathbf{x} \sim \mathbf{y}\}$ is an open subset of $\mathbb{R}^\omega$.
    <2>3. The complement $\mathbb{R}^\omega \setminus \mathcal{B} = \bigcup_{[\mathbf{x}] \neq \mathcal{B}} [\mathbf{x}]$ is a union of open equivalence classes, hence open.
    <2>4. Thus $\mathcal{B}$ is closed in the uniform topology.

<1>5. Conclusion:
    - $\mathcal{B}$ is non-empty (since $\mathbf{0} \in \mathcal{B}$).
    - $\mathbb{R}^\omega \setminus \mathcal{B}$ is non-empty (since the sequence $(1, 2, 3, \dots) \in \mathbb{R}^\omega \setminus \mathcal{B}$).
    - Thus $\mathcal{B}$ is a non-trivial clopen subset of $\mathbb{R}^\omega$, proving that $\mathbb{R}^\omega$ is **not connected** in the uniform topology. Q.E.D.
:::
