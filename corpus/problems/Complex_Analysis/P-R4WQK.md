---
schema: qual/card@1
id: P-R4WQK
kind: problem
title: Distinct $z_1,z_2,z_3$ form an equilateral triangle iff $z_1^2+z_2^2+z_3^2=z_1z_2+z_2z_3+z_3z_1$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Prove that distinct complex numbers $z_1,z_2,z_3$ are the vertices of an
equilateral triangle if and only if
\[
z_1^2+z_2^2+z_3^2=z_1z_2+z_2z_3+z_3z_1.
\]
:::

::: {.solution}
Let $\omega=e^{2\pi i/3}$. Since
$1+\omega+\omega^2=0$,
\[
z_1^2+z_2^2+z_3^2-z_1z_2-z_2z_3-z_3z_1
=(z_1+\omega z_2+\omega^2z_3)
 (z_1+\omega^2z_2+\omega z_3).
\]
Thus the displayed quadratic identity holds exactly when one factor vanishes.
For example,
\[
z_1+\omega z_2+\omega^2z_3=0
\iff z_1-z_3=-\omega(z_2-z_3).
\]
The multiplier $-\omega=e^{-i\pi/3}$ has modulus $1$ and rotates by
$-\pi/3$. Hence the two sides issuing from $z_3$ have equal length and meet
at angle $\pi/3$, so the triangle is equilateral. The other factor gives the
opposite orientation. Conversely, an equilateral triangle has one of these
two oriented side relations, so one factor vanishes and the identity follows.
:::