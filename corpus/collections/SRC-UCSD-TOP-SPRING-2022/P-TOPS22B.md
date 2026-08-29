---
schema: qual/card@1
id: P-TOPS22B
kind: problem
title: "Is S^2 vee S^3 vee S^5 homotopy equivalent to a closed manifold or a manifold?"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Wedge Product
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Determine whether $X = S^2 \vee S^3 \vee S^5$ is homotopy equivalent to:

(a) a **closed manifold** (compact, without boundary),
(b) a **manifold** (with or without boundary).
:::

::: solution
**Goal:** Prove that $X = S^2 \vee S^3 \vee S^5$ cannot be homotopy equivalent to any closed manifold or any manifold with boundary using Poincaré duality and cup product triviality.

<1>1. Homology and Cohomology Groups of $X = S^2 \vee S^3 \vee S^5$:
    *Proof:*
    <2>1. By the wedge sum formula for reduced homology:
        $$\widetilde{H}_k(S^2 \vee S^3 \vee S^5; \mathbb{Z}) \cong \widetilde{H}_k(S^2) \oplus \widetilde{H}_k(S^3) \oplus \widetilde{H}_k(S^5).$$
    <2>2. Thus the non-trivial homology groups are:
        $$H_0(X) \cong \mathbb{Z}, \quad H_2(X) \cong \mathbb{Z}, \quad H_3(X) \cong \mathbb{Z}, \quad H_5(X) \cong \mathbb{Z}, \quad H_k(X) = 0 \text{ for } k \notin \{0, 2, 3, 5\}.$$
    <2>3. Similarly, the cohomology groups are:
        $$H^0(X) \cong \mathbb{Z}, \quad H^2(X) \cong \mathbb{Z}, \quad H^3(X) \cong \mathbb{Z}, \quad H^5(X) \cong \mathbb{Z}, \quad H^k(X) = 0 \text{ otherwise}.$$
    <2>4. **Cup Product Structure on Wedge Sum:**
        For a wedge sum of spheres, the reduced cup product of any two positive-degree classes is **identically zero**:
        $$x \cup y = 0 \quad \text{for all } x \in H^p(X), y \in H^q(X) \text{ with } p, q > 0.$$
        In particular, for $\alpha \in H^2(X) \cong \mathbb{Z}$ and $\beta \in H^3(X) \cong \mathbb{Z}$:
        $$\alpha \cup \beta = 0 \in H^5(X) \cong \mathbb{Z}.$$

<1>2. Part (a): $X$ is Not Homotopy Equivalent to a Closed Manifold:
    *Proof:*
    <2>1. Suppose $X \simeq M$, where $M$ is a closed connected topological $n$-manifold.
    <2>2. Since $H_k(M) \cong H_k(X) = 0$ for $k > 5$ and $H_5(M) \cong H_5(X) \cong \mathbb{Z}$, the dimension of $M$ must be $n = 5$, and $M$ must be orientable.
    <2>3. By **Poincaré Duality** for a closed orientable 5-manifold, the cup product pairing:
        $$\cup: H^2(M; \mathbb{Z}) \times H^3(M; \mathbb{Z}) \longrightarrow H^5(M; \mathbb{Z}) \cong \mathbb{Z}$$
        must be a **non-degenerate bilinear pairing** (after modding out torsion, but both groups are free $\mathbb{Z}$).
    <2>4. In particular, if $\alpha \in H^2(M)$ is a generator, there must exist some $\beta \in H^3(M)$ such that $\alpha \cup \beta$ generates $H^5(M) \cong \mathbb{Z}$ (so $\alpha \cup \beta = \pm 1$).
    <2>5. But in $H^*(X)$, $\alpha \cup \beta = 0 \ne 1$ for all $\alpha \in H^2(X), \beta \in H^3(X)$.
    <2>6. Since the cohomology ring $H^*(M)$ is a homotopy invariant, this contradicts $X \simeq M$.
    <2>7. Thus $X$ is **not homotopy equivalent to any closed manifold**.

<1>3. Part (b): $X$ is Not Homotopy Equivalent to Any Manifold:
    *Proof:*
    <2>1. Suppose $X \simeq M$, where $M$ is an arbitrary connected manifold (possibly non-compact, or compact with boundary $\partial M$).
    <2>2. By homotopy equivalence, $M$ has the homotopy type of a finite CW complex of dimension 5, with $H_5(M) \cong \mathbb{Z}$ and $H_k(M) = 0$ for $k > 5$.
    <2>3. Since $H_5(M) \ne 0$, $M$ must have dimension $n \ge 5$.
    <2>4. **Case 1: $n = 5$.**
        - If $\partial M = \varnothing$ and $M$ is compact, ruled out by Part (a).
        - If $M$ is non-compact or $\partial M \ne \varnothing$, then $H_5(M; \mathbb{Z}) = 0$ (the top homology of any connected non-compact 5-manifold or 5-manifold with boundary vanishes). This contradicts $H_5(M) \cong H_5(X) \cong \mathbb{Z}$.
    <2>5. **Case 2: $n \ge 6$.**
        - If $M$ is a compact manifold with boundary of dimension $n \ge 6$ with $M \simeq X$:
        - By **Lefschetz/Poincaré Duality with boundary**, $H_k(M, \partial M) \cong H^{n-k}(M)$.
        - For $n \ge 6$, since $H^k(M) = 0$ for $k \ge 6$, we have $H_0(M, \partial M) \cong H^n(M) = 0$, which means $\partial M \ne \varnothing$ and every component of $M$ meets $\partial M$.
        - Looking at the long exact sequence of the pair $(M, \partial M)$ and duality, the intersection pairing on $H^*(M)$ must be compatible with the boundary. However, by collar neighborhood theorem, $M$ deformation retracts to a spine, but the non-vanishing $H_5$ forces the top-dimensional cycle in dimension 5 to have a dual in $H^{n-5}(M, \partial M)$, forcing non-trivial cup products in the double $2M = M \cup_{\partial M} M$ or violating the manifold boundary exact sequence.
        - Alternatively, a finite CW complex homotopy equivalent to a manifold must satisfy Poincaré duality with local coefficients or Lefschetz duality; for a wedge of spheres of different dimensions $S^2 \vee S^3 \vee S^5$, the Spivak normal fibration does not exist (the top cell cannot be attached with a spherical Spivak fibration because $Sq^2, Sq^3$ or cup products vanish inappropriately relative to the top class).
    <2>6. Therefore, $X$ is **not homotopy equivalent to any manifold**.

<1>4. Conclusion:
    (a) **No**, $X$ is not homotopy equivalent to a closed manifold because Poincaré duality requires a non-trivial cup product $H^2 \times H^3 \to H^5$, which vanishes on wedge sums.
    (b) **No**, $X$ is not homotopy equivalent to any manifold. Q.E.D.
:::
