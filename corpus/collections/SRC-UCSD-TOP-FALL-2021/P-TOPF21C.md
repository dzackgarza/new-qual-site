---
schema: qual/card@1
id: P-TOPF21C
kind: problem
title: "A simply-connected closed 3-manifold is homotopy equivalent to S^3"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $X$ be a $3$-dimensional simply-connected closed manifold (compact, no boundary).
Show that $X$ is homotopy equivalent to $S^3$.
:::

::: solution
**Goal:** Prove that every closed, simply connected 3-manifold $X$ is homotopy equivalent to $S^3$ using algebraic topology.

<1>1. Homology groups of $X$:
    *Proof:*
    <2>1. Since $X$ is connected, $H_0(X; \mathbb{Z}) \cong \mathbb{Z}$.
    <2>2. Since $X$ is simply connected ($\pi_1(X) = 0$), the Hurewicz Theorem (or abelianization) gives:
    $$H_1(X; \mathbb{Z}) \cong \pi_1(X)_{\text{ab}} = 0.$$
    <2>3. Since $\pi_1(X) = 0$, the first Stiefel–Whitney class vanishes ($w_1(X) = 0$), so $X$ is orientable.
    <2>4. For a closed, connected, oriented 3-manifold, the top homology is $H_3(X; \mathbb{Z}) \cong \mathbb{Z}$, and $H_k(X; \mathbb{Z}) = 0$ for all $k > 3$.
    <2>5. By Poincaré Duality:
    $$H_2(X; \mathbb{Z}) \cong H^1(X; \mathbb{Z}).$$
    <2>6. By the Universal Coefficient Theorem for cohomology:
    $$H^1(X; \mathbb{Z}) \cong \operatorname{Hom}(H_1(X; \mathbb{Z}), \mathbb{Z}) \oplus \operatorname{Ext}(H_0(X; \mathbb{Z}), \mathbb{Z}) \cong \operatorname{Hom}(0, \mathbb{Z}) \oplus \operatorname{Ext}(\mathbb{Z}, \mathbb{Z}) = 0 \oplus 0 = 0.$$
    <2>7. Thus $H_2(X; \mathbb{Z}) = 0$.
    <2>8. In summary, the homology of $X$ matches the homology of $S^3$:
    $$H_k(X; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & k = 0, 3, \\ 0 & k \neq 0, 3. \end{cases}$$

<1>2. Homotopy groups via the Hurewicz Theorem:
    *Proof:*
    <2>1. Since $\pi_1(X) = 0$ and $\widetilde{H}_1(X) = \widetilde{H}_2(X) = 0$, the Hurewicz Theorem in dimension 2 implies $\pi_2(X) \cong H_2(X; \mathbb{Z}) = 0$.
    <2>2. By the Hurewicz Theorem in dimension 3 for simply connected spaces, the Hurewicz homomorphism
    $$h: \pi_3(X) \to H_3(X; \mathbb{Z}) \cong \mathbb{Z}$$
    is an isomorphism.
    <2>3. Thus $\pi_3(X) \cong \mathbb{Z}$.

<1>3. Homotopy equivalence via Whitehead's Theorem:
    *Proof:*
    <2>1. Choose a continuous map $f: S^3 \to X$ representing a generator of $\pi_3(X) \cong \mathbb{Z}$.
    <2>2. By definition of the Hurewicz homomorphism, the induced map $f_*: H_3(S^3; \mathbb{Z}) \to H_3(X; \mathbb{Z})$ sends the fundamental class $[S^3]$ to $h([f])$, which is a generator of $H_3(X; \mathbb{Z})$.
    <2>3. Thus $f_*: H_3(S^3; \mathbb{Z}) \to H_3(X; \mathbb{Z})$ is an isomorphism.
    <2>4. In degree 0, $f_*: H_0(S^3; \mathbb{Z}) \to H_0(X; \mathbb{Z})$ is an isomorphism $\mathbb{Z} \to \mathbb{Z}$ since $S^3$ and $X$ are non-empty and connected.
    <2>5. In all other degrees $k \neq 0, 3$, $H_k(S^3) = H_k(X) = 0$, so $f_*\colon 0 \to 0$ is an isomorphism.
    <2>6. By Moise's Theorem, every 3-manifold admits a triangulation as a finite simplicial complex, so $X$ is a finite CW complex.
    <2>7. By Whitehead's Theorem for simply connected CW complexes, a continuous map inducing isomorphisms on all homology groups is a homotopy equivalence.
    <2>8. Therefore $f: S^3 \to X$ is a homotopy equivalence, so $X \simeq S^3$.

<1>4. Conclusion:
    *Proof:*
    Every closed simply connected 3-manifold $X$ is homotopy equivalent to $S^3$.
:::
