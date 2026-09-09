---
schema: qual/card@1
id: P-AMD-VUFY65E5
kind: problem
title: Nonorientable surface of genus $g$
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Classification
  - Orientation
relations: []
review: draft
---

::: {.problem}
Nonorientable surface of genus $g$ Obtain by removing $g$ discs from $S^2$ and attaching $g$ mobius strips
:::

::: {.solution}
<1>1. Removing the interiors of $g$ disjoint disks from $S^2$ produces an orientable genus-zero surface $S$ with $g$ boundary circles.
::: {.proof}
Deleting one open disk gives a disk; each additional deletion adds one boundary component without adding a handle.
:::

<1>2. Attach a Möbius band to each boundary circle of $S$. The resulting surface is closed and connected.
::: {.proof}
Each Möbius band has one boundary circle, so the $g$ gluings eliminate all boundary components. Connectivity is preserved because every band is attached to the connected surface $S$.
:::

<1>3. Each attached Möbius band contributes one crosscap, so the resulting surface is the connected sum
$$
\boxed{N_g=\#^g\mathbb{RP}^2}.
$$
::: {.proof}
A projective plane with an open disk removed is a Möbius band. The connected-sum construction removes a disk from each summand and glues boundary circles. Thus attaching a Möbius band to a boundary component is exactly adding one $\mathbb{RP}^2$ summand.
:::

<1>4. Its Euler characteristic is
$$
\chi(N_g)=2-g,
$$
and for $g\ge1$ it is nonorientable.
::: {.proof}
The punctured sphere has Euler characteristic $2-g$, each Möbius band has Euler characteristic $0$, and gluing along circles (Euler characteristic $0$) does not change the sum. The core circle of any attached Möbius band has a nonorientable neighborhood, so the resulting surface is nonorientable.
:::
:::
