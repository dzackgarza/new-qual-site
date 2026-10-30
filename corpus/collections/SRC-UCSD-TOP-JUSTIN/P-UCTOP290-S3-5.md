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
The left and right faces are identified by a translation composed with a rotation: the letter on the right face is the letter on the left face turned through a quarter turn.
Compute the fundamental group of the resulting space.
:::

::: {.remark}
The face-identification diagram appears on page 1 of the source sheet.
:::

::: {.solution}

::: pf

::: {.pf-step #fiber}

Use coordinates $(x,y,z)\in I^3$ with $x$ from left to right. The top/bottom and front/back pairings are translations, so they make each slice $\{x\}\times I^2$ into the torus $T^2=\RR^2/\ZZ^2$, and the quotient by these two pairings is $I\times T^2$.

::: pf-proof

The two translations identify opposite sides of each square slice $\{x\}\times I^2$, which is the standard square model of the torus.

:::

:::

::: {.pf-step #monodromy}

The left/right pairing is $(0,y,z)\sim(1,\rho(y,z))$, where $\rho$ is the rotation of the square through a quarter turn about its centre. Hence $X$ is the mapping torus of the homeomorphism of $T^2$ induced by $\rho$, which acts on $\pi_1(T^2)=H_1(T^2)\cong\ZZ^2$ by
$$A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$

::: pf-proof

In the figure the letter $R$ on the right face is the letter $R$ of the left face turned through $90^\circ$. The quarter turn $\rho$ maps the square to itself and carries the pair of horizontal sides to the pair of vertical sides, so it respects the translation identifications and induces a homeomorphism of $T^2$. It fixes the centre of the square, which is a base point for $\pi_1$, and it sends the horizontal generator $a$ to the vertical generator $b$ and $b$ to $a^{-1}$ (for one choice of orientations).

:::

:::

::: pf-qed

The fundamental group of the mapping torus of a based homeomorphism $h$ of $Y$ is $\pi_1(Y)\rtimes_{h_*}\ZZ$ (van Kampen, or the long exact sequence of the fibration over $S^1$). By Steps [](#fiber){.pf-ref} and [](#monodromy){.pf-ref},
$$\boxed{\pi_1(X)\cong\ZZ^2\rtimes_A\ZZ=\langle a,b,t\mid [a,b]=1,\ tat^{-1}=b,\ tbt^{-1}=a^{-1}\rangle.}$$
Its abelianization is $\ZZ\oplus\ZZ/2$, since $\operatorname{coker}(A-I)\cong\ZZ/2$. The other orientation of the quarter turn replaces $A$ by $A^{-1}$ and gives an isomorphic group, by $t\mapsto t^{-1}$.

:::

:::

:::
