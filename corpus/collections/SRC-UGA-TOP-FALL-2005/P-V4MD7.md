---
schema: qual/card@1
id: P-V4MD7
kind: problem
title: $H_0$ and $H_1$ of the complete graph $K_5$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the integer homology groups $H_0(K_5; \mathbb{Z})$ and $H_1(K_5; \mathbb{Z})$ of the **complete graph** $K_5$ on 5 vertices.
:::

::: solution
**Goal:** Compute $H_0(K_5)$ and $H_1(K_5)$ via cellular homology and the Euler characteristic of 1-dimensional CW complexes.

<1>1. CW Complex Structure of $K_5$:
    *Proof:*
    <2>1. The complete graph $K_5$ is a 1-dimensional CW complex (graph) with:
        - Vertices (0-cells): $V = 5$,
        - Edges (1-cells): $E = \binom{5}{2} = \frac{5 \cdot 4}{2} = 10$.
    <2>2. $K_5$ is a path-connected topological space (every pair of vertices is connected by an edge).

<1>2. Computation of $H_0(K_5; \mathbb{Z})$:
    *Proof:*
    <2>1. For any non-empty path-connected topological space $X$, the 0-th homology group is isomorphic to $\mathbb{Z}$:
        $$H_0(K_5; \mathbb{Z}) \cong \mathbb{Z}.$$

<1>3. Computation of $H_1(K_5; \mathbb{Z})$ via Euler Characteristic:
    *Proof:*
    <2>1. For any finite 1-dimensional CW complex $X$:
        - The cellular chain complex is $0 \to C_1(X) \xrightarrow{\partial_1} C_0(X) \to 0$.
        - Higher homology groups vanish: $H_k(X) = 0$ for all $k \ge 2$.
    <2>2. The **Euler characteristic** $\chi(X)$ can be computed in two ways:
        - By counting cells:
          $$\chi(K_5) = c_0 - c_1 = V - E = 5 - 10 = -5.$$
        - By alternating sum of Betti numbers:
          $$\chi(K_5) = \operatorname{rank} H_0(K_5) - \operatorname{rank} H_1(K_5) = 1 - \operatorname{rank} H_1(K_5).$$
    <2>3. Setting the two expressions equal:
        $$1 - \operatorname{rank} H_1(K_5) = -5 \implies \operatorname{rank} H_1(K_5) = 1 - (-5) = 6.$$
    <2>4. Since 1-dimensional complexes have free abelian homology groups ($H_1 \le C_1 \cong \mathbb{Z}^{10}$ is a subgroup of a free abelian group, hence torsion-free):
        $$H_1(K_5; \mathbb{Z}) \cong \mathbb{Z}^6.$$

<1>4. Alternative Homotopy Retraction Method (Maximal Spanning Tree):
    *Proof:*
    <2>1. Choose any maximal spanning tree $T \subset K_5$.
    <2>2. Any tree on 5 vertices has $V - 1 = 5 - 1 = 4$ edges and is contractible ($T \simeq \{*\}$).
    <2>3. Collapsing $T$ to a point gives a homotopy equivalence:
        $$K_5 \simeq K_5 / T \cong \bigvee_{i=1}^{E - (V - 1)} S^1 = \bigvee_{i=1}^{10 - 4} S^1 = \bigvee_{i=1}^6 S^1.$$
    <2>4. The homology of a wedge sum of 6 circles is:
        $$H_1\left( \bigvee_{i=1}^6 S^1 \right) \cong \bigoplus_{i=1}^6 H_1(S^1) \cong \mathbb{Z}^6.$$

<1>5. Conclusion:
    $$H_0(K_5; \mathbb{Z}) \cong \mathbb{Z}, \qquad H_1(K_5; \mathbb{Z}) \cong \mathbb{Z}^6, \qquad H_k(K_5; \mathbb{Z}) = 0 \text{ for } k \ge 2.$$
    Q.E.D.
:::
