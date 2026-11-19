---
schema: qual/card@1
id: P-UCTOP-SU14-1
kind: problem
title: 'Fundamental group and homology of $\RR^3$ minus the coordinate axes'
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained compilation `assets/attachments/UCSD_290_Qualifying_Exams.pdf`, whose contents page gives the exam as item
    406 of the printed sequence: the statement is Problem 1 of the Summer 2014 exam on printed
    p. 406, and the printed words are the card's. The exam, the problem number and the page are
    now named in the solution's opening sentence. Not checked in this pass: the computation,
    which the edit does not touch.
---

::: {.problem}
Compute the fundamental group and homology groups of the space obtained by removing the union of the three coordinate axes from $\RR^3$.
:::

::: {.solution}
This is Problem 1 of the Summer 2014 qualifying exam in the retained compilation `assets/attachments/UCSD_290_Qualifying_Exams.pdf`, printed p. 406, and the statement below is its wording.

::: pf

::: pf-step
Radial projection gives a deformation retraction
$$
\RR^3\setminus\{\text{three coordinate axes}\}\simeq S^2\setminus\{\pm e_1,\pm e_2,\pm e_3\}.
$$

::: pf-proof
Every removed coordinate axis is invariant under positive radial scaling. Hence the homotopy
$$
H(x,t)=\left((1-t)+\frac{t}{\norm{x}}\right)x
$$
stays in the complement and retracts it onto the unit sphere. The six points where the coordinate axes meet the sphere are precisely $\pm e_1,\pm e_2,\pm e_3$.
:::

:::

::: pf-step
The sphere with six punctures deformation-retracts onto a wedge of five circles.

::: pf-proof
Removing one puncture identifies the six-punctured sphere with the plane minus five points. A plane with five punctures deformation-retracts onto a graph which is a bouquet of five circles.
:::

:::

::: pf-step
Therefore
$$
\boxed{\pi_1\cong F_5}
$$
and
$$
\boxed{H_i\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ^5,&i=1,\\
0,&i\ge2.
\end{cases}}
$$

::: pf-proof
A wedge of five circles has free fundamental group of rank five and cellular homology as displayed. Homotopy equivalence preserves both invariants.
:::

:::

:::

:::
