---
schema: qual/card@1
id: P-VTCZF
kind: problem
title: A holomorphic function with vanishing derivative on a connected domain is constant
classification:
  areas:
  - complex-analysis
  topics:
  - holomorphic-functions
  - connectedness
relations: []
review: draft
solved: true
---

::: problem
- Show that if $f$ is holomorphic on a connected region $\Omega$ and $f'\equiv 0$ on $\Omega$, then $f$ is constant on $\Omega$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that a holomorphic function $f$ on a connected open set $\Omega$ with $f' \equiv 0$ is constant.

<1>1. $\Omega$ is polygonally connected: any two points of $\Omega$ can be joined by a polygonal path inside $\Omega$.
Proof: $\Omega$ is an open connected subset of $\CC$; such sets are path-connected, and the connecting path can be taken polygonal (cover the path by small disks in $\Omega$ and join centers by segments).

<1>2. If $f' \equiv 0$ on a segment, then $f$ is constant along that segment.
Proof: Parametrize the segment $z(t) = z_0 + t(z_1 - z_0)$, $t \in [0,1]$.
Then $\dv{t} f(z(t)) = f'(z(t)) z'(t) = 0 \cdot (z_1 - z_0) = 0$, so $t \mapsto f(z(t))$ is constant, and $f(z_1) = f(z_0)$.

<1>3. $f$ is constant on each convex neighborhood, in particular on each small disk in $\Omega$.
Proof: A disk is convex, so by <1>2 every point of the disk has the same value as its center (join by the straight segment, which stays in the disk).

<1>4. $f$ is constant on $\Omega$.
Proof: Fix $z_0 \in \Omega$.
For any $z \in \Omega$, join $z_0$ to $z$ by a polygonal path (by <1>1); by <1>2 the value of $f$ is unchanged along each segment of the path, so $f(z) = f(z_0)$.

<1>5. Q.E.D. Proof: <1>4 shows $f$ is constant on the connected region $\Omega$.
:::
