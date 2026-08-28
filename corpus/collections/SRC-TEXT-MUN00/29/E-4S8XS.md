---
schema: qual/card@1
id: E-4S8XS
kind: exercise
title: Nets in Hausdorff spaces have at most one limit
classification:
  areas:
  - topology
  topics:
  - Nets
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $X$ is Hausdorff, a net in $X$ converges to at most one point.
:::

::: solution
**Goal:** Prove that in a Hausdorff topological space $X$, limits of nets are unique (i.e. every net converges to at most one point).

<1>1. Setting and hypothesis:
    Let $(x_\alpha)_{\alpha \in J}$ be a net indexed by a directed set $(J, \succeq)$ in a Hausdorff space $X$.
    Suppose that $(x_\alpha) \to x$ and $(x_\alpha) \to y$ for points $x, y \in X$.
    We must show that $x = y$.

<1>2. Separation by disjoint open neighborhoods:
    *Proof:*
    <2>1. Suppose for contradiction that $x \neq y$.
    <2>2. Because $X$ is Hausdorff ($T_2$), there exist open sets $U, V \subseteq X$ such that $x \in U$, $y \in V$, and $U \cap V = \varnothing$.

<1>3. Eventual containment in both neighborhoods:
    *Proof:*
    <2>1. Since $(x_\alpha) \to x$ and $U$ is an open neighborhood of $x$, there exists $\alpha_1 \in J$ such that:
        $$\alpha \succeq \alpha_1 \implies x_\alpha \in U.$$
    <2>2. Since $(x_\alpha) \to y$ and $V$ is an open neighborhood of $y$, there exists $\alpha_2 \in J$ such that:
        $$\alpha \succeq \alpha_2 \implies x_\alpha \in V.$$

<1>4. Derivation of contradiction:
    *Proof:*
    <2>1. Because $(J, \succeq)$ is a directed set, there exists an upper bound $\alpha_0 \in J$ satisfying $\alpha_0 \succeq \alpha_1$ and $\alpha_0 \succeq \alpha_2$.
    <2>2. By <1>3, $\alpha_0 \succeq \alpha_1$ implies $x_{\alpha_0} \in U$, and $\alpha_0 \succeq \alpha_2$ implies $x_{\alpha_0} \in V$.
    <2>3. Therefore $x_{\alpha_0} \in U \cap V = \varnothing$, which is impossible.

<1>5. Conclusion:
    The assumption $x \neq y$ is false, so $x = y$. Thus every net in $X$ has at most one limit. Q.E.D.
:::
