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

::: problem
Prove that there is no compact 4-manifold $M$ (with or without boundary) which is homotopy-equivalent to the suspension $\Sigma\mathbb{RP}^3$.
:::

::: {.solution}
**Goal.** Show no compact $4$-manifold is homotopy equivalent to $\Sigma \RP^3$.

<1>1. Compute the homology of $\Sigma \RP^3$.
<2>1. $\tilde H_i(\Sigma X) \cong \tilde H_{i-1}(X)$.
Proof: the suspension isomorphism for reduced homology.
<2>2. $H_*(\RP^3) = \ZZ, \ZZ/2, 0, \ZZ$ in degrees $0, 1, 2, 3$.
Proof: standard homology of $\RP^3$.
<2>3. Hence $H_*(\Sigma \RP^3) = \ZZ, 0, \ZZ/2, 0, \ZZ$ in degrees $0, 1, 2, 3, 4$.
Proof: apply the suspension isomorphism: $H_1 = \tilde H_0(\RP^3) = 0$, $H_2 = \tilde H_1(\RP^3) = \ZZ/2$, $H_3 = \tilde H_2(\RP^3) = 0$, $H_4 = \tilde H_3(\RP^3) = \ZZ$.

<1>2. A compact $4$-manifold homotopy equivalent to $\Sigma \RP^3$ would have $H_2(M;\ZZ) = \ZZ/2$ and $H_4(M;\ZZ) = \ZZ$.
Proof: homotopy equivalence preserves homology.

<1>3. $H_4(M;\ZZ) = \ZZ$ forces $M$ to be closed and orientable.
<2>1. If $M$ has nonempty boundary, then $H_4(M;\ZZ) = 0$.
Proof: a compact $4$-manifold with boundary deformation-retracts onto a $3$-complex, so $H_4 = 0$.
<2>2. Hence $M$ is closed.
Proof: $H_4(M) = \ZZ \neq 0$ forces no boundary.
<2>3. $H_4(M;\ZZ) = \ZZ$ forces $M$ orientable.
Proof: a closed nonorientable $4$-manifold has $H_4(M;\ZZ) = 0$ (top homology is $\ZZ$ iff orientable, $\ZZ/2$ iff nonorientable, and $\ZZ/2$ tensored... actually $H_4 = \ZZ$ iff orientable).

<1>4. Contradiction via Poincaré duality.
<2>1. For a closed orientable $4$-manifold, $H_2(M;\ZZ) \cong H^2(M;\ZZ)$.
Proof: Poincaré duality.
<2>2. $H^2(M;\ZZ) \cong \operatorname{Hom}(H_2(M;\ZZ), \ZZ) \oplus \operatorname{Ext}(H_1(M;\ZZ), \ZZ)$.
Proof: universal coefficient theorem.
<2>3. $H_2(M;\ZZ) = \ZZ/2$ and $H_1(M;\ZZ) = 0$ (from <1>2.3).
Proof: $H_1(\Sigma \RP^3) = 0$.
<2>4. Hence $H^2(M;\ZZ) = \operatorname{Hom}(\ZZ/2, \ZZ) \oplus \operatorname{Ext}(0, \ZZ) = 0$.
Proof: $\operatorname{Hom}(\ZZ/2, \ZZ) = 0$ (no nonzero homomorphism from a torsion group to $\ZZ$).
<2>5. But $H_2(M;\ZZ) = \ZZ/2 \neq 0$, contradicting $H_2(M;\ZZ) \cong H^2(M;\ZZ) = 0$.
Proof: Poincaré duality (<1>4.1) would force $H_2 \cong H^2$, but $H_2 = \ZZ/2$ and $H^2 = 0$.

<1>5. Q.E.D.
Proof: <1>4.5 gives the contradiction, so no such $M$ exists.
:::
:::
