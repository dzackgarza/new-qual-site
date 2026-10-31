---
schema: qual/card@1
id: P-AMD-CM4OPBUE
kind: problem
title: Fundamental groups of band-and-disc spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Traced the band attachments in the page-one PDF render; over-under crossings do not identify the bands.
---

::: {.problem}
Each figure in Problem 4 of the source sheet depicts a space made by gluing bands, each homeomorphic to $I\times I$, to discs.
For each space, compute its fundamental group and the fundamental group after a disc is glued to each boundary circle.
:::

::: {.remark}
The two band-and-disc diagrams appear on page 1 of the source sheet.
:::

::: {.solution}

::: pf

::: pf-step

The left-hand figure has one disc and three untwisted bands.
Around the disc, the two attaching intervals of each band
are neighbors. The bands pass over and under one another
in the drawing, but those crossings do not identify points
of the bands. The surface has genus $0$ and four boundary
components.

::: pf-proof

Each band is a $1$-handle, so
$\chi=1-3=-2$. Attaching an untwisted band
along neighboring intervals of one boundary circle
splits that circle into two. The three bands
therefore raise the boundary count successively
from one to four. The equation
$2-2g-b=-2$ then gives $g=0$.

:::

:::

::: pf-step

Hence before capping its boundary,
$$\boxed{\pi_1\cong F_3,}$$
and after attaching a disc to every boundary circle the result is $S^2$, so
$$\boxed{\pi_1=1.}$$

::: pf-proof

A genus-$0$ surface with four boundary components deformation retracts to a wedge of three circles. Capping all four boundary components gives the sphere.

:::

:::

::: pf-step

The right-hand figure has two discs joined by three
untwisted bands. Tracing their ends through the
over-under crossings shows that the order of the
three bands at one disc is reversed at the other.
Its boundary is one circle, and the surface has
genus $1$.

::: pf-proof

The first band joins the two discs and leaves
one boundary circle. The second splits it into
two. Because the third band's ends occur in
the reversed cyclic order, they lie on those
two different boundary circles; attaching it
joins them, leaving one boundary circle.
Also $\chi=2-3=-1$. Hence
$2-2g-1=-1$, so $g=1$.

:::

:::

::: pf-step

Consequently before capping,
$$\boxed{\pi_1\cong F_2,}$$
and after attaching a disc to its boundary circle one obtains $T^2$, so
$$\boxed{\pi_1\cong\ZZ^2.}$$

::: pf-proof

A once-punctured torus deformation retracts to a wedge of two circles. Capping its unique boundary component gives the closed torus.

:::

:::

:::

:::
