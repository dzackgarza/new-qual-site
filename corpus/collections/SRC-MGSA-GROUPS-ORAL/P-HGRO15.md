---
schema: qual/card@1
id: P-HGRO15
kind: problem
title: The circle group as planar rotations
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Prove that $\RR/\ZZ$ is isomorphic to the group of rotations about the origin in the complex plane.
:::

::: {.solution}
Let $\operatorname{Rot}(\CC)$ denote the group of rotations about the
origin. Define
$$
\Phi:\RR/\ZZ\longrightarrow \operatorname{Rot}(\CC)
$$
by letting $\Phi(t+\ZZ)$ be rotation through angle $2\pi t$.

::: pf

::: {.pf-step #s1}

The map $\Phi$ is well-defined.

::: pf-proof

If $t-s\in\ZZ$, then $2\pi(t-s)$ is an integral multiple of $2\pi$, so
rotation through angle $2\pi t$ equals rotation through angle $2\pi s$.

:::

:::

::: {.pf-step #s2}

The map $\Phi$ is a homomorphism.

::: pf-proof

Composition of rotations adds angles. Hence
$$
\Phi((s+\ZZ)+(t+\ZZ))
=\Phi(s+t+\ZZ)
=\Phi(s+\ZZ)\Phi(t+\ZZ).
$$

:::

:::

::: {.pf-step #s3}

The map $\Phi$ is bijective.

::: pf-proof

Every rotation about the origin has some angle $\theta$, hence equals
$\Phi(\theta/(2\pi)+\ZZ)$, so $\Phi$ is surjective.

If $\Phi(t+\ZZ)$ is the identity rotation, then
$2\pi t\in2\pi\ZZ$, so $t\in\ZZ$ and therefore
$t+\ZZ=\ZZ$. Thus the kernel is trivial, and $\Phi$ is injective.

:::

:::

::: pf-step

Therefore $\RR/\ZZ\cong\operatorname{Rot}(\CC)$.

::: pf-proof

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\Phi$ is a bijective homomorphism.

:::

:::

:::

:::
