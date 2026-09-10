---
schema: qual/card@1
id: E-HAT-2.2-28
kind: problem
title: Mayer–Vietoris computations for torus with Möbius band and $\mathbb{RP}^2$ with Möbius band
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 28; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/Wang-sequence calculation checked.
---

(a) Use the Mayer–Vietoris sequence to compute the homology groups of the space obtained from a torus $S^1 \times S^1$ by attaching a Möbius band via a homeomorphism from the boundary circle of the Möbius band to the circle $S^1 \times \{x_0\}$ in the torus.

(b) Do the same for the space obtained by attaching a Möbius band to $\mathbb{RP}^2$ via a homeomorphism of its boundary circle to the standard $\mathbb{RP}^1 \subset \mathbb{RP}^2$.

::: {.solution}
For each attachment, use Mayer--Vietoris with the original space and the Möbius band, whose intersection is the common attaching circle. The Möbius band deformation retracts onto its core circle, and its boundary circle represents twice the core generator in $H_1$.

<1>1. In part (a), let
\[
Y=T^2\cup_{S^1}M,
\]
where the boundary of the Möbius band $M$ is attached to the circle $S^1\times\{x_0\}$ in the torus. Then
\[
H_i(Y)\cong
\begin{cases}
\mathbb Z,&i=0,2,\\
\mathbb Z^2,&i=1,\\
0,&i>2.
\end{cases}
\]
::: {.proof}
Choose generators $a,b$ for
\[
H_1(T^2)\cong\mathbb Z^2
\]
with $a$ represented by the attaching circle, and let $c$ generate
\[
H_1(M)\cong\mathbb Z.
\]
The Mayer--Vietoris map from the intersection is
\[
H_1(S^1)=\mathbb Z
\longrightarrow
H_1(T^2)\oplus H_1(M)=\mathbb Z^3,
\qquad
1\longmapsto(a,-2c).
\]
This map is injective, and its image is primitive because the coordinate of $a$ is $1$. Since $H_2(S^1)=H_2(M)=0$, the exact sequence gives
\[
0\to H_2(T^2)=\mathbb Z\to H_2(Y)\to\ker(1\mapsto(a,-2c))=0,
\]
so $H_2(Y)\cong\mathbb Z$. In degree one,
\[
H_1(Y)\cong\mathbb Z^3/\langle(a,-2c)\rangle\cong\mathbb Z^2.
\]
Connectedness gives $H_0(Y)=\mathbb Z$.
:::

<1>2. In part (b), let
\[
Z=\mathbb{RP}^2\cup_{\mathbb{RP}^1}M.
\]
Then
\[
H_i(Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z_4,&i=1,\\
0,&i\ge2.
\end{cases}
\]
::: {.proof}
Let $u$ generate
\[
H_1(\mathbb{RP}^2)\cong\mathbb Z_2
\]
and let $c$ generate $H_1(M)\cong\mathbb Z$. The standard circle $\mathbb{RP}^1$ represents $u$, while the boundary of $M$ represents $2c$. Hence the Mayer--Vietoris map is
\[
\mathbb Z\longrightarrow\mathbb Z_2\oplus\mathbb Z,
\qquad
1\longmapsto(u,-2c).
\]
It is injective because of the infinite cyclic second coordinate, so $H_2(Z)=0$. Its cokernel has presentation
\[
\langle u,c\mid 2u=0,\ u=2c\rangle
\cong
\langle c\mid4c=0\rangle
\cong\mathbb Z_4.
\]
Thus $H_1(Z)\cong\mathbb Z_4$, and connectedness gives $H_0(Z)=\mathbb Z$.
:::
:::
