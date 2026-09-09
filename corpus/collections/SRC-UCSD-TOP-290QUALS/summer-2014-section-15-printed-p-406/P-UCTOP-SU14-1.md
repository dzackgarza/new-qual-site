---
schema: qual/card@1
id: P-UCTOP-SU14-1
kind: problem
title: Fundamental group and homology of R^3 minus coordinate axes
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

Compute the fundamental group and homology groups of the space obtained by removing the union of the three coordinate axes from $\mathbb{R}^3$.

::: {.solution}
<1>1. Radial projection gives a deformation retraction
$$
\mathbb R^3\setminus\{\text{three coordinate axes}\}\simeq S^2\setminus\{\pm e_1,\pm e_2,\pm e_3\}.
$$
::: {.proof}
Every removed coordinate axis is invariant under positive radial scaling. Hence the homotopy
$$
H(x,t)=\left((1-t)+\frac{t}{\|x\|}\right)x
$$
stays in the complement and retracts it onto the unit sphere. The six points where the coordinate axes meet the sphere are precisely $\pm e_1,\pm e_2,\pm e_3$.
:::

<1>2. The sphere with six punctures deformation-retracts onto a wedge of five circles.
::: {.proof}
Removing one puncture identifies the six-punctured sphere with the plane minus five points. A plane with five punctures deformation-retracts onto a graph which is a bouquet of five circles.
:::

<1>3. Therefore
$$
\boxed{\pi_1\cong F_5}
$$
and
$$
\boxed{H_i\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^5,&i=1,\\
0,&i\ge2.
\end{cases}}
$$
::: {.proof}
A wedge of five circles has free fundamental group of rank five and cellular homology as displayed. Homotopy equivalence preserves both invariants.
:::
:::
