---
schema: qual/card@1
id: P-TOPF20H
kind: problem
title: 'A finite CW complex cannot have finite nontrivial $\pi_1$ and trivial higher homotopy'
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Fundamental Group
  - Euler Characteristic
  - Universal Cover
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Let $X$ be a connected CW complex such that $\pi_1(X)$ is a nontrivial finite group and $\pi_k(X) = 0$ for any $k \geq 2$.
Show that $X$ can not be a finite CW complex.
(Namely, $X$ must have infinitely many cells.)
Hint: Compute the Euler characteristic of the universal covering space.
:::

::: {.solution}
**Goal:** Prove that a connected CW complex $X$ with finite non-trivial $\pi_1(X)$ and $\pi_k(X) = 0$ for all $k \ge 2$ (an Eilenberg–MacLane space $K(G, 1)$ for a finite group $G \neq 1$) cannot be a finite CW complex.

::: pf

::: pf-step
Properties of the universal covering space $\widetilde{X}$:

::: pf-proof

::: pf-step
Let $p: \widetilde{X} \to X$ be the universal covering projection.
:::

::: pf-step
The number of sheets of the covering is $d = |\pi_1(X)|$. Since $\pi_1(X)$ is non-trivial and finite, $d \in \mathbb{Z}$ and $d \ge 2$.
:::

::: pf-step
By definition of the universal cover, $\pi_1(\widetilde{X}) = 0$.
:::

::: pf-step
For every $k \ge 2$, the covering map $p$ induces an isomorphism on higher homotopy groups:
$$\pi_k(\widetilde{X}) \cong \pi_k(X) = 0.$$
:::

::: pf-step
Thus all homotopy groups of $\widetilde{X}$ are trivial: $\pi_k(\widetilde{X}) = 0$ for all $k \ge 0$.
:::

::: pf-step
By Whitehead's Theorem, a CW complex with all homotopy groups trivial is contractible: $\widetilde{X} \simeq \{*\}$.
:::

:::

:::

::: {.pf-step #s2}
Euler characteristic of $\widetilde{X}$ via contractibility:

::: pf-proof

::: pf-step
Since $\widetilde{X}$ is contractible, its singular homology groups are:
$$H_0(\widetilde{X}; \mathbb{Q}) \cong \mathbb{Q}, \qquad H_k(\widetilde{X}; \mathbb{Q}) = 0 \quad \text{for all } k \ge 1.$$
:::

::: pf-step
Therefore the Euler characteristic of $\widetilde{X}$ is
$$\chi(\widetilde{X}) = \sum_{k=0}^\infty (-1)^k \dim_\mathbb{Q} H_k(\widetilde{X}; \mathbb{Q}) = 1 - 0 + 0 - \cdots = 1.$$
:::

:::

:::

::: {.pf-step #s3}
Covering formula for the Euler characteristic of finite CW complexes:

::: pf-proof

::: pf-step
Suppose for contradiction that $X$ is a finite CW complex.
:::

::: pf-step
Let $c_n(X)$ denote the number of $n$-cells of $X$. Since $X$ is finite, $c_n(X)$ is finite for each $n$ and $c_n(X) = 0$ for $n > N$.
:::

::: pf-step
Under the covering projection $p: \widetilde{X} \to X$, each open $n$-cell $e \subset X$ lifts to exactly $d$ disjoint open $n$-cells in $\widetilde{X}$, so $\widetilde{X}$ is a finite CW complex with
$$c_n(\widetilde{X}) = d \cdot c_n(X).$$
:::

::: pf-step
Computing the Euler characteristic of $\widetilde{X}$ from its cellular chain complex:
$$\chi(\widetilde{X}) = \sum_{n=0}^N (-1)^n c_n(\widetilde{X}) = \sum_{n=0}^N (-1)^n (d \cdot c_n(X)) = d \sum_{n=0}^N (-1)^n c_n(X) = d \cdot \chi(X).$$
:::

:::

:::

::: pf-step
Contradiction:

::: pf-proof

::: pf-step
Combining step [](#s2){.pf-ref} and step [](#s3){.pf-ref} gives the integer equation
$$d \cdot \chi(X) = 1.$$
:::

::: pf-step
Since $X$ is a finite CW complex, $\chi(X) = \sum (-1)^n c_n(X) \in \mathbb{Z}$ is an integer.
:::

::: pf-step
Since $d = |\pi_1(X)| \ge 2$, the only rational solution is $\chi(X) = 1/d \notin \mathbb{Z}$, a contradiction.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
The space $X$ cannot be a finite CW complex (it must have infinitely many cells).
:::

:::

:::
:::
