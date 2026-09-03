---
schema: qual/card@1
id: E-GDB6T
kind: problem
title: Compact Hausdorff spaces are metrizable if and only if second-countable
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Countability
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
Show that a compact Hausdorff space is metrizable if and only if it is second-countable.
:::

::: solution
**Goal:** Prove that a compact Hausdorff space $X$ is metrizable if and only if it has a countable basis (second-countable).

<1>1. Forward direction: Compact and metrizable $\implies$ second-countable.
    *Proof:*
    <2>1. Let $(X, d)$ be a compact metric space.
    <2>2. For each positive integer $m \in \mathbb{N}$, the collection of open balls $\{B(x, 1/m) : x \in X\}$ is an open cover of $X$.
    <2>3. By compactness of $X$, there exists a finite set of points $D_m = \{x_{m,1}, x_{m,2}, \dots, x_{m,k_m}\} \subset X$ such that
    $$X = \bigcup_{i=1}^{k_m} B(x_{m,i}, 1/m).$$
    <2>4. Define $\mathcal{B} = \bigcup_{m=1}^\infty \{B(x_{m,i}, 1/m) : 1 \le i \le k_m\}$. As a countable union of finite sets, $\mathcal{B}$ is countable.
    <2>5. We show $\mathcal{B}$ is a basis: let $U \subseteq X$ be open and $x \in U$. Choose $r > 0$ such that $B(x, r) \subseteq U$, and choose $m \in \mathbb{N}$ with $1/m < r/2$.
    <2>6. Since $D_m$ covers $X$, there is some $x_{m,i} \in D_m$ with $x \in B(x_{m,i}, 1/m)$.
    <2>7. For any $y \in B(x_{m,i}, 1/m)$, the triangle inequality gives
    $$d(y, x) \le d(y, x_{m,i}) + d(x_{m,i}, x) < \frac{1}{m} + \frac{1}{m} = \frac{2}{m} < r,$$
    so $x \in B(x_{m,i}, 1/m) \subseteq B(x, r) \subseteq U$.
    <2>8. Thus $\mathcal{B}$ is a countable basis for the topology of $X$, so $X$ is second-countable.

<1>2. Backward direction: Compact Hausdorff and second-countable $\implies$ metrizable.
    *Proof:*
    <2>1. Every compact Hausdorff space is normal ($T_4$).
    *Proof of normality:* For any closed set $F \subset X$ and point $y \notin F$, since $X$ is Hausdorff, each $x \in F$ has disjoint open neighborhoods $U_x \ni x$ and $V_x \ni y$. By compactness of $F$, finitely many $U_{x_i}$ cover $F$, and $\bigcap V_{x_i}$ is an open neighborhood of $y$ disjoint from $\bigcup U_{x_i}$. Repeating this argument for two disjoint closed sets separates them by disjoint open neighborhoods.
    <2>2. Every normal $T_1$ space is regular ($T_3$).
    <2>3. By the Urysohn Metrization Theorem, every second-countable regular space is metrizable.
    <2>4. Therefore $X$ is metrizable.

<1>3. Conclusion:
    *Proof:*
    By <1>1 and <1>2, a compact Hausdorff space is metrizable if and only if it is second-countable.
:::
