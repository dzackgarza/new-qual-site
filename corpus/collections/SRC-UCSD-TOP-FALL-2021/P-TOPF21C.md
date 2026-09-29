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

::: {.problem}
Let $X$ be a $3$-dimensional simply-connected closed manifold (compact, no boundary).
Show that $X$ is homotopy equivalent to $S^3$.
:::

::: {.solution}
**Goal:** Prove that every closed, simply connected 3-manifold $X$ is homotopy equivalent to $S^3$ using algebraic topology.

::: pf

::: pf-step
Homology groups of $X$:

::: pf-proof

::: pf-step
Since $X$ is connected, $H_0(X; \mathbb{Z}) \cong \mathbb{Z}$.
:::

::: pf-step
Since $X$ is simply connected ($\pi_1(X) = 0$), the Hurewicz Theorem (or abelianization) gives:
$$H_1(X; \mathbb{Z}) \cong \pi_1(X)_{\text{ab}} = 0.$$
:::

::: pf-step
Since $\pi_1(X) = 0$, the first Stiefel–Whitney class vanishes ($w_1(X) = 0$), so $X$ is orientable.
:::

::: pf-step
For a closed, connected, oriented 3-manifold, the top homology is $H_3(X; \mathbb{Z}) \cong \mathbb{Z}$, and $H_k(X; \mathbb{Z}) = 0$ for all $k > 3$.
:::

::: pf-step
By Poincaré Duality:
$$H_2(X; \mathbb{Z}) \cong H^1(X; \mathbb{Z}).$$
:::

::: pf-step
By the Universal Coefficient Theorem for cohomology:
$$H^1(X; \mathbb{Z}) \cong \operatorname{Hom}(H_1(X; \mathbb{Z}), \mathbb{Z}) \oplus \operatorname{Ext}(H_0(X; \mathbb{Z}), \mathbb{Z}) \cong \operatorname{Hom}(0, \mathbb{Z}) \oplus \operatorname{Ext}(\mathbb{Z}, \mathbb{Z}) = 0 \oplus 0 = 0.$$
:::

::: pf-step
Thus $H_2(X; \mathbb{Z}) = 0$.
:::

::: pf-step
In summary, the homology of $X$ matches the homology of $S^3$:
$$H_k(X; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & k = 0, 3, \\ 0 & k \neq 0, 3. \end{cases}$$
:::

:::

:::

::: pf-step
Homotopy groups via the Hurewicz Theorem:

::: pf-proof

::: pf-step
Since $\pi_1(X) = 0$ and $\widetilde{H}_1(X) = \widetilde{H}_2(X) = 0$, the Hurewicz Theorem in dimension 2 implies $\pi_2(X) \cong H_2(X; \mathbb{Z}) = 0$.
:::

::: pf-step
By the Hurewicz Theorem in dimension 3 for simply connected spaces, the Hurewicz homomorphism
$$h: \pi_3(X) \to H_3(X; \mathbb{Z}) \cong \mathbb{Z}$$
is an isomorphism.
:::

::: pf-step
Thus $\pi_3(X) \cong \mathbb{Z}$.
:::

:::

:::

::: pf-step
Homotopy equivalence via Whitehead's Theorem:

::: pf-proof

::: pf-step
Choose a continuous map $f: S^3 \to X$ representing a generator of $\pi_3(X) \cong \mathbb{Z}$.
:::

::: pf-step
By definition of the Hurewicz homomorphism, the induced map $f_*: H_3(S^3; \mathbb{Z}) \to H_3(X; \mathbb{Z})$ sends the fundamental class $[S^3]$ to $h([f])$, which is a generator of $H_3(X; \mathbb{Z})$.
:::

::: pf-step
Thus $f_*: H_3(S^3; \mathbb{Z}) \to H_3(X; \mathbb{Z})$ is an isomorphism.
:::

::: pf-step
In degree 0, $f_*: H_0(S^3; \mathbb{Z}) \to H_0(X; \mathbb{Z})$ is an isomorphism $\mathbb{Z} \to \mathbb{Z}$ since $S^3$ and $X$ are non-empty and connected.
:::

::: pf-step
In all other degrees $k \neq 0, 3$, $H_k(S^3) = H_k(X) = 0$, so $f_*\colon 0 \to 0$ is an isomorphism.
:::

::: pf-step
By Moise's Theorem, every 3-manifold admits a triangulation as a finite simplicial complex, so $X$ is a finite CW complex.
:::

::: pf-step
By Whitehead's Theorem for simply connected CW complexes, a continuous map inducing isomorphisms on all homology groups is a homotopy equivalence.
:::

::: pf-step
Therefore $f: S^3 \to X$ is a homotopy equivalence, so $X \simeq S^3$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
Every closed simply connected 3-manifold $X$ is homotopy equivalent to $S^3$.
:::

:::

:::
:::
