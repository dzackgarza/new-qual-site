---
schema: qual/card@1
id: P-VTCZF
kind: problem
title: A holomorphic function with vanishing derivative on a connected domain is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- Show that if $f$ is holomorphic on a connected region $\Omega$ and $f'\equiv 0$ on $\Omega$, then $f$ is constant on $\Omega$.
:::

::: {.solution}
**Goal:** Show that a holomorphic function $f$ on a connected open set $\Omega$ with $f' \equiv 0$ is constant.

::: pf

::: {.pf-step #s1}

$\Omega$ is polygonally connected: any two points of $\Omega$ can be joined by a polygonal path inside $\Omega$.

::: pf-proof

$\Omega$ is an open connected subset of $\CC$; such sets are path-connected, and the connecting path can be taken polygonal (cover the path by small disks in $\Omega$ and join centers by segments).

:::

:::

::: {.pf-step #s2}

If $f' \equiv 0$ on a segment, then $f$ is constant along that segment.

::: pf-proof

Parametrize the segment $z(t) = z_0 + t(z_1 - z_0)$, $t \in [0,1]$.

Then $\ddd{t} f(z(t)) = f'(z(t)) z'(t) = 0 \cdot (z_1 - z_0) = 0$, so $t \mapsto f(z(t))$ is constant, and $f(z_1) = f(z_0)$.

:::

:::

::: pf-step

$f$ is constant on each convex neighborhood, in particular on each small disk in $\Omega$.

::: pf-proof

A disk is convex, so by step [](#s2){.pf-ref} every point of the disk has the same value as its center (join by the straight segment, which stays in the disk).

:::

:::

::: {.pf-step #s4}

$f$ is constant on $\Omega$.

::: pf-proof

Fix $z_0 \in \Omega$.

For any $z \in \Omega$, join $z_0$ to $z$ by a polygonal path (by step [](#s1){.pf-ref}); by step [](#s2){.pf-ref} the value of $f$ is unchanged along each segment of the path, so $f(z) = f(z_0)$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} shows $f$ is constant on the connected region $\Omega$.

:::

:::

:::
