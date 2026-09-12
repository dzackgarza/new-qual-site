---
schema: qual/card@1
id: P-M62FC
kind: problem
title: Compact connected surfaces with nonempty boundary are homotopy equivalent to
  a wedge of circles
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Surfaces
  - Classification
relations: []
review: draft
---

::: problem
Show that any compact connected surface with nonempty boundary is homotopy equivalent to a wedge of circles

> Hint: you may assume that any compact connected surface without boundary is given by identifying edges of a polygon in pairs.

For each surface appearing in the classification of compact surfaces with nonempty boundary, say how many circles are needed in the wedge from part (a).

> Hint: you should be able to do this even if you have not done part (a).
:::

::: {.solution}
<1>1. Every compact connected surface with nonempty boundary admits a handle decomposition with one $0$-handle, only $1$-handles, and no $2$-handles.
::: {.proof}
By the classification of compact surfaces with boundary, an orientable surface is obtained from a disk by adding $g$ orientable handles and then creating $b-1$ additional boundary components, while a nonorientable surface is obtained by adding $h$ crosscaps and then creating $b-1$ additional boundary components. These operations can be realized by attaching $1$-handles to a disk.
:::

<1>2. Such a surface deformation retracts onto the union of the core point of the $0$-handle and the core arcs of its $1$-handles, which is a wedge of circles.
::: {.proof}
A handlebody with only $0$- and $1$-handles collapses onto its $1$-dimensional spine. With one $0$-handle, the spine is a connected graph with one vertex and one loop for each $1$-handle.
:::

<1>3. For the orientable surface $\Sigma_{g,b}$ of genus $g$ with $b\ge1$ boundary components,
$$\boxed{\Sigma_{g,b}\simeq\bigvee^{\,2g+b-1}S^1.}$$
::: {.proof}
Its Euler characteristic is $2-2g-b$. A wedge of $r$ circles has Euler characteristic $1-r$, so the spine in <1>2 must have
$$r=1-\chi(\Sigma_{g,b})=2g+b-1$$
loops.
:::

<1>4. For the nonorientable surface $N_{h,b}$ with $h\ge1$ crosscaps and $b\ge1$ boundary components,
$$\boxed{N_{h,b}\simeq\bigvee^{\,h+b-1}S^1.}$$
::: {.proof}
Here $\chi(N_{h,b})=2-h-b$, so the same calculation gives
$$r=1-\chi(N_{h,b})=h+b-1.$$
:::

<1>5. These formulas include the disk ($r=0$), annulus ($r=1$), Möbius band ($r=1$), punctured torus ($r=2$), and pair of pants ($r=2$).
::: {.proof}
Substitute the corresponding values of $(g,b)$ or $(h,b)$ into <1>3--<1>4.
:::
:::
