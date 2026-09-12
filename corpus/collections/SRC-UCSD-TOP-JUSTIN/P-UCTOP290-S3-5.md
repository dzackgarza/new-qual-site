---
schema: qual/card@1
id: P-UCTOP290-S3-5
kind: problem
title: Fundamental group of a face-identified cube
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
Take a solid cube and identify its faces in pairs as shown in Problem 5 of the source sheet.
The top and bottom faces and the front and back faces are identified by translations.
The left and right faces are identified by a translation composed with a rotation.
Compute the fundamental group of the resulting space.
:::

::: {.remark}
The face-identification diagram appears on page 1 of the source sheet.
:::

::: {.solution}
<1>1. First identify the top/bottom and front/back face pairs by the translations shown. The quotient is $T^2\times I$.
::: {.proof}
For each fixed left-to-right coordinate, the remaining two coordinate directions have opposite sides identified by translation, producing a torus fiber.
:::

<1>2. The source glyph on the left/right pair differs by a half-turn, so the final quotient is the mapping torus of
$$-I:T^2\to T^2.$$
::: {.proof}
The half-turn reverses both standard circle coordinates of the torus fiber, hence induces $-I$ on $\pi_1(T^2)\cong\mathbb Z^2$.
:::

<1>3. Therefore
$$\boxed{\pi_1(X)\cong \mathbb Z^2\rtimes_{-I}\mathbb Z}.$$
::: {.proof}
The fundamental group of a mapping torus of a homeomorphism $h:Y\to Y$ is the HNN semidirect product $\pi_1(Y)\rtimes_{h_*}\mathbb Z$.
:::

<1>4. Equivalently,
$$\boxed{\pi_1(X)=\langle a,b,t\mid [a,b]=1,\ tat^{-1}=a^{-1},\ tbt^{-1}=b^{-1}\rangle.}$$
::: {.proof}
Take $a,b$ for the two torus generators and $t$ for the mapping-torus direction; <1>2 gives the two conjugation relations.
:::
:::
