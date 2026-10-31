---
schema: qual/card@1
id: P-UCTOP290-S9-7
kind: problem
title: Euler characteristics of projective spaces, products, surfaces, and complements
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 9, Problem 7 in its checked-in extraction.
---

::: {.problem}
Compute the Euler characteristic of each space:
$\RP^2$, $\RP^3$, $S^2\vee S^2$,
$S^2\times S^2$, $S^2\times S^3$, $\CP^3$,
a torus with two open disks removed,
$\Sigma_4$, $\RR^3$ minus the unit circle,
and $\RR^2$ minus five points.
:::

::: {.solution}

The cellular structures of projective spaces
give $\chi(\RP^2)=1$ and $\chi(\RP^3)=0$.
Wedge additivity and product multiplicativity
give
$$
\chi(S^2\vee S^2)=3,\qquad
\chi(S^2\times S^2)=4,\qquad
\chi(S^2\times S^3)=0.
$$
The four even-dimensional cells of $\CP^3$
give $\chi(\CP^3)=4$. A torus has Euler
characteristic zero; removing two open
disks lowers it by two, so the resulting
surface has $\chi=-2$. The genus-four
surface has $\chi(\Sigma_4)=2-2(4)=-6$.

Let $C$ be the unit circle in $\RR^3$.
One-point compactification identifies
$\RR^3\setminus C$ with
$S^3\setminus(C\cup\{\infty\})$.
Alexander duality gives reduced homology
$\ZZ$ in degrees $1$ and $2$, and zero
otherwise, because $C\cup\{\infty\}$
has reduced cohomology $\ZZ$ in degrees
$0$ and $1$. Thus its Euler characteristic
is $1-1+1=1$.

The plane minus five points retracts onto
a wedge of five circles, so its Euler
characteristic is $1-5=-4$.
:::
