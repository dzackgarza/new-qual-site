---
schema: qual/card@1
id: P-VTB25
kind: problem
title: Even-degree orientable covers of non-orientable manifolds, and $\pi_1$ without
  index-$2$ subgroups
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Covering Spaces
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $M$ be a connected topological manifold.
(1) Prove that if $\widetilde{M}$ is an orientable connected manifold and $p: \widetilde{M} \to M$ is a $k$-fold covering map onto a **non-orientable** manifold $M$, then the covering degree $k$ must be **even** (or infinite).
(2) Prove that if $\pi_1(M)$ has no subgroup of index $2$, then $M$ must be **orientable**.
:::

::: solution
**Goal:** Prove that orientable covers of non-orientable manifolds have even degree, and that the absence of index-2 subgroups forces orientability via the orientation double cover.

<1>1. The Orientation Double Cover $\widehat{M} \to M$:
    *Proof:*
    <2>1. For any connected manifold $M$, there exists a canonical **orientation covering** $\pi_{\text{orient}}: \widehat{M} \to M$ of degree 2:
        $$\widehat{M} \coloneqq \{(x, \mu_x) \mid x \in M, \; \mu_x \text{ is a local orientation of } M \text{ at } x \in H_n(M, M \setminus \{x\}; \mathbb{Z}) \cong \mathbb{Z}\}.$$
    <2>2. The total space $\widehat{M}$ is always an **orientable manifold**.
    <2>3. $M$ is **orientable** if and only if $\widehat{M}$ is disconnected ($\widehat{M} \cong M \sqcup M$).
    <2>4. $M$ is **non-orientable** if and only if $\widehat{M}$ is **connected**, in which case $\pi_{\text{orient}}: \widehat{M} \to M$ is a connected 2-fold covering space corresponding to an index-2 subgroup $H_{\text{orient}} = \pi_*(\pi_1(\widehat{M})) \le \pi_1(M)$.

<1>2. Part 1: Orientable Cover of Non-Orientable Manifold Has Even Degree:
    *Proof:*
    <2>1. Let $p: \widetilde{M} \to M$ be a $k$-fold connected covering map with $\widetilde{M}$ orientable and $M$ non-orientable.
    <2>2. The orientation character of $M$ is the non-trivial homomorphism:
        $$w_1: \pi_1(M) \longrightarrow \{\pm 1\} \cong \mathbb{Z}_2$$
        whose kernel is $H_{\text{orient}} = \ker(w_1) \le \pi_1(M)$ of index 2.
    <2>3. A covering space $q: E \to M$ corresponding to subgroup $H \le \pi_1(M)$ is **orientable** if and only if every loop in $E$ preserves orientation on $M$, which means:
        $$H \subseteq \ker(w_1) = H_{\text{orient}}.$$
    <2>4. Since $\widetilde{M}$ is orientable, its characteristic subgroup $H = p_*(\pi_1(\widetilde{M})) \le \pi_1(M)$ satisfies:
        $$H \subseteq H_{\text{orient}} \subsetneq \pi_1(M).$$
    <2>5. By the Tower Law for subgroup indices:
        $$k = [\pi_1(M) : H] = [\pi_1(M) : H_{\text{orient}}] \cdot [H_{\text{orient}} : H] = 2 \cdot [H_{\text{orient}} : H].$$
    <2>6. Therefore, $k$ is an integer multiple of 2, so $k$ is **even** (or infinite if $[H_{\text{orient}} : H] = \infty$).

<1>3. Part 2: Manifolds with No Index 2 Subgroup are Orientable:
    *Proof:*
    <2>1. Suppose, for contradiction, that $M$ is non-orientable.
    <2>2. By Step <1>1, the orientation double cover $\widehat{M}$ is **connected**.
    <2>3. By the Galois correspondence for covering spaces, the connected 2-fold cover $\pi_{\text{orient}}: \widehat{M} \to M$ corresponds to a subgroup:
        $$H_{\text{orient}} = (\pi_{\text{orient}})_*(\pi_1(\widehat{M})) \le \pi_1(M)$$
        of exact index $[\pi_1(M) : H_{\text{orient}}] = 2$.
    <2>4. This provides an explicit **subgroup of index 2** in $\pi_1(M)$.
    <2>5. But this directly contradicts the hypothesis that $\pi_1(M)$ has **no subgroup of index 2**.
    <2>6. Therefore, $M$ must be **orientable**.

<1>4. Conclusion:
    Subgroups of orientable covers factor through $\ker(w_1)$ forcing $2 \mid k$, and non-orientability guarantees an index 2 subgroup $\ker(w_1) \le \pi_1(M)$. Q.E.D.
:::
