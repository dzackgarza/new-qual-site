---
schema: qual/card@1
id: E-4PQ1O
kind: problem
title: Coordinatewise convergence of nets in products
classification:
  areas:
  - topology
  topics:
  - Nets
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Suppose that

$$
(x_\alpha)_{\alpha \in J} \to x \text{ in } X \quad \text{and} \quad (y_\alpha)_{\alpha \in J} \to y \text{ in } Y.
$$

Show that $(x_\alpha \times y_\alpha) \to x \times y$ in $X \times Y$.
:::

::: solution
**Goal:** Prove that if nets $(x_\alpha)_{\alpha \in J}$ and $(y_\alpha)_{\alpha \in J}$ indexed by the same directed set $(J, \succeq)$ converge to $x \in X$ and $y \in Y$ respectively, then the product net $(x_\alpha, y_\alpha)_{\alpha \in J}$ converges to $(x, y)$ in the product topology on $X \times Y$.

<1>1. Setting and open neighborhood reduction:
    Let $W \subseteq X \times Y$ be an arbitrary open neighborhood of $(x, y)$.
    By definition of the product topology, there exist open neighborhoods $U \subseteq X$ of $x$ and $V \subseteq Y$ of $y$ such that:
    $$(x, y) \in U \times V \subseteq W.$$

<1>2. Eventual membership in coordinate components:
    *Proof:*
    <2>1. Since $x_\alpha \to x$ and $U$ is an open neighborhood of $x$, there exists $\alpha_1 \in J$ such that:
        $$\alpha \succeq \alpha_1 \implies x_\alpha \in U.$$
    <2>2. Since $y_\alpha \to y$ and $V$ is an open neighborhood of $y$, there exists $\alpha_2 \in J$ such that:
        $$\alpha \succeq \alpha_2 \implies y_\alpha \in V.$$

<1>3. Directed set upper bound and product convergence:
    *Proof:*
    <2>1. Since $(J, \succeq)$ is a directed set, there exists an element $\alpha_0 \in J$ with $\alpha_0 \succeq \alpha_1$ and $\alpha_0 \succeq \alpha_2$.
    <2>2. Let $\alpha \in J$ satisfy $\alpha \succeq \alpha_0$.
    <2>3. By transitivity of the preorder $\succeq$, $\alpha \succeq \alpha_1$ (so $x_\alpha \in U$) and $\alpha \succeq \alpha_2$ (so $y_\alpha \in V$).
    <2>4. Thus $(x_\alpha, y_\alpha) \in U \times V \subseteq W$ for all $\alpha \succeq \alpha_0$.
    <2>5. Since $W$ was arbitrary, the net $(x_\alpha, y_\alpha)_{\alpha \in J}$ is eventually in every neighborhood of $(x, y)$, so $(x_\alpha, y_\alpha) \to (x, y)$ in $X \times Y$. Q.E.D.
:::
