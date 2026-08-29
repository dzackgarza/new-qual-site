---
schema: qual/card@1
id: P-TOPF06G
kind: problem
title: "Homology of a simply-connected closed orientable 4-manifold from its Euler characteristic"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Euler Characteristic
  - Poincare Duality
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $M$ be a $4$-dimensional compact, connected, simply connected manifold without boundary such that $\chi(M) = k$.
Assuming $M$ is orientable, calculate $H_i(M; \mathbb{Z})$ for $0 \leq i \leq 4$.
:::

::: {.solution}
<1>1. $H_0(M) = \ZZ$.
Proof: $M$ is connected.

<1>2. $H_1(M) = 0$.
Proof: $H_1(M) \cong \pi_1(M)^{\mathrm{ab}} = 0$ since $M$ is simply connected.

<1>3. $H_4(M) = \ZZ$.
Proof: $M$ is a closed connected orientable $4$-manifold, so $H_4(M) \cong \ZZ$ (fundamental class).

<1>4. $H_3(M) \cong H^1(M) \cong \operatorname{Hom}(H_1(M), \ZZ) = 0$.
Proof: Poincaré duality $H_3(M) \cong H^1(M)$, and $H^1(M) \cong \operatorname{Hom}(H_1(M), \ZZ) = 0$ by <1>2 (using the universal coefficient theorem, since $H_0$ is free).

<1>5. Let $b_2 = \operatorname{rank} H_2(M)$.
Proof: define the second Betti number.

<1>6. $\chi(M) = 1 - 0 + b_2 - 0 + 1 = b_2 + 2$.
Proof: <1>1–<1>4, summing alternating ranks.

<1>7. Hence $b_2 = k - 2$.
Proof: <1>6 and the hypothesis $\chi(M) = k$.

<1>8. $H_2(M) \cong \ZZ^{k-2}$.
Proof: $H_2(M)$ is free abelian (its torsion would pair nontrivially with $H_1$ under Poincaré duality, but $H_1 = 0$), so $H_2(M) \cong \ZZ^{b_2} = \ZZ^{k-2}$ by <1>7.

<1>9. Q.E.D.
Proof: <1>1, <1>2, <1>8, <1>4, <1>3.
:::
