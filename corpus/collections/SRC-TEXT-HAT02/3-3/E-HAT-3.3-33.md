---
schema: qual/card@1
id: E-HAT-3.3-33
kind: problem
title: Boundary of contractible manifold is a homology sphere
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that if $M$ is a compact contractible $n$-manifold then $\partial M$ is a homology $(n-1)$-sphere, that is, $H_i(\partial M; \mathbb{Z}) \approx H_i(S^{n-1}; \mathbb{Z})$ for all $i$.
:::

::: {.solution}

::: pf

::: pf-step

$M$ contractible implies $H_i(M)=0$ for $i>0$, $H_0=\ZZ$.

::: pf-proof

contractible.

:::

:::

::: {.pf-step #s2}

Lefschetz duality: $H_i(M,\partial M)\cong H^{n-i}(M)=0$ for $i<n$.

::: pf-proof

duality for compact $n$-manifold.

:::

:::

::: {.pf-step #s3}

Long exact sequence of pair $(M,\partial M)$: $\cdots\to H_i(\partial M)\to H_i(M)\to H_i(M,\partial M)\to\cdots$.

::: pf-proof

LES.

:::

:::

::: {.pf-step #s4}

For $i<n-1$, $H_i(M,\partial M)=0$ and $H_i(M)=0$, so $H_i(\partial M)=0$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

For $i=n-1$, $0\to H_{n-1}(\partial M)\to0\to\ZZ\to H_{n-2}(\partial M)\to0$ gives $H_{n-1}(\partial M)\cong\ZZ$.

::: pf-proof

Step [](#s3){.pf-ref} with $H_n(M,\partial M)\cong\ZZ$, $H_n(M)=0$.

:::

:::

::: {.pf-step #s6}

Hence $H_i(\partial M)\cong H_i(S^{n-1})$.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
