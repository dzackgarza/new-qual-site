---
schema: qual/card@1
id: P-AMD-ERYR6LDW
kind: problem
title: Fundamental groups of polygonal quotient spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
---

::: {.problem}
Each picture in Problem 2 of the source sheet represents a solid polygon whose boundary segments are identified, not necessarily in pairs, according to the labelled arrows.
Describe the fundamental group in each case.
:::

::: {.remark}
The three polygon diagrams appear on page 1 of the source sheet.
:::

::: {.solution}
<1>1. In the left pentagon, the two $a$-edges and the two $b$-edges are paired as indicated, while the fifth edge remains boundary. The quotient has one vertex, three $1$-cells (the classes $a,b$ and the unpaired edge $c$), and one $2$-cell.
::: {.proof}
Following the arrows identifies all five polygon vertices. The paired edges give the two edge classes $a,b$, and the remaining edge gives $c$.
:::

<1>2. The attaching word contains the unpaired edge $c$ exactly once, so the single relation eliminates $c$ and leaves
$$\boxed{\pi_1\cong F(a,b)\cong F_2.}$$
::: {.proof}
Van Kampen gives a presentation with generators $a,b,c$ and one relator in which $c^{\pm1}$ occurs exactly once. Solve that relation for $c$; no relation on $a,b$ remains.
:::

<1>3. In the middle octagon, the $a$-pair and $b$-pair identify the eight vertices into four classes. The quotient has six $1$-cells (the two paired classes and four unpaired boundary edges), four $0$-cells, and one $2$-cell, so its Euler characteristic is $-1$.
::: {.proof}
Number the vertices cyclically. The arrows identify the endpoints of the two $a$-edges in pairs and likewise for the two $b$-edges, producing four vertex classes. The four diagonal sides are left unpaired.
:::

<1>4. This quotient is a connected compact surface with nonempty boundary, hence its fundamental group is free. Since for a connected surface with boundary $\chi=1-r$ when $\pi_1\cong F_r$, one gets
$$\boxed{\pi_1\cong F_2.}$$
::: {.proof}
The quotient is obtained by pairwise gluing boundary intervals of a disc and leaves boundary intervals unglued, hence is a compact surface with boundary. From <1>3, $-1=1-r$, so $r=2$.
:::

<1>5. In the right triangle all three boundary edges are identified to one oriented edge $a$. The attaching word is freely equal to $a$ (up to inversion), so
$$\boxed{\pi_1=1.}$$
::: {.proof}
Traversing the boundary with the arrow orientations gives a word with two occurrences agreeing and one opposing, hence $a^{\pm1}$ after free reduction. Van Kampen gives $\langle a\mid a\rangle=1$. This is the standard dunce-cap edge identification.
:::
:::
