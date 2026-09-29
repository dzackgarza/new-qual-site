---
schema: qual/card@1
id: E-P5AAV
kind: problem
title: '$\RR/\ZZ$ as a familiar topological group'
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

The integers $\mathbb{Z}$ are a normal subgroup of $(\mathbb{R}, +)$.
The quotient $\mathbb{R}/\mathbb{Z}$ is a familiar topological group; what is it?
:::

::: {.solution}
Let $\varphi\colon\mathbb R\to S^1$, $\varphi(t)=e^{2\pi it}$.

::: pf

::: {.pf-step #phi-is-quotient-homomorphism}
$\varphi$ is a continuous surjective homomorphism from $(\mathbb R,+)$ to $(S^1,\cdot)$ with kernel $\mathbb Z$.

::: pf-proof
$\varphi(s+t)=\varphi(s)\varphi(t)$, every point of $S^1$ is $e^{2\pi it}$ for some $t$, and $e^{2\pi it}=1$ if and only if $t\in\mathbb Z$.
:::

:::

::: {.pf-step #phi-is-open}
$\varphi$ is an open map.

::: pf-proof
For each $a\in\mathbb R$, $\varphi$ maps $(a,a+1)$ homeomorphically onto the open arc $S^1-\{\varphi(a)\}$, so it maps open subsets of $(a,a+1)$ to open subsets of $S^1$; every open subset of $\mathbb R$ is a union of such sets.
:::

:::

::: pf-qed
By step [](#phi-is-quotient-homomorphism){.pf-ref} and the first isomorphism theorem, $\varphi$ induces a group isomorphism $\mathbb R/\mathbb Z\to S^1$.
By steps [](#phi-is-quotient-homomorphism){.pf-ref} and [](#phi-is-open){.pf-ref}, $\varphi$ is a quotient map, so this bijection is a homeomorphism.
Hence $\mathbb R/\mathbb Z\cong\boxed{S^1}$ as topological groups.
:::

:::

:::
