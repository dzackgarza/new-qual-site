---
schema: qual/card@1
id: P-ALGPAN11-18
kind: problem
title: Symmetry group of a regular pentagram
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
Identify the isomorphism type of the symmetry group of the regular pentagram shown in the source.

![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-18.png)
:::

::: {.solution}
The symmetry group is the dihedral group of order $10$, so the answer is $\boxed{\text{(E)}}$.

<1>1. Determine the symmetries.
::: {.proof}
There are five rotations of the regular pentagram, through multiples of $2\pi/5$, and five reflections through axes passing through a vertex and the center.
These ten symmetries preserve adjacency in the star and exhaust the Euclidean symmetries of its five vertices.

If $r$ is a rotation by $2\pi/5$ and $s$ a reflection, then
\[
r^5=s^2=e,
\qquad srs=r^{-1}.
\]
Thus the group has the presentation of $D_5$ and has order $10$.
:::
:::
