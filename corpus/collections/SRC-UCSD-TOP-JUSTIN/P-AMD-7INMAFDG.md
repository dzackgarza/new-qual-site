---
schema: qual/card@1
id: P-AMD-7INMAFDG
kind: problem
title: Cellular homology of a triangular prism with identified faces
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Cell Complexes
  - Homology
relations: []
review: draft
---

::: {.problem}
Use cellular chain complexes to compute the homology of the solid triangular prism whose faces are identified as shown.

![Triangular prism with identified faces](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1518395440173.png)
:::

::: {.solution}
<1>1. The top and bottom triangular faces are identified by the common $Q$ marking, and the three rectangular side faces are identified by the common $F$ marking. Thus the quotient is
$$X\cong D\times S^1,$$
where $D$ is the dunce cap obtained by identifying the three sides of a triangle in the source orientation pattern.
::: {.proof}
The $Q$ pairing first turns $\Delta^2\times I$ into $\Delta^2\times S^1$. The side-face identifications preserve the circle coordinate and identify the three boundary edges of $\Delta^2$ by the standard dunce-cap pattern shown on the same source sheet.
:::

<1>2. The dunce cap $D$ is contractible.
::: {.proof}
Its CW structure has one $0$-cell, one $1$-cell $a$, and one $2$-cell attached by a word freely reducing to $a^{\pm1}$. Thus the $1$-cell is killed; the standard elementary collapse/homotopy of the dunce cap then contracts the resulting complex to its vertex.
:::

<1>3. Projection $D\times S^1\to S^1$ is a homotopy equivalence.
::: {.proof}
Choose a contraction of $D$ to a point and take its product with $S^1$.
:::

<1>4. Therefore
$$\boxed{H_i(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,1,\\
0,&i\ge2.
\end{cases}}$$
::: {.proof}
Use <1>3 and the integral homology of the circle.
:::
:::
