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
  - Poincaré Duality
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $M$ be a $4$-dimensional compact, connected, simply connected manifold without boundary such that $\chi(M) = k$.
Assuming $M$ is orientable, calculate $H_i(M; \mathbb{Z})$ for $0 \leq i \leq 4$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$H_0(M) = \ZZ$.

::: pf-proof

$M$ is connected.

:::

:::

::: {.pf-step #s2}

$H_1(M) = 0$.

::: pf-proof

$H_1(M) \cong \pi_1(M)^{\mathrm{ab}} = 0$ since $M$ is simply connected.

:::

:::

::: {.pf-step #s3}

$H_4(M) = \ZZ$.

::: pf-proof

$M$ is a closed connected orientable $4$-manifold, so $H_4(M) \cong \ZZ$ (fundamental class).

:::

:::

::: {.pf-step #s4}

$H_3(M) \cong H^1(M) \cong \operatorname{Hom}(H_1(M), \ZZ) = 0$.

::: pf-proof

Poincaré duality $H_3(M) \cong H^1(M)$, and $H^1(M) \cong \operatorname{Hom}(H_1(M), \ZZ) = 0$ by step [](#s2){.pf-ref} (using the universal coefficient theorem, since $H_0$ is free).

:::

:::

::: pf-step

Let $b_2 = \operatorname{rank} H_2(M)$.

::: pf-proof

define the second Betti number.

:::

:::

::: {.pf-step #s6}

$\chi(M) = 1 - 0 + b_2 - 0 + 1 = b_2 + 2$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}, summing alternating ranks.

:::

:::

::: {.pf-step #s7}

Hence $b_2 = k - 2$.

::: pf-proof

Step [](#s6){.pf-ref} and the hypothesis $\chi(M) = k$.

:::

:::

::: {.pf-step #s8}

$H_2(M) \cong \ZZ^{k-2}$.

::: pf-proof

By Poincaré duality, $H^3(M;\ZZ)\cong H_1(M;\ZZ)=0$. The universal coefficient theorem gives an injection
$$
\operatorname{Ext}(H_2(M;\ZZ),\ZZ)\hookrightarrow H^3(M;\ZZ),
$$
so $\operatorname{Ext}(H_2(M),\ZZ)=0$. Since $M$ is compact, $H_2(M)$ is finitely generated; a finitely generated abelian group has vanishing $\operatorname{Ext}(-,\ZZ)$ exactly when it is torsion-free, hence free. Its rank is $b_2=k-2$ by step [](#s7){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s8){.pf-ref}, [](#s4){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::
