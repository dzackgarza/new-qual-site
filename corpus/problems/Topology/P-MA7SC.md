---
schema: qual/card@1
id: P-MA7SC
kind: problem
title: $S^2$ with a disk attached along the equator
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "Source text: 'S^2 union_f D^2, where f attaches to the equator', a list item with no task. The statement now asks for the homotopy type and homology, which the solution computes."
---

::: {.problem}
Let $f:S^1\to S^2$ be the inclusion of the equator. Determine the homotopy type of $S^2 \union_f D^2$ and compute its homology.
:::

::: {.solution}

::: pf

::: pf-step

Give $S^2$ a CW structure with two $0$-cells (the poles), two $1$-cells forming the equator, and two $2$-cells (the hemispheres), then attach the additional disk along the equator.

::: pf-proof

This CW structure is adapted to the attaching circle.

:::

:::

::: pf-step

Equivalently, regard $S^2$ as two disks glued along their common boundary. Adding a third disk along that same circle produces three disks with common boundary.

::: pf-proof

This is exactly the quotient specified by the attaching map.

:::

:::

::: pf-step

The union of any two of the disks is $S^2$, and the third disk is attached along a null-homotopic loop in this $S^2$. Hence
$$\boxed{S^2\cup_fD^2\simeq S^2\vee S^2.}$$

::: pf-proof

The common boundary circle bounds either of the first two disks, so its inclusion into their union $S^2$ is null-homotopic. Attaching a $2$-cell by a null-homotopic map wedges on an $S^2$.

:::

:::

::: pf-step

Consequently $H_0\cong\ZZ$, $H_2\cong\ZZ^2$, and $H_k=0$ for all other $k$.

::: pf-proof

Use the homology of a wedge of two $2$-spheres.

:::

:::

:::

:::
