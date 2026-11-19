---
schema: qual/card@1
id: P-AMD-FV5LNKN4
kind: problem
title: Cellular homology of a cube with paired faces
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Cell Complexes
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The figure was read at assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1518395458668.png
    (the image the card embeds). It shows a cube whose three pairs of opposite
    faces carry, respectively, P, rho and R, with the R on the visible right
    face drawn rotated through a quarter turn against the upright R on the left
    face, and the P and rho pairs drawn without such a rotation. The card's
    description had called the rho pair "Q"; that is corrected to the label the
    figure carries. The reading of the gluing, two translations and one quarter
    turn, is what the answer depends on.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Given that gluing, the computation is correct. Gluing the P and rho pairs by
    translations makes each slice parallel to the R faces a torus, and the R
    pair, glued by a quarter turn of the square, induces an orientation
    preserving automorphism of that torus whose matrix on H_1 is the quarter
    turn A, with determinant 1 on H_2. The Wang sequence of the resulting mapping
    torus is 0 -> coker(1 - f_*) -> H_k(X) -> ker(1 - f_*) -> 0 in each degree;
    on H_1 the matrix 1 - A has determinant 2, so its kernel vanishes and its
    cokernel is cyclic of order 2, while on H_0 the difference is zero, whose
    kernel is Z, so H_1 is Z/2 + Z, splitting because Z is free; on H_2 the
    cokernel is Z and the kernel on H_1 vanishes; on H_3 the kernel on H_2 is Z.
    The result Z, Z + Z/2, Z, Z is consistent with chi = 0 for this closed
    orientable three-manifold. Nothing was changed beyond the label.
---

::: {.problem}
Use cellular chain complexes to compute the homology of the cube whose faces are identified in pairs according to the scheme shown.

![Cube with paired faces](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1518395458668.png)
:::

::: {.solution}

::: pf

::: {.pf-step #torus}

$X$ is the mapping torus of the homeomorphism $\rho$ of $T^2=\RR^2/\ZZ^2$ induced by a quarter turn of the square, which acts on $H_1(T^2)\cong\ZZ^2$ by
$$A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$

::: pf-proof

The letters $P$ and $\rho$ appear in the same position on their paired faces, so these two pairs are glued by translations, and each slice of the cube parallel to the $R$ faces becomes a torus. The letter $R$ on the right face is the letter $R$ of the left face turned through $90^\circ$, so the last pair is glued by a quarter turn of the square. A quarter turn carries the pair of horizontal sides of the square to the pair of vertical sides, so it respects the translation identifications and induces $\rho$. It sends the horizontal generator of $H_1(T^2)$ to the vertical one and the vertical one to minus the horizontal one.

:::

:::

::: {.pf-step #action}

$\rho_*$ is the identity on $H_0(T^2)$ and $H_2(T^2)$, and $A$ on $H_1(T^2)$. On $H_1$, $1-A$ has determinant $2$, so
$$\ker(1-A)=0,\qquad\operatorname{coker}(1-A)\cong\ZZ/2.$$

::: pf-proof

A rotation preserves orientation, so it acts by $\det A=1$ on $H_2$. Here $1-A=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$, and an integer $2\times2$ matrix with determinant $2$ is injective with cokernel of order $2$.

:::

:::

::: {.pf-step #wang}

For each $k$ there is a short exact sequence
$$
0\to\operatorname{coker}(1-\rho_*\mid H_k(T^2))\to H_k(X)\to\ker(1-\rho_*\mid H_{k-1}(T^2))\to0.
$$

::: pf-proof

Give $T^2$ the CW structure with one $0$-cell, two $1$-cells and one $2$-cell, and homotope $\rho$ to a cellular map. The mapping torus then has cells $e\times\{0\}$ and $e\times(0,1)$ for each cell $e$ of $T^2$, and its cellular chain complex is the mapping cone of $1-\rho_\sharp$ on $C_*(T^2)$, whose differentials are zero. The long exact sequence of that mapping cone is the Wang sequence, which splits into the displayed short exact sequences.

:::

:::

::: pf-qed

By Steps [](#action){.pf-ref} and [](#wang){.pf-ref},
$$
\boxed{H_k(X;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ\oplus\ZZ/2,&k=1,\\
\ZZ,&k=2,\\
\ZZ,&k=3,\\
0,&k>3.
\end{cases}}
$$
In degree $1$ the sequence is $0\to\ZZ/2\to H_1(X)\to\ZZ\to0$, which splits because $\ZZ$ is free. In degree $2$ the cokernel on $H_2(T^2)$ is $\ZZ$ and the kernel on $H_1(T^2)$ is $0$. In degree $3$ the kernel on $H_2(T^2)$ is $\ZZ$. As a check, $X$ is a closed orientable $3$-manifold, so $H_3\cong\ZZ$ and the Euler characteristic is $1-1+1-1=0$.

:::

:::

:::
