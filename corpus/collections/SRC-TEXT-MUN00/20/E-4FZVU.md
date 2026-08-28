---
schema: qual/card@1
id: E-4FZVU
kind: exercise
title: Continuity and convergence in the product, uniform, and box topologies
classification:
  areas:
  - topology
  topics:
  - Convergence
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the product, uniform, and box topologies on $\mathbb{R}^\omega$.

(a) In which topologies are the following functions from $\mathbb{R}$ to $\mathbb{R}^\omega$ continuous?

$$
\begin{array}{l}
f(t) = (t, 2t, 3t, \ldots), \\
g(t) = (t, t, t, \ldots), \\
h(t) = (t, \tfrac{1}{2}t, \tfrac{1}{3}t, \ldots).
\end{array}
$$

(b) In which topologies do the following sequences converge?

$$
\mathbf{w}_1 = (1, 1, 1, 1, \dots), \quad \mathbf{x}_1 = (1, 1, 1, 1, \dots),
$$

$$
\mathbf{w}_2 = (0, 2, 2, 2, \dots), \quad \mathbf{x}_2 = (0, \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, \dots),
$$

$$
\mathbf{w}_3 = (0, 0, 3, 3, \dots), \quad \mathbf{x}_3 = (0, 0, \tfrac{1}{3}, \tfrac{1}{3}, \dots),
$$

$$
\mathbf{y}_1 = (1, 0, 0, 0, \dots), \quad \mathbf{z}_1 = (1, 1, 0, 0, \dots),
$$

$$
\mathbf{y}_2 = (\tfrac{1}{2}, \tfrac{1}{2}, 0, 0, \dots), \quad \mathbf{z}_2 = (\tfrac{1}{2}, \tfrac{1}{2}, 0, 0, \dots),
$$

$$
\mathbf{y}_3 = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}, 0, \dots), \quad \mathbf{z}_3 = (\tfrac{1}{3}, \tfrac{1}{3}, 0, 0, \dots).
$$
:::

::: solution
**Goal:** Determine the continuity of functions $f, g, h: \mathbb{R} \to \mathbb{R}^\omega$ and the convergence of sequences $(\mathbf{w}_n), (\mathbf{x}_n), (\mathbf{y}_n), (\mathbf{z}_n)$ in the product, uniform, and box topologies on $\mathbb{R}^\omega$.

<1>1. Part (a): Continuity of functions.
    *Proof:*
    <2>1. **$f(t) = (t, 2t, 3t, \dots)$:**
        - *Product topology:* Each coordinate function $f_n(t) = nt$ is continuous on $\mathbb{R}$, so $f$ is continuous.
        - *Uniform topology:* For $t \neq 0$, $\bar{\rho}(f(t), f(0)) = \min\{\sup_{n \ge 1} |nt|, 1\} = 1$. As $t \to 0$, $\bar{\rho}(f(t), f(0)) = 1 \not\to 0$, so $f$ is discontinuous.
        - *Box topology:* Since box topology is finer than uniform topology, $f$ is also discontinuous in the box topology.
        - *Conclusion:* $f$ is continuous **only in the product topology**.
    <2>2. **$g(t) = (t, t, t, \dots)$:**
        - *Product topology:* Coordinate functions $g_n(t) = t$ are continuous, so $g$ is continuous.
        - *Uniform topology:* $\bar{\rho}(g(t), g(s)) = \min\{|t - s|, 1\} \to 0$ as $t \to s$, so $g$ is continuous.
        - *Box topology:* For the box-open neighborhood $U = \prod_{n=1}^\infty (-\frac{1}{n}, \frac{1}{n})$ of $\mathbf{0}$, $g(t) \in U \iff |t| < \frac{1}{n}$ for all $n \ge 1 \iff t = 0$. Thus $g^{-1}(U) = \{0\}$, which is not open in $\mathbb{R}$.
        - *Conclusion:* $g$ is continuous **in the product and uniform topologies, but not in the box topology**.
    <2>3. **$h(t) = (t, \frac{1}{2}t, \frac{1}{3}t, \dots)$:**
        - *Product topology:* Each $h_n(t) = \frac{t}{n}$ is continuous, so $h$ is continuous.
        - *Uniform topology:* $\bar{\rho}(h(t), h(s)) = \min\{\sup_{n \ge 1} \frac{|t-s|}{n}, 1\} = \min\{|t-s|, 1\} \to 0$ as $t \to s$, so $h$ is continuous.
        - *Box topology:* For $V = \prod_{n=1}^\infty (-\frac{1}{n^2}, \frac{1}{n^2})$, $h(t) \in V \iff |\frac{t}{n}| < \frac{1}{n^2}$ for all $n \iff |t| < \frac{1}{n}$ for all $n \iff t = 0$. Thus $h^{-1}(V) = \{0\}$, so $h$ is not continuous in the box topology.
        - *Conclusion:* $h$ is continuous **in the product and uniform topologies, but not in the box topology**.

<1>2. Part (b): Convergence of sequences (all have potential limit $\mathbf{0}$).
    *Proof:*
    <2>1. **$\mathbf{w}_n = (0, \dots, 0, n, n, n, \dots)$ ($n-1$ leading zeros):**
        - *Product topology:* For each fixed coordinate $k$, $(\mathbf{w}_n)_k = 0$ for all $n > k$, so $(\mathbf{w}_n)_k \to 0$. Thus $\mathbf{w}_n \to \mathbf{0}$.
        - *Uniform & Box topologies:* $\bar{\rho}(\mathbf{w}_n, \mathbf{0}) = \min\{\sup_{k \ge n} n, 1\} = 1 \not\to 0$.
        - *Conclusion:* Converges to $\mathbf{0}$ **only in the product topology**.
    <2>2. **$\mathbf{x}_n = (0, \dots, 0, \frac{1}{n}, \frac{1}{n}, \dots)$ ($n-1$ leading zeros):**
        - *Product topology:* $(\mathbf{x}_n)_k = 0$ for $n > k$, so $\mathbf{x}_n \to \mathbf{0}$.
        - *Uniform topology:* $\bar{\rho}(\mathbf{x}_n, \mathbf{0}) = \frac{1}{n} \to 0$, so $\mathbf{x}_n \to \mathbf{0}$.
        - *Box topology:* For $U = \prod_{k=1}^\infty (-\frac{1}{k^2}, \frac{1}{k^2})$, $(\mathbf{x}_n)_n = \frac{1}{n} > \frac{1}{n^2}$, so $\mathbf{x}_n \notin U$ for all $n \ge 2$, so $\mathbf{x}_n \not\to \mathbf{0}$.
        - *Conclusion:* Converges to $\mathbf{0}$ **in the product and uniform topologies, but not in the box topology**.
    <2>3. **$\mathbf{y}_n = (\frac{1}{n}, \dots, \frac{1}{n}, 0, 0, \dots)$ ($n$ non-zero terms):**
        - *Product topology:* $(\mathbf{y}_n)_k = \frac{1}{n} \to 0$ for all $n \ge k$, so $\mathbf{y}_n \to \mathbf{0}$.
        - *Uniform topology:* $\bar{\rho}(\mathbf{y}_n, \mathbf{0}) = \frac{1}{n} \to 0$, so $\mathbf{y}_n \to \mathbf{0}$.
        - *Box topology:* For $U = \prod_{k=1}^\infty (-\frac{1}{k^2}, \frac{1}{k^2})$, $(\mathbf{y}_n)_n = \frac{1}{n} > \frac{1}{n^2}$, so $\mathbf{y}_n \notin U$ for all $n \ge 2$.
        - *Conclusion:* Converges to $\mathbf{0}$ **in the product and uniform topologies, but not in the box topology**.
    <2>4. **$\mathbf{z}_n = (\frac{1}{n}, \frac{1}{n}, 0, 0, \dots)$ (exactly 2 non-zero terms):**
        - *Product & Uniform topologies:* $\bar{\rho}(\mathbf{z}_n, \mathbf{0}) = \frac{1}{n} \to 0$, so converges to $\mathbf{0}$.
        - *Box topology:* Let $V = \prod_{k=1}^\infty (-a_k, a_k)$ be an arbitrary box neighborhood of $\mathbf{0}$ ($a_k > 0$). Since $(\mathbf{z}_n)_k = 0 \in (-a_k, a_k)$ for all $k \ge 3$, $\mathbf{z}_n \in V \iff \frac{1}{n} < \min\{a_1, a_2\}$, which holds for all $n > \max\{1/a_1, 1/a_2\}$. Thus $\mathbf{z}_n \to \mathbf{0}$ in the box topology.
        - *Conclusion:* Converges to $\mathbf{0}$ **in all three topologies (product, uniform, and box)**. Q.E.D.
:::
