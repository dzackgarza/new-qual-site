---
schema: qual/card@1
id: E-0GM3H
kind: exercise
title: The fine topology on function spaces
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $(Y, d)$ be a metric space; let $X$ be a space.
Define a topology on $\mathcal{C}(X, Y)$ as follows.
Given $f \in \mathcal{C}(X, Y)$, and given a positive continuous function $\delta: X \to \mathbb{R}_+$ on $X$, let

$$
B(f, \delta) = \ts{g \mid d(f(x), g(x)) < \delta(x) \text{ for all } x \in X}.
$$

(a) Show that the sets $B(f, \delta)$ form a basis for a topology on $\mathcal{C}(X, Y)$.
We call it the fine topology.

(b) Show that the fine topology contains the uniform topology.

(c) Show that if $X$ is compact, the fine and uniform topologies agree.

(d) Show that if $X$ is discrete, then $\mathcal{C}(X, Y) = Y^X$ and the fine and box topologies agree.
:::

::: solution
**Goal:** Prove the foundational properties of the fine topology on the function space $\mathcal{C}(X, Y)$ and compare it with the uniform and box topologies.

<1>1. Part (a): The sets $\mathcal{B} = \{B(f, \delta) : f \in \mathcal{C}(X, Y), \delta \in \mathcal{C}(X, \mathbb{R}_+)\}$ form a basis.
    *Proof:*
    <2>1. Covering: For any $f \in \mathcal{C}(X, Y)$, the constant function $\delta_1(x) = 1$ is continuous and positive, and $d(f(x), f(x)) = 0 < 1$ for all $x$, so $f \in B(f, \delta_1)$.
    <2>2. Intersection: Let $g \in B(f_1, \delta_1) \cap B(f_2, \delta_2)$.
    <2>3. For each $x \in X$, $d(f_1(x), g(x)) < \delta_1(x)$ and $d(f_2(x), g(x)) < \delta_2(x)$.
    <2>4. Define $\delta_3: X \to \mathbb{R}_+$ by:
        $$\delta_3(x) = \min\{\delta_1(x) - d(f_1(x), g(x)), \; \delta_2(x) - d(f_2(x), g(x))\}.$$
    <2>5. Since $f_1, f_2, g, \delta_1, \delta_2$ and the metric $d$ are continuous, the map $x \mapsto d(f_i(x), g(x))$ is continuous on $X$. Hence $\delta_3$ is continuous and strictly positive everywhere ($\delta_3(x) > 0$).
    <2>6. For any $h \in B(g, \delta_3)$ and each $x \in X$, the triangle inequality gives:
        $$d(f_1(x), h(x)) \le d(f_1(x), g(x)) + d(g(x), h(x)) < d(f_1(x), g(x)) + (\delta_1(x) - d(f_1(x), g(x))) = \delta_1(x).$$
    <2>7. Thus $h \in B(f_1, \delta_1)$. Similarly $h \in B(f_2, \delta_2)$.
    <2>8. Hence $g \in B(g, \delta_3) \subseteq B(f_1, \delta_1) \cap B(f_2, \delta_2)$, proving that $\mathcal{B}$ is a basis.

<1>2. Part (b): The fine topology contains the uniform topology.
    *Proof:*
    <2>1. A standard basis element for the uniform topology is a metric ball $B_{\bar{\rho}}(f, \varepsilon) = \{g \in \mathcal{C}(X, Y) : \sup_{x \in X} d(f(x), g(x)) < \varepsilon\}$ for constant $\varepsilon > 0$ (assuming $\varepsilon \le 1$).
    <2>2. Choosing the constant function $\delta(x) = \varepsilon$ for all $x \in X$, $\delta$ is continuous and positive, and $B(f, \delta) = B_{\bar{\rho}}(f, \varepsilon)$.
    <2>3. Thus every basic open set in the uniform topology is an element of the basis $\mathcal{B}$, so the fine topology contains the uniform topology.

<1>3. Part (c): If $X$ is compact, the fine and uniform topologies coincide.
    *Proof:*
    <2>1. By <1>2, the fine topology is at least as fine as the uniform topology.
    <2>2. Conversely, let $B(f, \delta)$ be a basic open set in the fine topology.
    <2>3. Since $X$ is compact and $\delta: X \to (0, \infty)$ is continuous, the Extreme Value Theorem guarantees that $\delta$ attains its minimum:
        $$\varepsilon := \inf_{x \in X} \delta(x) = \min_{x \in X} \delta(x) > 0.$$
    <2>4. If $g \in B_{\bar{\rho}}(f, \varepsilon)$, then for all $x \in X$, $d(f(x), g(x)) < \varepsilon \le \delta(x)$, which implies $g \in B(f, \delta)$.
    <2>5. Thus $B_{\bar{\rho}}(f, \varepsilon) \subseteq B(f, \delta)$, proving that every fine-open set is uniform-open.

<1>4. Part (d): If $X$ is discrete, $\mathcal{C}(X, Y) = Y^X$ and the fine topology equals the box topology.
    *Proof:*
    <2>1. When $X$ is discrete, every map $f: X \to Y$ is continuous, so $\mathcal{C}(X, Y) = Y^X$.
    <2>2. Furthermore, every function $\delta: X \to \mathbb{R}_+$ is continuous.
    <2>3. A basic open set in the box topology on $\prod_{x \in X} Y$ containing $f$ is $\prod_{x \in X} B_d(f(x), \varepsilon_x)$ for an arbitrary collection of positive numbers $(\varepsilon_x)_{x \in X}$.
    <2>4. Defining $\delta(x) = \varepsilon_x$ for each $x \in X$, $\delta$ is a continuous positive function on the discrete space $X$, and $B(f, \delta) = \prod_{x \in X} B_d(f(x), \varepsilon_x)$.
    <2>5. Hence the bases for the fine topology and the box topology are identical. Q.E.D.
:::
