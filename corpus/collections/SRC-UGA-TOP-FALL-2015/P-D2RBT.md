---
schema: qual/card@1
id: P-D2RBT
kind: problem
title: Fundamental group of $\RP^2\#\RP^2\#\RP^2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Fall 2015 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the one-vertex CW structure for the nonorientable genus-three surface and the attaching word a^2 b^2 c^2 before applying van Kampen.
---

::: problem
Compute the fundamental group, using any technique you like, of $\RP^2 \#\RP^2 \#\RP^2$.
:::

::: {.solution}
Let
\[
N_3=\RP^2\#\RP^2\#\RP^2.
\]

<1>1. The surface $N_3$ has a CW structure with one $0$-cell, three $1$-cells $a,b,c$, and one $2$-cell whose attaching word is
\[
a^2b^2c^2.
\]
::: {.proof}
Remove the interior of a disk from $N_3$.
The resulting nonorientable surface $N_{3,1}$ is a disk with three twisted bands attached, one for each projective-plane summand.
Collapse the disk and the transverse directions in the three bands onto their cores.
This gives a deformation retraction
\[
N_{3,1}\simeq S^1_a\vee S^1_b\vee S^1_c.
\]

When the boundary of $N_{3,1}$ is traversed once, the core of each twisted band is traversed twice in the same direction: the twist reverses the boundary side, so the two occurrences do not cancel as $a a^{-1}$ but contribute $a^2$, and similarly for the other two bands.
Ordering the bands as $a,b,c$, the boundary loop therefore represents
\[
a^2b^2c^2
\]
in $\pi_1(N_{3,1})$.
Gluing back the removed disk attaches one $2$-cell along precisely this boundary loop.
Hence $N_3$ has the asserted CW structure.
:::

<1>2. Therefore
\[
\boxed{
\pi_1(\RP^2\#\RP^2\#\RP^2)
\cong
\left\langle a,b,c\ \middle|\ a^2b^2c^2=1\right\rangle .
}
\]
::: {.proof}
The $1$-skeleton in <1>1 is a wedge of three circles, so its fundamental group is the free group
\[
F(a,b,c).
\]
Attaching a $2$-cell along the loop represented by $a^2b^2c^2$ quotients this free group by the normal closure of that word.
The Seifert–van Kampen theorem therefore gives
\[
\pi_1(N_3)
\cong
F(a,b,c)/\!\left\langle\!\left\langle a^2b^2c^2\right\rangle\!\right\rangle,
\]
which is exactly the displayed presentation.
:::
:::
