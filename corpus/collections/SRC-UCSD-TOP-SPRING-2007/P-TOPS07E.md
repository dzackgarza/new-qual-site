---
schema: qual/card@1
id: P-TOPS07E
kind: problem
title: "Any map from S^2 to a surface of genus >= 1 has degree zero"
classification:
  areas:
  - topology
  topics:
  - Degree Theory
  - Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
On any closed orientable surface $\Sigma_g$ of genus $g \geq 1$, it is possible to find a pair of simple closed curves $\alpha, \beta \subset \Sigma_g$ (submanifolds homeomorphic to $S^1$) meeting transversely at exactly one point ($I(\alpha, \beta) = \pm 1$).
Use this fact together with intersection theory to show that any smooth (or continuous) map $f: S^2 \to \Sigma_g$ has **degree zero**:
$$\deg(f) = 0.$$
:::

::: solution
**Goal:** Prove that $\deg(f) = 0$ for any map $f: S^2 \to \Sigma_g$ ($g \ge 1$) using intersection theory and pullbacks of transverse submanifolds.

<1>1. Setting up Intersection Theory on Oriented Manifolds:
    *Proof:*
    <2>1. Let $M, N$ be closed, oriented, smooth manifolds of the same dimension $n = 2$, and let $f: M \to N$ be a smooth map.
    <2>2. Let $A, B \subset N$ be two closed submanifolds of complementary dimensions ($\dim A + \dim B = \dim N = 2$, so $\dim A = 1$ and $\dim B = 1$) that intersect transversely at a finite set of points.
    <2>3. The oriented **intersection number** of $A$ and $B$ in $N$ is denoted $I_N(A, B) \in \mathbb{Z}$.
    <2>4. If $f$ is transverse to both $A$ and $B$, their preimages $f^{-1}(A)$ and $f^{-1}(B)$ are 1-dimensional submanifolds of $M = S^2$ intersecting transversely.
    <2>5. By the **Naturality / Pullback Formula for Intersection Numbers** in differential topology:
        $$I_M(f^{-1}(A), f^{-1}(B)) = \deg(f) \cdot I_N(A, B).$$

<1>2. Application to $N = \Sigma_g$ and $M = S^2$:
    *Proof:*
    <2>1. By the given fact, choose two simple closed curves $\alpha, \beta \subset \Sigma_g$ meeting transversely at exactly one point.
    <2>2. Their intersection number on $\Sigma_g$ is:
        $$I_{\Sigma_g}(\alpha, \beta) = \pm 1 \ne 0.$$
    <2>3. By Smooth Approximation and Sard's Theorem, perturb $f: S^2 \to \Sigma_g$ within its homotopy class so that $f$ is smooth and transverse to both $\alpha$ and $\beta$.
    <2>4. The preimages $C_1 = f^{-1}(\alpha)$ and $C_2 = f^{-1}(\beta)$ are disjoint unions of smooth circles embedded in $S^2$.

<1>3. Intersection Number of 1-Cycles in $S^2$:
    *Proof:*
    <2>1. The intersection pairing on homology is dual to the cup product pairing on cohomology:
        $$I_{S^2}(C_1, C_2) = \langle [C_1] \frown [C_2], [S^2] \rangle = \int_{S^2} \omega_1 \wedge \omega_2$$
        where $\omega_1, \omega_2 \in H^1(S^2; \mathbb{R})$ are the Poincaré duals to $C_1, C_2$.
    <2>2. But the first cohomology of the 2-sphere vanishes:
        $$H^1(S^2; \mathbb{R}) = 0 \quad (\text{and } H_1(S^2; \mathbb{Z}) = 0).$$
    <2>3. Alternatively, by the Jordan Curve Theorem on $S^2$, every simple closed curve $C \subset S^2$ separates $S^2$ into two open disks ($C = \partial D$).
    <2>4. Thus every 1-cycle in $S^2$ is the boundary of a 2-chain ($[C_1] = 0 \in H_1(S^2)$).
    <2>5. Since $H_1(S^2) = 0$, any two 1-cycles in $S^2$ have **zero intersection number**:
        $$I_{S^2}(f^{-1}(\alpha), f^{-1}(\beta)) = 0.$$

<1>4. Calculation of $\deg(f)$:
    *Proof:*
    <2>1. Substituting $I_{S^2}(f^{-1}(\alpha), f^{-1}(\beta)) = 0$ and $I_{\Sigma_g}(\alpha, \beta) = \pm 1$ into the pullback formula:
        $$0 = \deg(f) \cdot (\pm 1).$$
    <2>2. Since $\pm 1 \ne 0$, this forces:
        $$\deg(f) = 0.$$

<1>5. Conclusion:
    Every continuous map $f: S^2 \to \Sigma_g$ has degree 0. Q.E.D.
:::
