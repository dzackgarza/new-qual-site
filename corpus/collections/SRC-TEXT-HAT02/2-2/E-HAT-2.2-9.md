---
schema: qual/card@1
id: E-HAT-2.2-9
kind: problem
title: Homology of four specific 2-complexes
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 9; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Computed all four cases by quotient/CW/Kunneth/relative-homology arguments, including the orientation sign in the pair-of-pants case.
---

Compute the homology groups of the following 2 complexes:

(a) The quotient of $S^2$ obtained by identifying north and south poles to a point.

(b) $S^1 \times (S^1 \lor S^1)$.

(c) The space obtained from $D^2$ by first deleting the interiors of two disjoint subdisks in the interior of $D^2$ and then identifying all three resulting boundary circles together via homeomorphisms preserving clockwise orientations of these circles.

(d) The quotient space of $S^1 \times S^1$ obtained by identifying points in the circle $S^1 \times \{x_0\}$ that differ by $2\pi/m$ rotation and identifying points in the circle $\{x_0\} \times S^1$ that differ by $2\pi/n$ rotation.

::: {.solution}
We compute the four spaces separately.

<1>1. In part (a), if $Y$ is obtained from $S^2$ by identifying the north and south poles, then
\[
Y\simeq S^2\vee S^1.
\]
Hence
\[
H_i(Y)\cong
\begin{cases}
\mathbb Z,&i=0,2,\\
\mathbb Z,&i=1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Choose an embedded arc in $S^2$ joining the two poles. After the endpoints are identified, this arc becomes a circle. Collapsing the arc before the endpoint identification gives the standard quotient description of a wedge $S^2\vee S^1$; equivalently one obtains a CW structure with one cell in dimensions $0,1,2$ and zero cellular differentials. Thus the displayed homology follows.
:::

<1>2. In part (b), for
\[
Y=S^1\times(S^1\vee S^1),
\]
one has
\[
H_i(Y)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^3,&i=1,\\
\mathbb Z^2,&i=2,\\
0,&i>2.
\end{cases}
\]
::: {.proof}
The homology of $S^1\vee S^1$ is $\mathbb Z$ in degree $0$, $\mathbb Z^2$ in degree $1$, and zero otherwise. Since all groups involved are free, the Kunneth formula has no Tor term. Therefore
\[
H_1(Y)\cong H_1(S^1)\otimes H_0(S^1\vee S^1)
\oplus H_0(S^1)\otimes H_1(S^1\vee S^1)
\cong\mathbb Z^3,
\]
and
\[
H_2(Y)\cong H_1(S^1)\otimes H_1(S^1\vee S^1)
\cong\mathbb Z^2.
\]
:::

<1>3. In part (c), let $P$ be the pair of pants and let $Y$ be the quotient obtained by identifying its three boundary circles, preserving their clockwise orientations. Then
\[
H_i(Y)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^2,&i=1,\\
0,&i\ge2.
\end{cases}
\]
::: {.proof}
Let $C\subset Y$ be the common image of the three boundary circles. Since
\[
Y/C\cong P/\partial P,
\]
we have
\[
H_*(Y,C)\cong H_*(P,\partial P).
\]
For an oriented pair of pants,
\[
H_2(P,\partial P)\cong\mathbb Z,
\qquad
H_1(P,\partial P)\cong\mathbb Z^2,
\qquad
H_0(P,\partial P)=0.
\]
The relevant part of the long exact sequence is
\[
0\to H_2(Y)\to\mathbb Z
\xrightarrow{\delta}\mathbb Z
\to H_1(Y)\to\mathbb Z^2\to0.
\]
Take the generator of $H_1(C)$ to be clockwise. For the standard orientation of the planar pair of pants, the induced boundary orientation is counterclockwise on the outer boundary and clockwise on each inner boundary. Since all three are identified preserving clockwise orientation, the boundary of the relative fundamental class maps to
\[
(-1)+1+1=1
\]
times the generator of $H_1(C)$. Thus $\delta$ is an isomorphism. Hence $H_2(Y)=0$ and $H_1(Y)\cong\mathbb Z^2$.
:::

<1>4. In part (d), let $Y_{m,n}$ be the stated quotient of the torus. Then
\[
H_i(Y_{m,n})\cong
\begin{cases}
\mathbb Z,&i=0,2,\\
\mathbb Z^2,&i=1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Use the usual square CW structure on the torus. After the quotient, the two coordinate circles are still circles, say $a$ and $b$, but the original horizontal edge maps to $a$ with degree $m$ and the original vertical edge maps to $b$ with degree $n$. The open $2$-cell is unchanged. Hence the attaching word of the $2$-cell becomes
\[
a^m b^n a^{-m}b^{-n}.
\]
The cellular boundary $d_2:C_2\to C_1$ records exponent sums in the two $1$-cells, and both exponent sums are zero. Thus
\[
0\longrightarrow\mathbb Z\xrightarrow{0}\mathbb Z^2\xrightarrow{0}\mathbb Z\longrightarrow0
\]
is the cellular chain complex, yielding the displayed groups.
:::
:::
