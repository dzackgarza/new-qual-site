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

::: {.problem}
The Euler characteristic $\chi(X)$ of a space $X$ is defined as the alternating sum of the dimensions of the rational homology groups $H_i(X; \mathbb{Q})$.
Use Poincaré duality to show that the Euler characteristic of a compact connected closed orientable $3$-manifold $M^3$ is zero.
Prove that the result still holds even if $M$ is non-orientable.
:::

::: {.solution}
**Case 1: $M^3$ is orientable:**

::: pf

::: pf-step
Let $b_i = \dim_{\mathbb{Q}} H_i(M; \mathbb{Q})$ denote the $i$-th Betti number of $M$.

::: pf-proof

::: pf-step
Since $M$ is a compact 3-manifold without boundary, $b_i = 0$ for all $i > 3$.

::: pf-proof
dimension of manifold is 3.
:::

:::

::: pf-step
The Euler characteristic is:
\[
\chi(M) = b_0 - b_1 + b_2 - b_3.
\]

::: pf-proof
definition of Euler characteristic.
:::

:::

:::

:::

::: {.pf-step #s2}
Apply Poincaré Duality over the field $\mathbb{Q}$:

::: pf-proof

::: {.pf-step #s2-1}
Since $M$ is closed and orientable, Poincaré Duality gives an isomorphism $H_i(M; \mathbb{Q}) \cong H^{3-i}(M; \mathbb{Q})$ for each $i$.

::: pf-proof
Poincaré Duality Theorem for compact orientable manifolds.
:::

:::

::: pf-step
By the Universal Coefficient Theorem for cohomology with field coefficients:
\[
H^k(M; \mathbb{Q}) \cong \operatorname{Hom}_{\mathbb{Q}}(H_k(M; \mathbb{Q}), \mathbb{Q}).
\]

::: pf-proof
Universal Coefficient Theorem over a field (Ext vanishes).
:::

:::

::: {.pf-step #s2-3}
Thus $\dim_{\mathbb{Q}} H^k(M; \mathbb{Q}) = \dim_{\mathbb{Q}} H_k(M; \mathbb{Q}) = b_k$.

::: pf-proof
finite-dimensional vector spaces are isomorphic to their duals.
:::

:::

::: pf-step
Combining step [](#s2-1){.pf-ref} and step [](#s2-3){.pf-ref} gives $b_i = b_{3-i}$ for all $i \in \{0, 1, 2, 3\}$.

::: pf-proof
$b_i = \dim H_i(M; \mathbb{Q}) = \dim H^{3-i}(M; \mathbb{Q}) = b_{3-i}$.
:::

:::

:::

:::

::: {.pf-step #s3}
Compute $\chi(M)$:
\[
\chi(M) = b_0 - b_1 + b_2 - b_3 = b_0 - b_1 + b_1 - b_0 = 0.
\]

::: pf-proof
$b_3 = b_0$ and $b_2 = b_1$ from step [](#s2){.pf-ref}.
:::

:::

:::

**Case 2: $M^3$ is non-orientable:**

::: pf

::: {.pf-step #s4}
Method 1: Via the orientation double cover $\widetilde{M}$:

::: pf-proof

::: pf-step
Every connected non-orientable manifold $M$ has a connected 2-sheeted orientation covering space $p: \widetilde{M} \to M$, where $\widetilde{M}$ is a closed, connected, orientable 3-manifold.

::: pf-proof
construction of the orientation covering.
:::

:::

::: pf-step
The Euler characteristic is multiplicative under finite covering spaces:
\[
\chi(\widetilde{M}) = d \cdot \chi(M) = 2 \chi(M).
\]

::: pf-proof
Euler characteristic of a $d$-sheeted covering space of a finite CW complex satisfies $\chi(\widetilde{M}) = d\chi(M)$.
:::

:::

::: pf-step
Since $\widetilde{M}$ is a closed orientable 3-manifold, $\chi(\widetilde{M}) = 0$ by step [](#s3){.pf-ref}.

::: pf-proof
Case 1 applied to $\widetilde{M}$.
:::

:::

::: pf-step
Hence $2 \chi(M) = 0 \implies \chi(M) = 0$.

::: pf-proof
division by 2 in $\mathbb{Q}$.
:::

:::

:::

:::

::: {.pf-step #s5}
Method 2: Via $\mathbb{Z}_2$-Poincaré Duality:

::: pf-proof

::: pf-step
Over the field $\mathbb{Z}_2$, every closed manifold is orientable, so Poincaré Duality gives $H_i(M; \mathbb{Z}_2) \cong H^{3-i}(M; \mathbb{Z}_2) \cong H_{3-i}(M; \mathbb{Z}_2)^*$.

::: pf-proof
$\mathbb{Z}_2$-Poincaré Duality.
:::

:::

::: {.pf-step #s5-2}
Thus $\dim_{\mathbb{Z}_2} H_i(M; \mathbb{Z}_2) = \dim_{\mathbb{Z}_2} H_{3-i}(M; \mathbb{Z}_2)$ for all $i$.

::: pf-proof
vector space duality over $\mathbb{Z}_2$.
:::

:::

::: pf-step
By the Universal Coefficient Theorem, the mod-2 Euler characteristic equals the rational Euler characteristic:
\[
\chi(M) = \chi_2(M) = \sum_{i=0}^3 (-1)^i \dim_{\mathbb{Z}_2} H_i(M; \mathbb{Z}_2).
\]

::: pf-proof
Universal Coefficient Theorem torsion cancellation for Euler characteristics.
:::

:::

::: pf-step
By symmetry, $\chi_2(M) = \dim_{\mathbb{Z}_2} H_0 - \dim_{\mathbb{Z}_2} H_1 + \dim_{\mathbb{Z}_2} H_1 - \dim_{\mathbb{Z}_2} H_0 = 0$.

::: pf-proof
step [](#s5-2){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion: $\chi(M) = 0$ for every compact closed 3-manifold $M$, whether orientable or non-orientable.

::: pf-proof
step [](#s3){.pf-ref}, step [](#s4){.pf-ref}, and step [](#s5){.pf-ref}.
:::

:::

:::
:::
