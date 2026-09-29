---
schema: qual/card@1
id: E-AL52O
kind: problem
title: The Euler number is a topological invariant
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that the Euler number of a finite linear graph $X$ is a topological invariant of $X$.
[Hint: First consider the case where $X$ is connected.]
:::

::: {.solution}
**Goal:** Prove that the Euler characteristic $\chi(X) = V - E$ of a finite linear graph (1-dimensional CW complex) $X$ is a topological invariant.

::: pf

::: {.pf-step #s1}

Connected finite graphs:
    *Proof:*

::: pf-proof

::: pf-step

Let $X$ be a connected finite graph with $V$ vertices and $E$ edges.

:::

::: pf-step

Choose a maximal spanning tree $T \subseteq X$.

:::

::: pf-step

Because $T$ is a tree with $V$ vertices, it has exactly $V - 1$ edges and is contractible.

:::

::: pf-step

The quotient space $X / T$ is homeomorphic to a wedge sum of $k$ circles:
        $$X / T \cong \bigvee_{j=1}^k S^1,$$
        where the number of circles equals the number of remaining edges $E - (V - 1) = E - V + 1 = 1 - \chi(X)$.

:::

::: pf-step

Because $(X, T)$ is a CW pair with contractible subcomplex $T$, the quotient projection $q: X \to X / T$ is a homotopy equivalence (Theorem 84.1).

:::

::: pf-step

Thus the fundamental group of $X$ is a free group of rank $k$:
        $$\pi_1(X, x_0) \cong \pi_1\left(\bigvee_{j=1}^k S^1\right) \cong F_k.$$

:::

::: pf-step

The rank $k$ of a finitely generated free group is uniquely determined by its abelianization $\pi_1(X)^{\text{ab}} \cong \mathbb{Z}^k$ (or first homology $H_1(X) \cong \mathbb{Z}^k$).

:::

::: pf-step

Expressing $\chi(X)$ in terms of the rank gives:
        $$\chi(X) = 1 - k = 1 - \operatorname{rank}(\pi_1(X, x_0)).$$

:::

::: pf-step

Because the fundamental group is a topological (and homotopy) invariant, $\chi(X)$ is a topological invariant for any connected finite graph $X$.

:::

:::

:::

::: pf-step

General finite graphs (disconnected case):
    *Proof:*

::: pf-proof

::: pf-step

Let $X$ be a finite graph with $c$ connected components $X_1, \dots, X_c$.

:::

::: pf-step

The vertex and edge counts satisfy $V = \sum_{i=1}^c V_i$ and $E = \sum_{i=1}^c E_i$, so:
        $$\chi(X) = V - E = \sum_{i=1}^c (V_i - E_i) = \sum_{i=1}^c \chi(X_i).$$

:::

::: pf-step

Applying step [](#s1){.pf-ref} to each connected component $X_i$:
        $$\chi(X) = \sum_{i=1}^c \big(1 - \operatorname{rank}(\pi_1(X_i))\big) = c - \sum_{i=1}^c \operatorname{rank}(\pi_1(X_i)).$$

:::

::: pf-step

The number of connected components $c$ and the fundamental groups of the individual components are all topological invariants of the space $X$.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    The Euler number $\chi(X)$ is completely determined by the topology of $X$, and hence is a topological invariant. Q.E.D.
:::
