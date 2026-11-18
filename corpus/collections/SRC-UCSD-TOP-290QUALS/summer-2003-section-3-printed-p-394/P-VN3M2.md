---
schema: qual/card@1
id: P-VN3M2
kind: problem
title: Homology and cohomology of a closed oriented $3$-manifold with $\pi_1=\ZZ^{*2}$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Homology
  - Cohomology
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    Justin sheet 13, Problem 7 states the same task. Replaced the
    list-style solution with the abelianization, universal
    coefficient, and Poincare-duality argument.
---

::: {.problem}
Let $M^3$ be a closed connected oriented 3-manifold with fundamental group isomorphic to the free group on two generators.
Compute the homology and cohomology groups $H_*(M;\ZZ)$ and $H^*(M;\ZZ)$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own computation follows, with the Hurewicz input, the cohomology in degree one and the duality applications as separate steps.

::: pf

::: {.pf-step #low}
$H_{0}(M;\ZZ)=\ZZ$ and $H_{1}(M;\ZZ)\cong\ZZ^{2}$.

::: pf-proof
$M$ is connected, so $H_{0}(M;\ZZ)=\ZZ$. $M$ is path connected, so the Hurewicz map in degree one is an isomorphism onto the abelianisation: $H_{1}(M;\ZZ)\cong\pi_{1}(M)^{\mathrm{ab}}$, and the abelianisation of the free group $F_{2}$ is $\ZZ^{2}$.
:::

:::

::: {.pf-step #hone}
$H^{1}(M;\ZZ)\cong\ZZ^{2}$ and $H^{0}(M;\ZZ)\cong\ZZ$.

::: pf-proof
The universal coefficient theorem gives the split exact sequence $0\to\Ext^{1}\big(H_{0}(M),\ZZ\big)\to H^{1}(M;\ZZ)\to\Hom\big(H_{1}(M),\ZZ\big)\to0$, with $\Ext^{1}(\ZZ,\ZZ)=0$ because $\ZZ$ is free, so $H^{1}(M;\ZZ)\cong\Hom(\ZZ^{2},\ZZ)=\ZZ^{2}$. Similarly $H^{0}(M;\ZZ)\cong\Hom(H_{0}(M),\ZZ)=\ZZ$.
:::

:::

::: {.pf-step #duality}
$H_{2}(M;\ZZ)\cong\ZZ^{2}$ and $H_{3}(M;\ZZ)\cong\ZZ$.

::: pf-proof
$M$ is a closed connected orientable $3$-manifold, so Poincaré duality gives $H_{k}(M;\ZZ)\cong H^{3-k}(M;\ZZ)$: with $k=2$ this is $H_{2}\cong H^{1}=\ZZ^{2}$ and with $k=3$ it is $H_{3}\cong H^{0}=\ZZ$.
:::

:::

::: {.pf-step #cohomology}
$H^{i}(M;\ZZ)\cong H_{3-i}(M;\ZZ)$ for all $i$.

::: pf-proof
Poincaré duality in cohomology for a closed oriented $n$-manifold reads $H^{i}(M;\ZZ)\cong H_{n-i}(M;\ZZ)$; here $n=3$.
:::

:::

::: {.pf-qed}
Combining the steps, $H_{0}=\ZZ$, $H_{1}=\ZZ^{2}$, $H_{2}=\ZZ^{2}$, $H_{3}=\ZZ$, and by step [](#cohomology){.pf-ref} the same list in the other order: $H^{0}=\ZZ$, $H^{1}=\ZZ^{2}$, $H^{2}=\ZZ^{2}$, $H^{3}=\ZZ$, with all other (co)homology groups zero. In particular there is no torsion, and $H_{1}=\ZZ^{2}$ agrees with $\pi_{1}=F_{2}$ abelianised.
:::

:::

:::
