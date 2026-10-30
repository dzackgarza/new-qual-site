---
schema: qual/card@1
id: P-TOPF23B
kind: problem
title: "Homology of a cube with faces identified in pairs"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $X$ be the space obtained by identifying the faces of a standard cube $I^3$ in pairs, as shown in the source figure (top and bottom by a translation, front and back by a reflection that turns the face upside down, left and right by a half-turn).
Compute the integral homology groups $H_*(X; \ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #gluings}

Use coordinates $(x,y,z)\in I^3$, with $x$ from left to right, $y$ from front to back and $z$ from bottom to top. The figure gives the face identifications
$$
(x,y,0)\sim(x,y,1),\qquad (x,0,z)\sim(x,1,1-z),\qquad (0,y,z)\sim(1,1-y,1-z).
$$

::: pf-proof

The flags on the top and bottom faces have the same orientation, so that pair is a translation. The flag on the back face has its pennant at the bottom of the pole and still points in the $+x$ direction, while the flag on the front face has its pennant at the top: that pair is the reflection $z\mapsto1-z$. The glyph on the right face is the glyph on the left face turned through $180^\circ$ in the $(y,z)$-plane: the arm at the top of the pole pointing to the back becomes an arm at the bottom of the pole pointing to the front.

:::

:::

::: {.pf-step #klein}

$X$ is the mapping torus of the homeomorphism
$$\varphi:K\to K,\qquad \varphi(y,z)=(1-y,-z),$$
of the Klein bottle $K=\bigl([0,1]\times\RR/\ZZ\bigr)/(0,z)\sim(1,-z)$.

::: pf-proof

The top/bottom pairing makes $z$ a coordinate on $\RR/\ZZ$, and in that coordinate $1-z=-z$. The front/back pairing then glues each slice $\{x\}\times I\times(\RR/\ZZ)$ into $K$, so the quotient so far is $I\times K$. The left/right pairing glues $\{0\}\times K$ to $\{1\}\times K$ by $\varphi$. The map $\varphi$ respects the relation defining $K$: it sends $(0,z)$ to $(1,-z)$ and $(1,-z)$ to $(0,z)$, which are identified points.

:::

:::

::: {.pf-step #action}

Let $a$ be the class of the loop $z\mapsto(y_0,z)$ and $b$ the class of the loop $y\mapsto(y,0)$ in $K$. Then
$$H_1(K;\ZZ)=\ZZ b\oplus(\ZZ/2)a,\qquad \varphi_*b=-b,\qquad \varphi_*a=a,$$
and $\varphi_*$ is the identity on $H_0(K)$, while $H_2(K;\ZZ)=0$.

::: pf-proof

The relation $bab^{-1}=a^{-1}$ of $\pi_1(K)$ gives $2a=0$ in $H_1$, and $b$ has infinite order. The map $\varphi$ fixes the base point $(0,0)\sim(1,0)$, carries the loop $y\mapsto(y,0)$ to the same loop run backwards, and carries the $z$-loop to a $z$-loop run backwards, which is $-a=a$.

:::

:::

::: {.pf-step #wang}

For each $k$ there is a short exact sequence
$$
0\to\operatorname{coker}(1-\varphi_*\mid H_k(K))\to H_k(X)\to\ker(1-\varphi_*\mid H_{k-1}(K))\to0.
$$

::: pf-proof

This is the Wang sequence of the mapping torus of $\varphi$.

:::

:::

::: pf-qed

By Step [](#action){.pf-ref}, $1-\varphi_*$ is $0$ on $H_0(K)$ and is $(n,\epsilon)\mapsto(2n,0)$ on $H_1(K)=\ZZ\oplus\ZZ/2$. Its cokernel on $H_1$ is $\ZZ/2\oplus\ZZ/2$ and its kernel on $H_1$ is $0\oplus\ZZ/2$. Step [](#wang){.pf-ref} gives
$$
\boxed{H_k(X;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ\oplus(\ZZ/2)^2,&k=1,\\
\ZZ/2,&k=2,\\
0,&k\ge3.
\end{cases}}
$$
The sequence in degree $1$ splits because its quotient $\ker(1-\varphi_*\mid H_0)=\ZZ$ is free. As a check, $X$ is a closed nonorientable $3$-manifold, so $H_3(X;\ZZ)=0$, the torsion of $H_2$ is $\ZZ/2$, and the Euler characteristic $1-1+0-0$ is $0$.

:::

:::

:::
