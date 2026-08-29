---
schema: qual/card@1
id: P-XAQEZ
kind: problem
title: Homology of $\RP^2$ via Mayer-Vietoris
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the integer homology groups $H_*(\mathbb{RP}^2; \mathbb{Z})$ using the **Mayer–Vietoris sequence** by decomposing $\mathbb{RP}^2$ as the union of a Möbius strip $M$ and a 2-disk $D^2$ along their boundary circle $\partial M = S^1$.
:::

::: solution
**Goal:** Compute $H_*(\mathbb{RP}^2; \mathbb{Z})$ via the Mayer–Vietoris exact sequence associated to the decomposition $\mathbb{RP}^2 = M \cup_{S^1} D^2$.

<1>1. Decomposition of $\mathbb{RP}^2$:
    *Proof:*
    <2>1. The real projective plane $\mathbb{RP}^2$ can be decomposed into two open neighborhoods (or deformation retracts) $A = M$ (Möbius band) and $B = D^2$ (topological 2-disk).
    <2>2. Their intersection is their common boundary circle:
        $$A \cap B = M \cap D^2 = \partial M = S^1.$$
    <2>3. Their union is the entire space:
        $$A \cup B = M \cup_{S^1} D^2 = \mathbb{RP}^2.$$

<1>2. Homology Groups of the Pieces:
    *Proof:*
    <2>1. **For $A \cap B = S^1$:**
        $$H_0(S^1) \cong \mathbb{Z}, \quad H_1(S^1) \cong \mathbb{Z}, \quad H_k(S^1) = 0 \text{ for } k \ge 2.$$
    <2>2. **For $A = M$ (Möbius band):**
        $M$ deformation retracts onto its central core circle $S^1$, so:
        $$H_0(M) \cong \mathbb{Z}, \quad H_1(M) \cong \mathbb{Z}, \quad H_k(M) = 0 \text{ for } k \ge 2.$$
    <2>3. **For $B = D^2$ (Disk):**
        $D^2$ is contractible ($D^2 \simeq \{*\}$), so:
        $$H_0(D^2) \cong \mathbb{Z}, \quad H_k(D^2) = 0 \text{ for } k \ge 1.$$

<1>3. Induced Maps on Homology:
    *Proof:*
    <2>1. Let $i: S^1 \hookrightarrow M$ and $j: S^1 \hookrightarrow D^2$ be the inclusion maps.
    <2>2. In degree 1:
        - The boundary circle $\partial M = S^1$ wraps **twice** around the central core circle of the Möbius strip $M$. Thus the induced map on $H_1 \cong \mathbb{Z}$ is multiplication by 2:
          $$i_*: H_1(S^1) \longrightarrow H_1(M), \qquad 1 \longmapsto 2.$$
        - For the disk, $H_1(D^2) = 0$, so $j_*: H_1(S^1) \to H_1(D^2)$ is the zero map:
          $$j_*: H_1(S^1) \longrightarrow H_1(D^2) = 0, \qquad 1 \longmapsto 0.$$
        - Thus $(i_*, -j_*)_1: \mathbb{Z} \to \mathbb{Z} \oplus 0$ is given by $x \mapsto (2x, 0)$.
    <2>3. In degree 0:
        - Both $M$ and $D^2$ are path-connected, so $i_*: H_0(S^1) \to H_0(M)$ and $j_*: H_0(S^1) \to H_0(D^2)$ are isomorphisms $\mathbb{Z} \to \mathbb{Z}$ sending $1 \mapsto 1$.
        - Thus $(i_*, -j_*)_0: \mathbb{Z} \to \mathbb{Z} \oplus \mathbb{Z}$ is given by $x \mapsto (x, -x)$, which is injective with image of rank 1.

<1>4. Mayer–Vietoris Exact Sequence Analysis:
    *Proof:*
    <2>1. **For $k \ge 3$:**
        $$0 = H_k(M) \oplus H_k(D^2) \longrightarrow H_k(\mathbb{RP}^2) \longrightarrow H_{k-1}(S^1) = 0 \implies H_k(\mathbb{RP}^2) = 0.$$
    <2>2. **For $k = 2$:**
        $$0 = H_2(M) \oplus H_2(D^2) \longrightarrow H_2(\mathbb{RP}^2) \xrightarrow{\partial_*} H_1(S^1) \xrightarrow{(i_*, -j_*)_1} H_1(M) \oplus H_1(D^2).$$
        Substituting the groups and maps:
        $$0 \longrightarrow H_2(\mathbb{RP}^2) \xrightarrow{\partial_*} \mathbb{Z} \xrightarrow{x \mapsto (2x, 0)} \mathbb{Z} \oplus 0.$$
        Since $x \mapsto (2x, 0)$ is injective ($\ker = 0$), exactness forces $\operatorname{im}(\partial_*) = \ker(i_*, -j_*)_1 = 0$.
        Since $\partial_*$ is injective ($\ker(\partial_*) = 0$), this gives:
        $$H_2(\mathbb{RP}^2) \cong 0.$$
    <2>3. **For $k = 1$:**
        $$H_1(S^1) \xrightarrow{x \mapsto (2x, 0)} H_1(M) \oplus H_1(D^2) \xrightarrow{\Phi} H_1(\mathbb{RP}^2) \xrightarrow{\partial_*} H_0(S^1) \xrightarrow{x \mapsto (x, -x)} H_0(M) \oplus H_0(D^2).$$
        - Since $x \mapsto (x, -x)$ is injective, $\ker(i_*, -j_*)_0 = 0$, so $\operatorname{im}(\partial_*) = 0 \implies \partial_* = 0$.
        - Therefore, $\Phi: H_1(M) \oplus H_1(D^2) \to H_1(\mathbb{RP}^2)$ is **surjective**.
        - By exactness at $H_1(M) \oplus H_1(D^2) = \mathbb{Z} \oplus 0$:
          $$\ker(\Phi) = \operatorname{im}(i_*, -j_*)_1 = 2\mathbb{Z} \oplus 0.$$
        - By the First Isomorphism Theorem:
          $$H_1(\mathbb{RP}^2) \cong \frac{H_1(M) \oplus H_1(D^2)}{\operatorname{im}(i_*, -j_*)_1} = \frac{\mathbb{Z} \oplus 0}{2\mathbb{Z} \oplus 0} \cong \mathbb{Z}/2\mathbb{Z}.$$
    <2>4. **For $k = 0$:**
        Since $\mathbb{RP}^2$ is path-connected:
        $$H_0(\mathbb{RP}^2) \cong \mathbb{Z}.$$

<1>5. Conclusion:
    $$H_k(\mathbb{RP}^2; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & \text{if } k = 0, \\ \mathbb{Z}/2\mathbb{Z} & \text{if } k = 1, \\ 0 & \text{if } k \ge 2. \end{cases}$$
    Q.E.D.
:::
