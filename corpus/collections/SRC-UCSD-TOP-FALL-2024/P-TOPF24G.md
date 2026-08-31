---
schema: qual/card@1
id: P-TOPF24G
kind: problem
title: 'Fundamental group and $\pi_2$ of $\mathbb{RP}^3 \# \mathbb{RP}^3$'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
What is the fundamental group of $X = \mathbb{RP}^3 \# \mathbb{RP}^3$?
Give a description of the universal cover $\widetilde{X}$ of $X$ and use this to calculate $\pi_2(X)$.
:::

::: solution
**Goal:** Compute the fundamental group $\pi_1(X)$, describe the universal cover $\widetilde{X}$, and compute $\pi_2(X)$ for the connected sum $X = \mathbb{RP}^3 \# \mathbb{RP}^3$.

<1>1. Computation of $\pi_1(X)$:
    *Proof:*
    <2>1. By definition of the connected sum of 3-manifolds, $X = M_1 \# M_2$ is formed by deleting the interior of an open 3-ball $B^3$ from each copy of $\mathbb{RP}^3$ to obtain $M_1' = M_2' = \mathbb{RP}^3 \setminus \operatorname{int}(D^3)$, and gluing along their boundary 2-spheres:
    $$X = M_1' \cup_{S^2} M_2'.$$
    <2>2. Since $\operatorname{codim}(D^3) = 3 \ge 3$, removing an open 3-ball does not affect the fundamental group:
    $$\pi_1(M_1') \cong \pi_1(\mathbb{RP}^3) \cong \mathbb{Z}/2\mathbb{Z}, \qquad \pi_1(M_2') \cong \pi_1(\mathbb{RP}^3) \cong \mathbb{Z}/2\mathbb{Z}.$$
    <2>3. The neck $S^2$ is simply connected ($\pi_1(S^2) = 0$).
    <2>4. Applying the Seifert–van Kampen Theorem to the open collar neighborhood decomposition of $X$:
    $$\pi_1(X) \cong \pi_1(M_1') *_{\pi_1(S^2)} \pi_1(M_2') \cong (\mathbb{Z}/2\mathbb{Z}) *_{\{e\}} (\mathbb{Z}/2\mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/2\mathbb{Z} \cong D_\infty,$$
    which is the infinite dihedral group $D_\infty = \langle a, b \mid a^2 = b^2 = 1 \rangle$.

<1>2. Description of the universal cover $\widetilde{X}$:
    *Proof:*
    <2>1. The universal cover of $M_1' = \mathbb{RP}^3 \setminus \operatorname{int}(D^3)$ is $\widetilde{M}_1' = S^3 \setminus (D_1^3 \cup D_2^3)$ (the 3-sphere with two antipodal open 3-balls removed).
    <2>2. The space $\widetilde{M}_1' = S^3 \setminus (D_1^3 \cup D_2^3)$ is homeomorphic to the cylinder $S^2 \times [-1, 1]$, which deformation retracts to $S^2$.
    <2>3. The Cayley graph of the group $G = \mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/2\mathbb{Z}$ with respect to the generators $\{a, b\}$ is an infinite line (a 1D tree with vertices indexed by $\mathbb{Z}$).
    <2>4. The universal cover $\widetilde{X}$ is the tree-like plumbing of building blocks according to the Cayley tree: it is formed by gluing countably infinitely many copies of $S^2 \times [-1, 1]$ end-to-end along their boundary 2-spheres.
    <2>5. Collapsing the cylinder intervals gives a homeomorph/deformation retraction of the entire infinite chain to
    $$\widetilde{X} \cong S^2 \times \mathbb{R}.$$
    <2>6. Thus the universal cover $\widetilde{X}$ is homeomorphic to $S^2 \times \mathbb{R}$, which deformation retracts to $S^2$.

<1>3. Computation of $\pi_2(X)$:
    *Proof:*
    <2>1. For any covering space $p: \widetilde{X} \to X$, the induced homomorphism on homotopy groups $p_*: \pi_k(\widetilde{X}) \to \pi_k(X)$ is an isomorphism for all $k \ge 2$.
    <2>2. In particular, for $k = 2$:
    $$\pi_2(X) \cong \pi_2(\widetilde{X}).$$
    <2>3. Since $\widetilde{X} \simeq S^2 \times \mathbb{R} \simeq S^2$:
    $$\pi_2(\widetilde{X}) \cong \pi_2(S^2 \times \mathbb{R}) \cong \pi_2(S^2) \oplus \pi_2(\mathbb{R}) \cong \mathbb{Z} \oplus 0 \cong \mathbb{Z}.$$
    <2>4. Therefore $\pi_2(X) \cong \mathbb{Z}$.

<1>4. Conclusion:
    *Proof:*
    $\pi_1(X) \cong \mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/2\mathbb{Z}$, the universal cover is $\widetilde{X} \cong S^2 \times \mathbb{R} \simeq S^2$, and $\pi_2(X) \cong \mathbb{Z}$.
:::
