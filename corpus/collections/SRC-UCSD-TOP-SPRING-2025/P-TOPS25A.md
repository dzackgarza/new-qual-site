---
schema: qual/card@1
id: P-TOPS25A
kind: problem
title: Fundamental group of the 2-sphere minus ten points
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $X = S^2 \setminus \{p_1, p_2, \dots, p_{10}\}$ be the topological space obtained by removing 10 distinct points from the 2-sphere $S^2$.
Compute its **fundamental group** $\pi_1(X, x_0)$.
:::

::: solution
**Goal:** Compute the fundamental group of a punctured sphere using stereographic projection and deformation retractions onto a wedge of circles.

<1>1. Stereographic Projection to the Plane:
    *Proof:*
    <2>1. Removing one point (say $p_{10}$, the "north pole") from the 2-sphere $S^2$ is homeomorphic to the Euclidean plane $\mathbb{R}^2$ via **stereographic projection**:
        $$S^2 \setminus \{p_{10}\} \cong \mathbb{R}^2.$$
    <2>2. Under this homeomorphism, the remaining 9 points $\{p_1, \dots, p_9\}$ map to 9 distinct points $\{q_1, \dots, q_9\}$ in $\mathbb{R}^2$.
    <2>3. Therefore, $X$ is homeomorphic to the 9-punctured plane:
        $$X = S^2 \setminus \{p_1, \dots, p_{10}\} \cong \mathbb{R}^2 \setminus \{q_1, q_2, \dots, q_9\}.$$

<1>2. Deformation Retraction onto a Wedge of Circles:
    *Proof:*
    <2>1. Choose a large closed disk $D \subset \mathbb{R}^2$ containing all 9 points $\{q_1, \dots, q_9\}$ in its interior.
    <2>2. $\mathbb{R}^2 \setminus \{q_1, \dots, q_9\}$ deformation retracts radially onto $D \setminus \{q_1, \dots, q_9\}$.
    <2>3. The disk minus 9 points $D \setminus \{q_1, \dots, q_9\}$ is a compact 2-manifold with boundary (a disk with 9 open sub-disks removed), which has 10 boundary components.
    <2>4. Any connected 2-manifold with non-empty boundary deformation retracts onto a 1-dimensional CW complex (graph).
    <2>5. Specifically, connecting the outer boundary of $D$ to each of the 9 puncture boundaries via disjoint simple arcs and retracting shows that $D \setminus \{q_1, \dots, q_9\}$ **deformation retracts onto a bouquet (wedge sum) of 9 circles**:
        $$X \simeq \bigvee_{i=1}^9 S^1.$$

<1>3. Computation of the Fundamental Group:
    *Proof:*
    <2>1. By the **Seifert–van Kampen Theorem**, the fundamental group of a wedge sum of circles is the **free group** on the circles:
        $$\pi_1\left( \bigvee_{i=1}^k S^1 \right) \cong F_k.$$
    <2>2. For $k = 9$:
        $$\pi_1(X) \cong F_9 = \langle \gamma_1, \gamma_2, \dots, \gamma_9 \rangle$$
        the free group on 9 generators (where each generator $\gamma_i$ corresponds to a simple loop winding once counterclockwise around the puncture $p_i$).

<1>4. Generalization to $n$ Points:
    *Proof:*
    <2>1. In general, removing $n \ge 1$ points from $S^2$ yields a space homeomorphic to $\mathbb{R}^2 \setminus (n-1 \text{ points}) \simeq \bigvee_{i=1}^{n-1} S^1$, with fundamental group $F_{n-1}$.
    <2>2. For $n = 10$, $n - 1 = 9$, yielding $F_9$.

<1>5. Conclusion:
    $\pi_1(S^2 \setminus \{10 \text{ points}\}) \cong F_9$, the free group of rank 9. Q.E.D.
:::
