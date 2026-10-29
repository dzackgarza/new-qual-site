---
schema: qual/card@1
id: P-XW3UP
kind: problem
title: Stabilizer of a point in the unit disk under conformal automorphisms
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What is the stabilizer of a point $z_0 \in \DD$ in the open unit disk under the group of conformal automorphisms $\Aut(\DD)$?
Describe the group structure and express the automorphisms explicitly.
:::

::: {.solution}
Let $\phi_{z_0}(z)=\dfrac{z-z_0}{1-\overline{z_0}z}$; then $\phi_{z_0}\in\Aut(\DD)$ and $\phi_{z_0}(z_0)=0$.

::: pf

::: {.pf-step #origin}
$\Stab(0)=\{z\mapsto e^{i\theta}z:\theta\in\RR\}\cong U(1)$.

::: pf-proof
Rotations are automorphisms fixing $0$.
Conversely, if $f\in\Aut(\DD)$ fixes $0$, the Schwarz lemma applied to $f$ and $f^{-1}$ gives $\abs{f'(0)}\le1$ and $\abs{1/f'(0)}\le1$, so $\abs{f'(0)}=1$ and $f$ is a rotation.
Composition of rotations adds angles, so $\Stab(0)\cong\RR/2\pi\ZZ\cong U(1)$.
:::

:::

::: pf-step
$\Stab(z_0)=\{\phi_{z_0}^{-1}(e^{i\theta}\phi_{z_0}(z)):\theta\in\RR\}$, and $\boxed{\Stab(z_0)\cong U(1)\cong\SO(2)}$.

::: pf-proof
An automorphism $f$ fixes $z_0$ if and only if $\phi_{z_0}f\phi_{z_0}^{-1}$ fixes $0$, so conjugation by $\phi_{z_0}$ is an isomorphism $\Stab(z_0)\to\Stab(0)$; apply step [](#origin){.pf-ref}.
:::

:::

:::

:::
