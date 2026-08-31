---
schema: qual/card@1
id: P-TOPF20H
kind: problem
title: "A CW complex with finite nontrivial pi_1 and no higher homotopy cannot be finite"
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

::: problem
Let $X$ be a connected CW complex such that $\pi_1(X)$ is a nontrivial finite group and $\pi_k(X) = 0$ for any $k \geq 2$.
Show that $X$ can not be a finite CW complex.
(Namely, $X$ must have infinitely many cells.)
Hint: Compute the Euler characteristic of the universal covering space.
:::

::: solution
**Goal:** Prove that a connected CW complex $X$ with finite non-trivial $\pi_1(X)$ and $\pi_k(X) = 0$ for all $k \ge 2$ (an Eilenberg–MacLane space $K(G, 1)$ for a finite group $G \neq 1$) cannot be a finite CW complex.

<1>1. Properties of the universal covering space $\widetilde{X}$:
    *Proof:*
    <2>1. Let $p: \widetilde{X} \to X$ be the universal covering projection.
    <2>2. The number of sheets of the covering is $d = |\pi_1(X)|$. Since $\pi_1(X)$ is non-trivial and finite, $d \in \mathbb{Z}$ and $d \ge 2$.
    <2>3. By definition of the universal cover, $\pi_1(\widetilde{X}) = 0$.
    <2>4. For every $k \ge 2$, the covering map $p$ induces an isomorphism on higher homotopy groups:
    $$\pi_k(\widetilde{X}) \cong \pi_k(X) = 0.$$
    <2>5. Thus all homotopy groups of $\widetilde{X}$ are trivial: $\pi_k(\widetilde{X}) = 0$ for all $k \ge 0$.
    <2>6. By Whitehead's Theorem, a CW complex with all homotopy groups trivial is contractible: $\widetilde{X} \simeq \{*\}$.

<1>2. Euler characteristic of $\widetilde{X}$ via contractibility:
    *Proof:*
    <2>1. Since $\widetilde{X}$ is contractible, its singular homology groups are:
    $$H_0(\widetilde{X}; \mathbb{Q}) \cong \mathbb{Q}, \qquad H_k(\widetilde{X}; \mathbb{Q}) = 0 \quad \text{for all } k \ge 1.$$
    <2>2. Therefore the Euler characteristic of $\widetilde{X}$ is
    $$\chi(\widetilde{X}) = \sum_{k=0}^\infty (-1)^k \dim_\mathbb{Q} H_k(\widetilde{X}; \mathbb{Q}) = 1 - 0 + 0 - \cdots = 1.$$

<1>3. Covering formula for the Euler characteristic of finite CW complexes:
    *Proof:*
    <2>1. Suppose for contradiction that $X$ is a finite CW complex.
    <2>2. Let $c_n(X)$ denote the number of $n$-cells of $X$. Since $X$ is finite, $c_n(X)$ is finite for each $n$ and $c_n(X) = 0$ for $n > N$.
    <2>3. Under the covering projection $p: \widetilde{X} \to X$, each open $n$-cell $e \subset X$ lifts to exactly $d$ disjoint open $n$-cells in $\widetilde{X}$, so $\widetilde{X}$ is a finite CW complex with
    $$c_n(\widetilde{X}) = d \cdot c_n(X).$$
    <2>4. Computing the Euler characteristic of $\widetilde{X}$ from its cellular chain complex:
    $$\chi(\widetilde{X}) = \sum_{n=0}^N (-1)^n c_n(\widetilde{X}) = \sum_{n=0}^N (-1)^n (d \cdot c_n(X)) = d \sum_{n=0}^N (-1)^n c_n(X) = d \cdot \chi(X).$$

<1>4. Contradiction:
    *Proof:*
    <2>1. Combining <1>2 and <1>3 gives the integer equation
    $$d \cdot \chi(X) = 1.$$
    <2>2. Since $X$ is a finite CW complex, $\chi(X) = \sum (-1)^n c_n(X) \in \mathbb{Z}$ is an integer.
    <2>3. Since $d = |\pi_1(X)| \ge 2$, the only rational solution is $\chi(X) = 1/d \notin \mathbb{Z}$, a contradiction.

<1>5. Conclusion:
    *Proof:*
    The space $X$ cannot be a finite CW complex (it must have infinitely many cells).
:::
