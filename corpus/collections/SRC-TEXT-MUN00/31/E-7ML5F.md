---
schema: qual/card@1
id: E-7ML5F
kind: problem
title: Separation axioms under refinement of topologies
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ and $X'$ denote a single set under two topologies $\mathcal{T}$ and $\mathcal{T}'$, respectively; assume that $\mathcal{T}' \supset \mathcal{T}$.
If one of the spaces is Hausdorff (or regular, or normal), what does that imply about the other?
:::

::: solution
**Goal:** Determine which separation properties (Hausdorff, regular, normal) are preserved when passing to a finer topology ($\mathcal{T} \subset \mathcal{T}'$) or a coarser topology ($\mathcal{T}' \supset \mathcal{T}$), providing proofs and counterexamples.

<1>1. Hausdorff property ($T_2$):
    - If $(X, \mathcal{T})$ is Hausdorff, then $(X, \mathcal{T}')$ is Hausdorff.
    - If $(X, \mathcal{T}')$ is Hausdorff, $(X, \mathcal{T})$ need not be Hausdorff.
    *Proof:*
    <2>1. **Forward preservation:** Suppose $(X, \mathcal{T})$ is Hausdorff. For any distinct $x \neq y \in X$, there exist disjoint open sets $U, V \in \mathcal{T}$ with $x \in U$ and $y \in V$. Since $\mathcal{T} \subset \mathcal{T}'$, $U, V \in \mathcal{T}'$, so $(X, \mathcal{T}')$ is Hausdorff.
    <2>2. **Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is Hausdorff, but the coarser cofinite topology $\mathcal{T}$ on $X$ is not Hausdorff.

<1>2. Regular property ($T_3$):
    Neither direction holds:
    - $(X, \mathcal{T})$ regular does NOT imply $(X, \mathcal{T}')$ is regular.
    - $(X, \mathcal{T}')$ regular does NOT imply $(X, \mathcal{T})$ is regular.
    *Proof:*
    <2>1. **Forward failure:** The standard Euclidean topology $\mathcal{T}$ on $\mathbb{R}$ is regular (and metric). The $K$-topology $\mathcal{T}' = \mathcal{T}_K$ is strictly finer than $\mathcal{T}$, but $(\mathbb{R}, \mathcal{T}_K)$ is not regular because the closed set $K = \{1/n \mid n \in \mathbb{Z}_+\}$ and the point $0 \notin K$ cannot be separated by disjoint open sets in $\mathcal{T}_K$.
    <2>2. **Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is regular, but the coarser cofinite topology $\mathcal{T}$ is not regular.

<1>3. Normal property ($T_4$):
    Neither direction holds:
    - $(X, \mathcal{T})$ normal does NOT imply $(X, \mathcal{T}')$ is normal.
    - $(X, \mathcal{T}')$ normal does NOT imply $(X, \mathcal{T})$ is normal.
    *Proof:*
    <2>1. **Forward failure:** The standard Euclidean topology $\mathcal{T}$ on $\mathbb{R}$ is normal, but the strictly finer $K$-topology $\mathcal{T}_K$ is not even regular, and therefore not normal.
    <2>2. **Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is normal, but the coarser cofinite topology $\mathcal{T}$ is not normal (it is not even Hausdorff).

<1>4. Summary Table of Implications:
    - **Hausdorff:** Coarser $\implies$ Finer (yes); Finer $\implies$ Coarser (no).
    - **Regular:** Coarser $\implies$ Finer (no); Finer $\implies$ Coarser (no).
    - **Normal:** Coarser $\implies$ Finer (no); Finer $\implies$ Coarser (no).
    Q.E.D.
:::
