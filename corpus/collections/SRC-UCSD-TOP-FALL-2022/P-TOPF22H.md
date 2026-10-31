---
schema: qual/card@1
id: P-TOPF22H
kind: problem
title: "Homology of a cube with pairs of faces glued"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    Read Problem 8 and its cube figure on the rendered exam page. The
    paired P glyphs are upright, the right R is reflected, and the Q
    glyphs are vertically reflected. The statement now gives the face
    maps in coordinates.
---

::: {.problem}
Write the cube as $I^3$ with coordinates $(x,y,z)$. Form $X$ by the
face identifications shown in the Fall 2022 exam figure:
$$
\begin{aligned}
(x,0,z)&\sim(x,1,z) &&(P),\\
(0,y,z)&\sim(1,1-y,z) &&(R),\\
(x,y,0)&\sim(x,1-y,1) &&(Q).
\end{aligned}
$$
Compute the homology $H_*(X; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step

The $P$ pairing makes the $y$ direction a circle. The $R$ pairing
then makes each horizontal slice a Klein bottle $K$.

::: pf-proof

After the $P$ pairing, $(x,y)$ ranges over $I\times S^1$. The $R$
pairing identifies $(0,y)$ with $(1,1-y)$, the mapping-torus
description of the Klein bottle. The two pairings do not involve
$z$, so their quotient is $K\times I$.

:::

:::

::: pf-step

The $Q$ pairing makes $X$ the mapping torus of the involution
$$
f:K\longrightarrow K,\qquad f([x,y])=[x,1-y].
$$

::: pf-proof

The $Q$ face map fixes $x$ and reflects the $y$ circle. It respects
the $R$ identification: reflecting $y$ twice gives back $y$.
Thus it descends to the displayed homeomorphism of $K$.

:::

:::

::: pf-step

The map $f$ is isotopic to the identity on $K$. Hence $X$ is
homeomorphic to $K\times S^1$.

::: pf-proof

In the mapping-torus model
$$
K=(\RR\times S^1)/((x,y)\sim(x+1,1-y)),
$$
translation in the first coordinate gives an isotopy
$$
F_t([x,y])=[x+t,y],\qquad 0\le t\le1.
$$
The relations make every $F_t$ well defined. We have $F_0=\operatorname{id}$
and $F_1([x,y])=[x,1-y]=f([x,y])$. A mapping torus of a homeomorphism
isotopic to the identity is homeomorphic to the product with $S^1$.

:::

:::

::: pf-step

The integral homology of $K$ is
$$
H_0(K)=\ZZ,\qquad
H_1(K)=\ZZ\oplus\ZZ/2,\qquad
H_k(K)=0\quad(k\ge2).
$$

::: pf-proof

The standard cell structure of the Klein bottle has one vertex, two
edges and one 2-cell. Its 2-cell boundary is twice the
orientation-reversing edge, giving the displayed homology.

:::

:::

::: pf-step

Therefore
$$
\boxed{H_k(X;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ^2\oplus\ZZ/2,&k=1,\\
\ZZ\oplus\ZZ/2,&k=2,\\
0,&k>3.
\end{cases}}
$$

::: pf-proof

Use the integral Künneth theorem on $K\times S^1$. The homology
of $S^1$ is free, so there are no Tor terms. Thus
$H_1(X)=H_1(K)\oplus H_0(K)$ and
$H_2(X)=H_1(K)\otimes H_1(S^1)$; all higher groups vanish.

:::

:::

:::

:::
