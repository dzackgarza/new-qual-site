---
schema: qual/card@1
id: P-TOPF02B
kind: problem
title: "Relative homology of the torus modulo its boundary figure-eight"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $T$ be the torus which is obtained by identifying the edges of the unit square in the usual manner.
Let $S^1 \vee S^1$ be the one-point union of circles which is the image of the boundary of the unit square.

(a) Compute $H_*(T, S^1 \vee S^1; \ZZ)$ and the map $i_* : H_*(S^1 \vee S^1; \ZZ) \to H_*(T; \ZZ)$, where $i : S^1 \vee S^1 \hookrightarrow T$ is the inclusion map.

(b) Let $Z = S^1 \vee S^1 \vee S^2$ be the one-point union of the two circles and a $2$-sphere.
Prove that $H_*(Z; \ZZ)$ and $H_*(T; \ZZ)$ are isomorphic, but that $Z$ and $T$ do not have the same homotopy type.
:::

::: {.solution}

::: pf

::: pf-step
Give $T$ its standard CW structure with one $0$-cell, two $1$-cells $a,b$, and one $2$-cell. Then $Y=S^1\vee S^1$ is exactly the $1$-skeleton.

::: pf-proof
This is the CW structure obtained from the unit square with opposite sides identified.
:::

:::

::: pf-step
The relative cellular chain complex $C_*(T,Y)$ is
$$
0\longrightarrow\ZZ\longrightarrow0\longrightarrow0.
$$

::: pf-proof
Passing to the relative cellular complex quotients out all cells of $Y$, leaving only the single $2$-cell of the torus.
:::

:::

::: pf-step
Therefore
$$
H_k(T,Y;\ZZ)\cong
\begin{cases}
\ZZ,&k=2,\\
0,&k\ne2.
\end{cases}
$$

::: pf-proof
The only nonzero relative chain group is $C_2(T,Y)\cong\ZZ$, so all relative differentials vanish.
:::

:::

::: pf-step
The inclusion map satisfies
$$
i_*:H_0(Y)\xrightarrow{\cong}H_0(T),
\qquad
i_*:H_1(Y)\xrightarrow{\cong}H_1(T),
$$
and $i_*=0$ in every other degree.

::: pf-proof
Both spaces are connected, so $H_0\cong\ZZ$ and inclusion induces the identity. The two circle classes $a,b$ form a basis of $H_1(Y)\cong\ZZ^2$ and also the standard basis of $H_1(T)\cong\ZZ^2$, hence $i_*$ is an isomorphism in degree $1$. Since $H_2(Y)=0$, the degree-$2$ map is zero; all other groups vanish.
:::

:::

::: pf-step
The wedge
$$
Z=S^1\vee S^1\vee S^2
$$
has the same integral homology groups as $T$.

::: pf-proof
Reduced homology of a finite wedge is the direct sum of the reduced homologies of the summands. Hence
$$
H_0(Z)\cong\ZZ,\quad H_1(Z)\cong\ZZ^2,\quad H_2(Z)\cong\ZZ,
$$
with all higher groups zero, exactly as for the torus.
:::

:::

::: pf-step
Nevertheless $Z$ and $T$ are not homotopy equivalent.

::: pf-proof
Their fundamental groups are
$$
\pi_1(Z)\cong F_2,
\qquad
\pi_1(T)\cong\ZZ^2.
$$
The first is nonabelian and the second abelian, so they are not isomorphic. A homotopy equivalence would induce an isomorphism on fundamental groups.
:::

:::

:::

:::

