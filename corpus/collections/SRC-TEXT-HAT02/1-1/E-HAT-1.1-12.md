---
schema: qual/card@1
id: E-HAT-1.1-12
kind: problem
title: Every homomorphism $\pi_1(S^1) \to \pi_1(S^1)$ is induced by a map
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Circle
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that every homomorphism $\pi_1(S^1) \to \pi_1(S^1)$ can be realized as the induced homomorphism $\varphi_*$ of a map $\varphi: S^1 \to S^1$.
:::

::: {.solution}
::: pf

::: {.pf-step #hom-is-mult-by-n}
$\pi_1(S^1) = \ZZ$, so a homomorphism $\pi_1(S^1) \to \pi_1(S^1)$ is multiplication by some integer $n$.

::: pf-proof
$\operatorname{Hom}(\ZZ, \ZZ) = \ZZ$.
:::

:::

::: pf-step
Define $\varphi_n: S^1 \to S^1$ by $\varphi_n(z) = z^n$ (viewing $S^1 \subset \CC$).

::: pf-proof
definition.
:::

:::

::: {.pf-step #phin-degree-n}
$\varphi_n$ has degree $n$, so $(\varphi_n)_*$ is multiplication by $n$ on $\pi_1(S^1) = \ZZ$.

::: pf-proof
the map $z \mapsto z^n$ has degree $n$, and the induced map on $\pi_1$ is multiplication by the degree.
:::

:::

::: {.pf-step #hom-realized-by-phin}
Hence every homomorphism (multiplication by $n$) is realized by $\varphi_n$.

::: pf-proof
Steps [](#hom-is-mult-by-n){.pf-ref} and [](#phin-degree-n){.pf-ref}.
:::

:::

::: pf-qed
Step [](#hom-realized-by-phin){.pf-ref}.
:::

:::
:::
