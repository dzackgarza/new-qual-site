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

::: {.exercise}
Show that a compact Hausdorff space is metrizable if and only if it is second-countable.
:::

::: {.solution}
**Goal:** Prove that a compact Hausdorff space $X$ is metrizable if and only if it has a countable basis (second-countable).

::: pf

::: pf-step

Forward direction: Compact and metrizable $\implies$ second-countable.
    *Proof:*

::: pf-proof

::: pf-step

Let $(X, d)$ be a compact metric space.

:::

::: pf-step

For each positive integer $m \in \mathbb{N}$, the collection of open balls $\{B(x, 1/m) : x \in X\}$ is an open cover of $X$.

:::

::: pf-step

By compactness of $X$, there exists a finite set of points $D_m = \{x_{m,1}, x_{m,2}, \dots, x_{m,k_m}\} \subset X$ such that
    $$X = \bigcup_{i=1}^{k_m} B(x_{m,i}, 1/m).$$

:::

::: pf-step

Define $\mathcal{B} = \bigcup_{m=1}^\infty \{B(x_{m,i}, 1/m) : 1 \le i \le k_m\}$. As a countable union of finite sets, $\mathcal{B}$ is countable.

:::

::: pf-step

We show $\mathcal{B}$ is a basis: let $U \subseteq X$ be open and $x \in U$. Choose $r > 0$ such that $B(x, r) \subseteq U$, and choose $m \in \mathbb{N}$ with $1/m < r/2$.

:::

::: pf-step

Since $D_m$ covers $X$, there is some $x_{m,i} \in D_m$ with $x \in B(x_{m,i}, 1/m)$.

:::

::: pf-step

For any $y \in B(x_{m,i}, 1/m)$, the triangle inequality gives
    $$d(y, x) \le d(y, x_{m,i}) + d(x_{m,i}, x) < \frac{1}{m} + \frac{1}{m} = \frac{2}{m} < r,$$
    so $x \in B(x_{m,i}, 1/m) \subseteq B(x, r) \subseteq U$.

:::

::: pf-step

Thus $\mathcal{B}$ is a countable basis for the topology of $X$, so $X$ is second-countable.

:::

:::

:::

::: pf-step

Backward direction: Compact Hausdorff and second-countable $\implies$ metrizable.
    *Proof:*

::: pf-proof

::: pf-step

Every compact Hausdorff space is normal ($T_4$).
    *Proof of normality:* For any closed set $F \subset X$ and point $y \notin F$, since $X$ is Hausdorff, each $x \in F$ has disjoint open neighborhoods $U_x \ni x$ and $V_x \ni y$. By compactness of $F$, finitely many $U_{x_i}$ cover $F$, and $\bigcap V_{x_i}$ is an open neighborhood of $y$ disjoint from $\bigcup U_{x_i}$. Repeating this argument for two disjoint closed sets separates them by disjoint open neighborhoods.

:::

::: pf-step

Every normal $T_1$ space is regular ($T_3$).

:::

::: pf-step

By the Urysohn Metrization Theorem, every second-countable regular space is metrizable.

:::

::: pf-step

Therefore $X$ is metrizable.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    *Proof:*
    By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, a compact Hausdorff space is metrizable if and only if it is second-countable.
:::
