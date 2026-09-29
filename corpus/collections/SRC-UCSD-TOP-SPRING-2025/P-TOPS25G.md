---
schema: qual/card@1
id: P-TOPS25G
kind: problem
title: No compact 4-manifold homotopy equivalent to $\Sigma\mathbb{RP}^3$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Prove that there is no compact 4-manifold $M$ (with or without boundary) which is homotopy-equivalent to the suspension $\Sigma\mathbb{RP}^3$.
:::

::: {.solution}
**Goal.** Show no compact $4$-manifold is homotopy equivalent to $\Sigma \RP^3$.

::: pf

::: pf-step
Compute the homology of $\Sigma \RP^3$.

::: pf-proof

::: pf-step
$\tilde H_i(\Sigma X) \cong \tilde H_{i-1}(X)$.

::: pf-proof
the suspension isomorphism for reduced homology.
:::

:::

::: pf-step
$H_*(\RP^3) = \ZZ, \ZZ/2, 0, \ZZ$ in degrees $0, 1, 2, 3$.

::: pf-proof
standard homology of $\RP^3$.
:::

:::

::: {.pf-step #s1-3}
Hence $H_*(\Sigma \RP^3) = \ZZ, 0, \ZZ/2, 0, \ZZ$ in degrees $0, 1, 2, 3, 4$.

::: pf-proof
apply the suspension isomorphism: $H_1 = \tilde H_0(\RP^3) = 0$, $H_2 = \tilde H_1(\RP^3) = \ZZ/2$, $H_3 = \tilde H_2(\RP^3) = 0$, $H_4 = \tilde H_3(\RP^3) = \ZZ$.
:::

:::

:::

:::

::: pf-step
A compact $4$-manifold homotopy equivalent to $\Sigma \RP^3$ would have $H_2(M;\ZZ) = \ZZ/2$ and $H_4(M;\ZZ) = \ZZ$.

::: pf-proof
homotopy equivalence preserves homology.
:::

:::

::: pf-step
$H_4(M;\ZZ) = \ZZ$ forces $M$ to be closed and orientable.

::: pf-proof

::: pf-step
If $M$ has nonempty boundary, then $H_4(M;\ZZ) = 0$.

::: pf-proof
for a connected compact $4$-manifold with nonempty boundary, absolute top homology vanishes. For example, in the orientable case the relative fundamental class $[M,\partial M]\in H_4(M,\partial M;\mathbb Z)$ has nonzero boundary $[\partial M]$, so exactness of the pair sequence forces $H_4(M;\mathbb Z)=0$; in the nonorientable case absolute top homology is already zero.
:::

:::

::: pf-step
Hence $M$ is closed.

::: pf-proof
$H_4(M) = \ZZ \neq 0$ forces no boundary.
:::

:::

::: pf-step
$H_4(M;\ZZ) = \ZZ$ forces $M$ orientable.

::: pf-proof
for a connected closed manifold, integral top homology is $\ZZ$ exactly in the orientable case and is $0$ in the nonorientable case.
:::

:::

:::

:::

::: pf-step
Contradiction via Poincaré duality.

::: pf-proof

::: {.pf-step #s4-1}
For a closed orientable $4$-manifold, $H_2(M;\ZZ) \cong H^2(M;\ZZ)$.

::: pf-proof
Poincaré duality.
:::

:::

::: pf-step
$H^2(M;\ZZ) \cong \operatorname{Hom}(H_2(M;\ZZ), \ZZ) \oplus \operatorname{Ext}(H_1(M;\ZZ), \ZZ)$.

::: pf-proof
universal coefficient theorem.
:::

:::

::: pf-step
$H_2(M;\ZZ) = \ZZ/2$ and $H_1(M;\ZZ) = 0$ (from step [](#s1-3){.pf-ref}).

::: pf-proof
$H_1(\Sigma \RP^3) = 0$.
:::

:::

::: pf-step
Hence $H^2(M;\ZZ) = \operatorname{Hom}(\ZZ/2, \ZZ) \oplus \operatorname{Ext}(0, \ZZ) = 0$.

::: pf-proof
$\operatorname{Hom}(\ZZ/2, \ZZ) = 0$ (no nonzero homomorphism from a torsion group to $\ZZ$).
:::

:::

::: {.pf-step #s4-5}
But $H_2(M;\ZZ) = \ZZ/2 \neq 0$, contradicting $H_2(M;\ZZ) \cong H^2(M;\ZZ) = 0$.

::: pf-proof
Poincaré duality (step [](#s4-1){.pf-ref}) would force $H_2 \cong H^2$, but $H_2 = \ZZ/2$ and $H^2 = 0$.
:::

:::

:::

:::

::: pf-qed
Step [](#s4-5){.pf-ref} gives the contradiction, so no such $M$ exists.
:::

:::
:::
