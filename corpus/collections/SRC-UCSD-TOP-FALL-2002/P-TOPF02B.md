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

::: problem
Let $T$ be the torus which is obtained by identifying the edges of the unit square in the usual manner.
Let $S^1 \vee S^1$ be the one-point union of circles which is the image of the boundary of the unit square.

(a) Compute $H_*(T, S^1 \vee S^1; \mathbb{Z})$ and the map $i_* : H_*(S^1 \vee S^1; \mathbb{Z}) \to H_*(T; \mathbb{Z})$, where $i : S^1 \vee S^1 \hookrightarrow T$ is the inclusion map.

(b) Let $Z = S^1 \vee S^1 \vee S^2$ be the one-point union of the two circles and a $2$-sphere.
Prove that $H_*(Z; \mathbb{Z})$ and $H_*(T; \mathbb{Z})$ are isomorphic, but that $Z$ and $T$ do not have the same homotopy type.
:::

::: {.solution}
<1>1. Give $T$ its standard CW structure with one $0$-cell, two $1$-cells $a,b$, and one $2$-cell. Then $Y=S^1\vee S^1$ is exactly the $1$-skeleton.
::: {.proof}
This is the CW structure obtained from the unit square with opposite sides identified.
:::

<1>2. The relative cellular chain complex $C_*(T,Y)$ is
$$
0\longrightarrow\mathbb Z\longrightarrow0\longrightarrow0.
$$
::: {.proof}
Passing to the relative cellular complex quotients out all cells of $Y$, leaving only the single $2$-cell of the torus.
:::

<1>3. Therefore
$$
H_k(T,Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=2,\\
0,&k\ne2.
\end{cases}
$$
::: {.proof}
The only nonzero relative chain group is $C_2(T,Y)\cong\mathbb Z$, so all relative differentials vanish.
:::

<1>4. The inclusion map satisfies
$$
i_*:H_0(Y)\xrightarrow{\cong}H_0(T),
\qquad
i_*:H_1(Y)\xrightarrow{\cong}H_1(T),
$$
and $i_*=0$ in every other degree.
::: {.proof}
Both spaces are connected, so $H_0\cong\mathbb Z$ and inclusion induces the identity. The two circle classes $a,b$ form a basis of $H_1(Y)\cong\mathbb Z^2$ and also the standard basis of $H_1(T)\cong\mathbb Z^2$, hence $i_*$ is an isomorphism in degree $1$. Since $H_2(Y)=0$, the degree-$2$ map is zero; all other groups vanish.
:::

<1>5. The wedge
$$
Z=S^1\vee S^1\vee S^2
$$
has the same integral homology groups as $T$.
::: {.proof}
Reduced homology of a finite wedge is the direct sum of the reduced homologies of the summands. Hence
$$
H_0(Z)\cong\mathbb Z,\quad H_1(Z)\cong\mathbb Z^2,\quad H_2(Z)\cong\mathbb Z,
$$
with all higher groups zero, exactly as for the torus.
:::

<1>6. Nevertheless $Z$ and $T$ are not homotopy equivalent.
::: {.proof}
Their fundamental groups are
$$
\pi_1(Z)\cong F_2,
\qquad
\pi_1(T)\cong\mathbb Z^2.
$$
The first is nonabelian and the second abelian, so they are not isomorphic. A homotopy equivalence would induce an isomorphism on fundamental groups.
:::
:::

