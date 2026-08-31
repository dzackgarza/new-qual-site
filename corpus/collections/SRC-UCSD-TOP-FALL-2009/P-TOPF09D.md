---
schema: qual/card@1
id: P-TOPF09D
kind: problem
title: "Euler characteristic of a compact connected closed 3-manifold is zero (orientable and non-orientable)"
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Poincaré Duality
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
The Euler characteristic $\chi(X)$ of a space $X$ is defined as the alternating sum of the dimensions of the rational homology groups $H_i(X; \mathbb{Q})$.
Use Poincaré duality to show that the Euler characteristic of a compact connected closed orientable $3$-manifold $M^3$ is zero.
Prove that the result still holds even if $M$ is non-orientable.
:::

::: {.solution}
**Case 1: $M^3$ is orientable:**

<1>1. Let $b_i = \dim_{\mathbb{Q}} H_i(M; \mathbb{Q})$ denote the $i$-th Betti number of $M$.
<2>1. Since $M$ is a compact 3-manifold without boundary, $b_i = 0$ for all $i > 3$.
::: {.proof}
dimension of manifold is 3. <2>2. The Euler characteristic is:
:::
\[
\chi(M) = b_0 - b_1 + b_2 - b_3.
\]
::: {.proof}
definition of Euler characteristic.
:::

<1>2. Apply Poincaré Duality over the field $\mathbb{Q}$: <2>1. Since $M$ is closed and orientable, Poincaré Duality gives an isomorphism $H_i(M; \mathbb{Q}) \cong H^{3-i}(M; \mathbb{Q})$ for each $i$.
::: {.proof}
Poincaré Duality Theorem for compact orientable manifolds.
:::
<2>2. By the Universal Coefficient Theorem for cohomology with field coefficients:
\[
H^k(M; \mathbb{Q}) \cong \operatorname{Hom}_{\mathbb{Q}}(H_k(M; \mathbb{Q}), \mathbb{Q}).
\]
::: {.proof}
Universal Coefficient Theorem over a field (Ext vanishes).
:::
<2>3. Thus $\dim_{\mathbb{Q}} H^k(M; \mathbb{Q}) = \dim_{\mathbb{Q}} H_k(M; \mathbb{Q}) = b_k$.
::: {.proof}
finite-dimensional vector spaces are isomorphic to their duals.
:::
<2>4. Combining <2>1 and <2>3 gives $b_i = b_{3-i}$ for all $i \in \{0, 1, 2, 3\}$.
::: {.proof}
$b_i = \dim H_i(M; \mathbb{Q}) = \dim H^{3-i}(M; \mathbb{Q}) = b_{3-i}$.
:::

<1>3. Compute $\chi(M)$:
\[
\chi(M) = b_0 - b_1 + b_2 - b_3 = b_0 - b_1 + b_1 - b_0 = 0.
\]
::: {.proof}
$b_3 = b_0$ and $b_2 = b_1$ from <1>2.
:::

**Case 2: $M^3$ is non-orientable:**

<1>4. Method 1: Via the orientation double cover $\widetilde{M}$: <2>1. Every connected non-orientable manifold $M$ has a connected 2-sheeted orientation covering space $p: \widetilde{M} \to M$, where $\widetilde{M}$ is a closed, connected, orientable 3-manifold.
::: {.proof}
construction of the orientation covering.
:::
<2>2. The Euler characteristic is multiplicative under finite covering spaces:
\[
\chi(\widetilde{M}) = d \cdot \chi(M) = 2 \chi(M).
\]
::: {.proof}
Euler characteristic of a $d$-sheeted covering space of a finite CW complex satisfies $\chi(\widetilde{M}) = d\chi(M)$.
:::
<2>3. Since $\widetilde{M}$ is a closed orientable 3-manifold, $\chi(\widetilde{M}) = 0$ by <1>3.
::: {.proof}
Case 1 applied to $\widetilde{M}$.
:::
<2>4. Hence $2 \chi(M) = 0 \implies \chi(M) = 0$.
::: {.proof}
division by 2 in $\mathbb{Q}$.
:::

<1>5. Method 2: Via $\mathbb{Z}_2$-Poincaré Duality: <2>1. Over the field $\mathbb{Z}_2$, every closed manifold is orientable, so Poincaré Duality gives $H_i(M; \mathbb{Z}_2) \cong H^{3-i}(M; \mathbb{Z}_2) \cong H_{3-i}(M; \mathbb{Z}_2)^*$.
::: {.proof}
$\mathbb{Z}_2$-Poincaré Duality.
:::
<2>2. Thus $\dim_{\mathbb{Z}_2} H_i(M; \mathbb{Z}_2) = \dim_{\mathbb{Z}_2} H_{3-i}(M; \mathbb{Z}_2)$ for all $i$.
::: {.proof}
vector space duality over $\mathbb{Z}_2$.
:::
<2>3. By the Universal Coefficient Theorem, the mod-2 Euler characteristic equals the rational Euler characteristic:
\[
\chi(M) = \chi_2(M) = \sum_{i=0}^3 (-1)^i \dim_{\mathbb{Z}_2} H_i(M; \mathbb{Z}_2).
\]
::: {.proof}
Universal Coefficient Theorem torsion cancellation for Euler characteristics.
:::
<2>4. By symmetry, $\chi_2(M) = \dim_{\mathbb{Z}_2} H_0 - \dim_{\mathbb{Z}_2} H_1 + \dim_{\mathbb{Z}_2} H_1 - \dim_{\mathbb{Z}_2} H_0 = 0$.
::: {.proof}
<2>2.
:::

<1>6. Conclusion: $\chi(M) = 0$ for every compact closed 3-manifold $M$, whether orientable or non-orientable.
::: {.proof}
<1>3, <1>4, and <1>5.
:::
Q.E.D.
:::
