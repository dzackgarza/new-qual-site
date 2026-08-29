---
schema: qual/card@1
id: P-RVG47
kind: problem
title: A Lie group with no faithful finite-dimensional representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Do you know a Lie group that has no faithful finite-dimensional representation?
:::

::: solution
**Goal:** Exhibit a connected Lie group with no faithful finite-dimensional representation (the universal cover $\widetilde{\operatorname{SL}_2(\mathbb{R})}$ of $\operatorname{SL}_2(\mathbb{R})$) and prove this property.

<1>1. Candidate: The universal covering group $\widetilde{\operatorname{SL}_2(\mathbb{R})}$:
    *Proof:*
    <2>1. The Lie group $\operatorname{SL}_2(\mathbb{R})$ is connected and has fundamental group $\pi_1(\operatorname{SL}_2(\mathbb{R})) \cong \mathbb{Z}$ (since $\operatorname{SL}_2(\mathbb{R})$ deformation retracts onto $\operatorname{SO}(2) \cong S^1$).
    <2>2. Let $G = \widetilde{\operatorname{SL}_2(\mathbb{R})}$ be its universal covering group, with covering homomorphism $p: G \to \operatorname{SL}_2(\mathbb{R})$.
    <2>3. The kernel $\ker p = Z(G)$ is the center of $G$, which is isomorphic to $\mathbb{Z}$.

<1>2. Lie algebra representations:
    *Proof:*
    <2>1. Any finite-dimensional smooth representation $\rho: G \to \operatorname{GL}(V)$ (with $\dim V < \infty$) induces a Lie algebra representation $d\rho: \mathfrak{g} \to \mathfrak{gl}(V)$, where $\mathfrak{g} = \mathfrak{sl}_2(\mathbb{R})$.
    <2>2. Since $\mathfrak{sl}_2(\mathbb{R})$ is a simple real Lie algebra, the Lie algebra representation $d\rho$ extends uniquely to a complex Lie algebra representation of the complexification $\mathfrak{sl}_2(\mathbb{C}) = \mathfrak{sl}_2(\mathbb{R}) \otimes_\mathbb{R} \mathbb{C}$.

<1>3. Descent to the linear algebraic group $\operatorname{SL}_2(\mathbb{C})$:
    *Proof:*
    <2>1. The simply connected complex Lie group corresponding to $\mathfrak{sl}_2(\mathbb{C})$ is $\operatorname{SL}_2(\mathbb{C})$.
    <2>2. Therefore, the Lie algebra representation $d\rho \otimes \mathbb{C}$ integrates to a unique holomorphic representation $\widetilde{\rho}: \operatorname{SL}_2(\mathbb{C}) \to \operatorname{GL}(V_\mathbb{C})$.
    <2>3. Restricting $\widetilde{\rho}$ to the real subgroup $\operatorname{SL}_2(\mathbb{R}) \subset \operatorname{SL}_2(\mathbb{C})$ gives a representation $\rho_{\operatorname{SL}_2(\mathbb{R})}: \operatorname{SL}_2(\mathbb{R}) \to \operatorname{GL}(V)$.
    <2>4. Since $G = \widetilde{\operatorname{SL}_2(\mathbb{R})}$ is connected, the unique representation of $G$ with derivative $d\rho$ must be the pullback:
        $$\rho = \rho_{\operatorname{SL}_2(\mathbb{R})} \circ p.$$

<1>4. Obstruction to fidelity:
    *Proof:*
    <2>1. Because $\rho = \rho_{\operatorname{SL}_2(\mathbb{R})} \circ p$, the kernel of $\rho$ contains $\ker p$:
        $$\ker p \subseteq \ker \rho.$$
    <2>2. Since $\ker p \cong \mathbb{Z} \ne \{e\}$, the representation $\rho$ is never injective.
    <2>3. In particular, the center $Z(G) \cong \mathbb{Z}$ is mapped into the finite subgroup $\{\pm I\}$ (or kernel), so $\ker\rho$ is always infinite.

<1>5. Conclusion:
    The universal cover $\widetilde{\operatorname{SL}_2(\mathbb{R})}$ is a connected Lie group with no faithful finite-dimensional representations (in fact, it is not a matrix Lie group). Q.E.D.
:::
