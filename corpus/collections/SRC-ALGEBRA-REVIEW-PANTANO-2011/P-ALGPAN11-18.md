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
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the misattached scan of test 1, problem 49 with a transcription of test 1, problem 60 from ALGEBRA_REVIEW1.pdf page 5, describing its pentagram figure.
---

::: {.problem}
The source shows a regular pentagram: a five-pointed star drawn by joining each vertex of a regular pentagon to the two vertices not adjacent to it.

The group of symmetries of the regular pentagram shown above is isomorphic to the

(A) symmetric group $S_5$

(B) alternating group $A_5$

(C) cyclic group of order $5$

(D) cyclic group of order $10$

(E) dihedral group of order $10$
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
