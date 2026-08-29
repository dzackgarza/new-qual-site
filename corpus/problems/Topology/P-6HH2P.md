---
schema: qual/card@1
id: P-6HH2P
kind: problem
title: A manifold is orientable if $\pi_1$ has no subgroup of index $2$
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
Let $M$ be a connected topological/smooth manifold.
Prove that if the fundamental group $\pi_1(M)$ has no subgroup of index 2, then $M$ is **orientable**.
:::

::: solution
**Goal:** Prove that a connected manifold $M$ with no index-2 subgroup in $\pi_1(M)$ is orientable via the orientation double cover.

<1>1. The Orientation Double Cover $\tilde{M} \to M$:
    *Proof:*
    <2>1. Every connected manifold $M$ of dimension $n$ admits a canonical **orientation double cover** $p: \tilde{M} \to M$.
    <2>2. The points of $\tilde{M}$ are pairs $(x, \mu_x)$ where $x \in M$ and $\mu_x$ is a local orientation of $M$ at $x$ (a generator of $H_n(M, M \setminus \{x\}; \mathbb{Z}) \cong \mathbb{Z}$).
    <2>3. Since there are exactly 2 choices of orientation $\pm \mu_x$ at each point, the projection $p: \tilde{M} \to M$ given by $p(x, \mu_x) = x$ is a **2-sheeted covering space**.
    <2>4. The total space $\tilde{M}$ is always an **orientable manifold**.

<1>2. Orientability and Connectedness of $\tilde{M}$:
    *Proof:*
    <2>1. The manifold $M$ is **orientable** if and only if the orientation double cover $\tilde{M}$ is disconnected (consisting of two disjoint homeomorphic copies of $M$, $M \sqcup M$).
    <2>2. Conversely, $M$ is **non-orientable** if and only if $\tilde{M}$ is **connected**.

<1>3. Covering Space Classification and Subgroups of $\pi_1(M)$:
    *Proof:*
    <2>1. Suppose, for contradiction, that $M$ is **non-orientable**.
    <2>2. Then the orientation double cover $p: \tilde{M} \to M$ is a **connected 2-sheeted covering space**.
    <2>3. By the Galois correspondence / Classification of Covering Spaces:
        - Connected covering spaces $p: \tilde{M} \to M$ correspond bijectively to conjugacy classes of subgroups $H \le \pi_1(M)$.
        - The number of sheets of the cover is equal to the index of the subgroup:
            $$\text{Number of sheets} = [\pi_1(M) : p_*(\pi_1(\tilde{M}))] = 2.$$
    <2>4. Thus $H \coloneqq p_*(\pi_1(\tilde{M}))$ is a **subgroup of index 2** in $\pi_1(M)$ (which is automatically normal, with quotient $\pi_1(M)/H \cong \mathbb{Z}_2$, corresponding to the first Stiefel-Whitney class $w_1(M) \in H^1(M; \mathbb{Z}_2) \cong \operatorname{Hom}(\pi_1(M), \mathbb{Z}_2)$).
    <2>5. However, this directly contradicts the hypothesis that $\pi_1(M)$ has **no subgroup of index 2**!

<1>4. Conclusion:
    The orientation double cover cannot be connected, so $\tilde{M} \cong M \sqcup M$, which implies that $M$ is orientable. Q.E.D.
:::
