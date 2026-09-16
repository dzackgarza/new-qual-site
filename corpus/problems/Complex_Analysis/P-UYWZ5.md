---
schema: qual/card@1
id: P-UYWZ5
kind: problem
title: Equilateral triangles as $z_1^2+z_2^2+z_3^2=z_1z_2+z_2z_3+z_3z_1$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Prove that the distinct complex numbers $z_1, z_2, z_3$ are the vertices of an equilateral triangle if and only if
\[
z_{1}^{2}+z_{2}^{2}+z_{3}^{2}=z_{1} z_{2}+z_{2} z_{3}+z_{3} z_{1}
.\]
:::

::: {.solution}
Translate so that $z_1=0$, and put
\[
a=z_2-z_1,\qquad b=z_3-z_1.
\]
The displayed equation is translation-invariant and becomes
\[
a^2+b^2=ab.
\]
Since the three points are distinct, $a\ne0$. Dividing by $a^2$ and writing
$t=b/a$ gives
\[
t^2-t+1=0,
\]
so
\[
t=e^{i\pi/3}\quad\text{or}\quad t=e^{-i\pi/3}.
\]
Thus $|b|=|a|$ and the angle between $a$ and $b$ is $\pi/3$. Consequently
\[
|a-b|=|a|=|b|,
\]
so the three vertices form an equilateral triangle.

Conversely, if the triangle is equilateral, after the same translation and
division by $a\ne0$ we have $b/a=e^{\pm i\pi/3}$, which satisfies
$t^2-t+1=0$. Reversing the algebra gives the displayed identity.
:::
