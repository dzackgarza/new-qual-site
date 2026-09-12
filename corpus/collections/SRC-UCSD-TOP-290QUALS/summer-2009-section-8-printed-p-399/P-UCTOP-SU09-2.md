---
schema: qual/card@1
id: P-UCTOP-SU09-2
kind: problem
title: Homology of quotient of solid hexagonal prism
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

A space $X$ is constructed by gluing up the solid hexagonal prism: the hexagonal faces are glued using translation and a 60 degree rotation, and the opposite sides of the prism are glued in pairs via translation.
Calculate the integral homology of $X$.

::: {.solution}
<1>1. Pairing the three opposite rectangular sides of the prism by translations turns each horizontal hexagonal cross-section into a torus $T^2$.
:::
::: {.proof}
A regular hexagon with opposite sides identified by translations is a fundamental polygon for the hexagonal lattice in $\mathbb R^2$, hence its quotient is $\mathbb R^2/\Lambda\cong T^2$. Doing this continuously through the height of the prism gives $T^2\times I$.
:::

<1>2. The remaining top-to-bottom gluing makes $X$ the mapping torus of the $60^\circ$ rotation
$$
R:T^2\to T^2.
$$
:::
::: {.proof}
The stated top/bottom identification differs from the vertical translation by a $60^\circ$ rotation of the hexagonal lattice, which descends to a torus automorphism. Thus
$$
X\cong T^2\times[0,1]/(x,1)\sim(Rx,0).
$$
:::

<1>3. In the lattice basis $u,v$ making an angle of $60^\circ$, the induced map on $H_1(T^2)\cong\mathbb Z^2$ is
$$
A=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
$$
:::
::: {.proof}
A $60^\circ$ rotation sends $u$ to $v$ and sends $v$ to $v-u$. These are the two columns of $A$.
:::

<1>4. The endomorphism $A-I$ of $\mathbb Z^2$ is an isomorphism.
:::
::: {.proof}
$$
A-I=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},
\qquad
\det(A-I)=1.
$$
Hence it is unimodular.
:::

<1>5. On $H_0(T^2)$ and $H_2(T^2)$, the induced map $R_*$ is the identity.
:::
::: {.proof}
The torus is connected, so every self-map acts as the identity on $H_0$. The rotation preserves orientation and has determinant $1$ on $H_1$, so it acts by $+1$ on the top homology $H_2(T^2)\cong\mathbb Z$.
:::

<1>6. The Wang exact sequence for the mapping torus gives
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,1,2,3,\\
0,&\text{otherwise}.
\end{cases}
$$
:::
::: {.proof}
The Wang sequence contains
$$
\cdots\to H_i(T^2)\xrightarrow{I-R_*}H_i(T^2)\to H_i(X)
\to H_{i-1}(T^2)\xrightarrow{I-R_*}H_{i-1}(T^2)\to\cdots.
$$
In degree $1$, $I-A$ is an isomorphism by <1>4, while in degrees $0$ and $2$ the map $I-R_*$ is zero by <1>5. Exactness then gives $H_3(X)\cong H_2(T^2)\cong\mathbb Z$, $H_2(X)\cong H_2(T^2)\cong\mathbb Z$, $H_1(X)\cong H_0(T^2)\cong\mathbb Z$, and connectedness gives $H_0(X)\cong\mathbb Z$.
:::
:::

