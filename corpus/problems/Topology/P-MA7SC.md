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
---

::: {.problem}
4. $S^2 \union_f D^2$, where $f$ attaches to the equator
:::

::: {.solution}
<1>1. Give $S^2$ a CW structure with two $0$-cells (the poles), two $1$-cells forming the equator, and two $2$-cells (the hemispheres), then attach the additional disk along the equator.
::: {.proof}
This CW structure is adapted to the attaching circle.
:::

<1>2. Equivalently, regard $S^2$ as two disks glued along their common boundary. Adding a third disk along that same circle produces three disks with common boundary.
::: {.proof}
This is exactly the quotient specified by the attaching map.
:::

<1>3. The union of any two of the disks is $S^2$, and the third disk is attached along a null-homotopic loop in this $S^2$. Hence
$$\boxed{S^2\cup_fD^2\simeq S^2\vee S^2.}$$
::: {.proof}
The common boundary circle bounds either of the first two disks, so its inclusion into their union $S^2$ is null-homotopic. Attaching a $2$-cell by a null-homotopic map wedges on an $S^2$.
:::

<1>4. Consequently $H_0\cong\mathbb Z$, $H_2\cong\mathbb Z^2$, and all other reduced homology vanishes.
::: {.proof}
Use the homology of a wedge of two $2$-spheres.
:::
:::
