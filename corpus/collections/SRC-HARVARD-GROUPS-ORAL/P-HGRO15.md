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

::: problem
Prove that $\mathbb R/\mathbb Z$ is isomorphic to the group of rotations about the origin in the complex plane.
:::

::: solution
Let $\operatorname{Rot}(\mathbb C)$ denote the group of rotations about the
origin. Define
\[
\Phi:\mathbb R/\mathbb Z\longrightarrow \operatorname{Rot}(\mathbb C)
\]
by letting $\Phi(t+\mathbb Z)$ be rotation through angle $2\pi t$.

<1>1. The map $\Phi$ is well-defined.
::: proof
If $t-s\in\mathbb Z$, then $2\pi(t-s)$ is an integral multiple of $2\pi$, so
rotation through angle $2\pi t$ equals rotation through angle $2\pi s$.
:::

<1>2. The map $\Phi$ is a homomorphism.
::: proof
Composition of rotations adds angles. Hence
\[
\Phi((s+\mathbb Z)+(t+\mathbb Z))
=\Phi(s+t+\mathbb Z)
=\Phi(s+\mathbb Z)\Phi(t+\mathbb Z).
\]
:::

<1>3. The map $\Phi$ is bijective.
::: proof
Every rotation about the origin has some angle $\theta$, hence equals
$\Phi(\theta/(2\pi)+\mathbb Z)$, so $\Phi$ is surjective.

If $\Phi(t+\mathbb Z)$ is the identity rotation, then
$2\pi t\in2\pi\mathbb Z$, so $t\in\mathbb Z$ and therefore
$t+\mathbb Z=\mathbb Z$. Thus the kernel is trivial, and $\Phi$ is injective.
:::

<1>4. Therefore $\mathbb R/\mathbb Z\cong\operatorname{Rot}(\mathbb C)$.
::: proof
By <1>1--<1>3, $\Phi$ is a bijective homomorphism.
:::
:::
