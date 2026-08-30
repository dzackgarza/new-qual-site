---
schema: qual/card@1
id: P-USPU6
kind: problem
title: A finite abelian group is the product of its Sylow subgroups
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
- Show that any finite abelian group is isomorphic to the direct product of its Sylow subgroups
:::

::: solution
**Goal:** Prove $G \cong \prod_{p} G_p$ for finite abelian $G$.

<1> Decompose via the fundamental theorem.
    *Proof:*
    <2>1. Write
        $$G \cong \bigoplus_{i=1}^r C_{n_i}, \quad n_i = \prod_{p\mid |G|} p^{a_{i,p}},$$
        by the finite abelian classification theorem.
    <2>2. For each prime $p\mid |G|$, define
        $$G_p:=\{g\in G\mid |g|\ \text{is a power of }p\}.$$
    <2>3. In the decomposition above, $G_p$ is the direct sum of the $p$-power cyclic factors.

<1> Reassemble from the prime components.
    *Proof:*
    <2>1. The map
        $$\Phi:\prod_{p\mid |G|} G_p \to G,\qquad (g_p)_p\mapsto \sum_p g_p$$
        is a homomorphism.
    <2>2. $\Phi$ is injective because the intersection $G_p\cap G_q=\{e\}$ for $p\neq q$.
    <2>3. $\Phi$ is surjective because every cyclic factor $C_{n_i}$ splits as a direct product of its prime-power factors.
    <2>4. Therefore $\Phi$ is an isomorphism.

<1> Hence $G$ is the direct product of its Sylow subgroups.  
    Q.E.D.

Authored by **Codex 5.3 Spark Extra High**.
:::
