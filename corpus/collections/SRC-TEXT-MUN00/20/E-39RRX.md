---
schema: qual/card@1
id: E-39RRX
kind: exercise
title: Four topologies on l2 and the Hilbert cube
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be the subset of $\mathbb{R}^\omega$ consisting of all sequences $\mathbf{x}$ such that $\sum x_i^2$ converges.
Then the formula

$$
d(\mathbf{x}, \mathbf{y}) = \left[ \sum_{i=1}^{\infty} (x_i - y_i)^2 \right]^{1/2}
$$

defines a metric on $X$.
(See Exercise 10.) On $X$ we have the three topologies it inherits from the box, uniform, and product topologies on $\mathbb{R}^\omega$.
We have also the topology given by the metric $d$, which we call the $\ell^2$-topology.

(a) Show that on $X$, we have the inclusions

$$
\text{box topology} \supset \ell^2\text{-topology} \supset \text{uniform topology}.
$$

(b) The set $\mathbb{R}^\infty$ of all sequences that are eventually zero is contained in $X$.
Show that the four topologies that $\mathbb{R}^\infty$ inherits as a subspace of $X$ are all distinct.

(c) The set

$$
H = \prod_{n \in \mathbb{Z}_+} [0, 1/n]
$$

is contained in $X$; it is called the Hilbert cube.
Compare the four topologies that $H$ inherits as a subspace of $X$.
:::

::: solution
**Goal:** Analyze and compare the four topologies (box, $\ell^2$, uniform, product) on the Hilbert space $\ell^2$, on the subspace of finite sequences $\mathbb{R}^\infty$, and on the Hilbert cube $H$.

<1>1. Part (a): Inclusions on $X = \ell^2$.
    We have $\mathcal{T}_{\text{box}} \supset \mathcal{T}_d \supset \mathcal{T}_{\bar{\rho}} \supset \mathcal{T}_{\text{prod}}$.
    *Proof:*
    <2>1. $\mathcal{T}_{\bar{\rho}} \subseteq \mathcal{T}_d$: For any $\mathbf{x}, \mathbf{y} \in \ell^2$, $\bar{\rho}(\mathbf{x}, \mathbf{y}) = \sup_{i} \min\{|x_i - y_i|, 1\} \le \sup_i |x_i - y_i| \le \left(\sum_{i=1}^\infty (x_i - y_i)^2\right)^{1/2} = d(\mathbf{x}, \mathbf{y})$. Thus $B_d(\mathbf{x}, \varepsilon) \subseteq B_{\bar{\rho}}(\mathbf{x}, \varepsilon)$, showing every uniform-open set is $\ell^2$-open.
    <2>2. $\mathcal{T}_d \subseteq \mathcal{T}_{\text{box}}$: Given $\mathbf{x} \in \ell^2$ and $\varepsilon > 0$, set $\varepsilon_i = \frac{\varepsilon}{2^{(i+1)/2}}$. Then $\sum_{i=1}^\infty \varepsilon_i^2 = \varepsilon^2 \sum_{i=1}^\infty 2^{-(i+1)} = \frac{\varepsilon^2}{2} < \varepsilon^2$. The box neighborhood $U = \prod_{i=1}^\infty (x_i - \varepsilon_i, x_i + \varepsilon_i) \cap X$ satisfies $d(\mathbf{x}, \mathbf{y}) = \sqrt{\sum (x_i - y_i)^2} < \sqrt{\sum \varepsilon_i^2} < \varepsilon$ for all $\mathbf{y} \in U$, so $U \subseteq B_d(\mathbf{x}, \varepsilon)$.

<1>2. Part (b): Strict distinction on $\mathbb{R}^\infty$.
    The four subspace topologies satisfy $\mathcal{T}_{\text{prod}} \subsetneq \mathcal{T}_{\bar{\rho}} \subsetneq \mathcal{T}_d \subsetneq \mathcal{T}_{\text{box}}$ on $\mathbb{R}^\infty$.
    *Proof:*
    <2>1. $\mathcal{T}_{\text{prod}} \neq \mathcal{T}_{\bar{\rho}}$: The sequence $\mathbf{z}_n = \mathbf{e}_n = (0, \dots, 0, 1, 0, \dots)$ converges to $\mathbf{0}$ in the product topology (each coordinate is eventually 0), but $\bar{\rho}(\mathbf{z}_n, \mathbf{0}) = 1 \not\to 0$.
    <2>2. $\mathcal{T}_{\bar{\rho}} \neq \mathcal{T}_d$: The sequence $\mathbf{y}_n = (\frac{1}{\sqrt{n}}, \dots, \frac{1}{\sqrt{n}}, 0, \dots)$ ($n$ terms) has $\bar{\rho}(\mathbf{y}_n, \mathbf{0}) = \frac{1}{\sqrt{n}} \to 0$, so $\mathbf{y}_n \to \mathbf{0}$ in the uniform topology, but $d(\mathbf{y}_n, \mathbf{0}) = \sqrt{n \cdot \frac{1}{n}} = 1 \not\to 0$.
    <2>3. $\mathcal{T}_d \neq \mathcal{T}_{\text{box}}$: The sequence $\mathbf{w}_n = \frac{1}{n} \mathbf{e}_n$ has $d(\mathbf{w}_n, \mathbf{0}) = \frac{1}{n} \to 0$, so $\mathbf{w}_n \to \mathbf{0}$ in $\ell^2$. But for the box-open neighborhood $V = \prod_{i=1}^\infty (-\frac{1}{i^2}, \frac{1}{i^2}) \cap \mathbb{R}^\infty$, $(\mathbf{w}_n)_n = \frac{1}{n} > \frac{1}{n^2}$, so $\mathbf{w}_n \notin V$ for all $n \ge 2$, so $\mathbf{w}_n \not\to \mathbf{0}$ in the box topology.

<1>3. Part (c): Comparison on the Hilbert cube $H = \prod_{n=1}^\infty [0, 1/n]$.
    On $H$, $\mathcal{T}_{\text{prod}} = \mathcal{T}_{\bar{\rho}} = \mathcal{T}_d \subsetneq \mathcal{T}_{\text{box}}$.
    *Proof:*
    <2>1. By Tychonoff's Theorem, $H$ is compact in the product topology $\mathcal{T}_{\text{prod}}$.
    <2>2. Since $H \subset \ell^2$, for any $\mathbf{x}, \mathbf{y} \in H$ and any $N \in \mathbb{Z}_+$:
        $$d(\mathbf{x}, \mathbf{y})^2 = \sum_{i=1}^N (x_i - y_i)^2 + \sum_{i=N+1}^\infty (x_i - y_i)^2 \le \sum_{i=1}^N (x_i - y_i)^2 + \sum_{i=N+1}^\infty \frac{1}{i^2}.$$
    <2>3. Given $\varepsilon > 0$, choose $N$ such that $\sum_{i=N+1}^\infty \frac{1}{i^2} < \frac{\varepsilon^2}{2}$. The basic product open set $W = \{\mathbf{y} \in H : |y_i - x_i| < \frac{\varepsilon}{\sqrt{2N}} \text{ for } 1 \le i \le N\}$ satisfies $d(\mathbf{x}, \mathbf{y}) < \varepsilon$.
    <2>4. Thus $\mathcal{T}_d \subseteq \mathcal{T}_{\text{prod}}$ on $H$. Combined with <1>1, $\mathcal{T}_{\text{prod}} = \mathcal{T}_{\bar{\rho}} = \mathcal{T}_d$ on $H$.
    <2>5. The box topology is strictly finer: $U = \prod_{n=1}^\infty [0, \frac{1}{n^2}) \cap H$ is box-open, but contains no product basic open neighborhood of $\mathbf{0}$ (which can only restrict finitely many coordinates). Q.E.D.
:::
