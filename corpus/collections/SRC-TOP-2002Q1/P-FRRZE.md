---
schema: qual/card@1
id: P-FRRZE
kind: problem
title: Fundamental group of $\mathbb{R}^3$ minus the three coordinate axes
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked the statement and coordinate-axis figure against Section B,
    problem B2 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Radial projection strongly deformation retracts the complement onto S^2
    minus the six signed coordinate directions. Stereographic projection turns
    this into a five-punctured plane, whose standard graph spine is a wedge of
    five circles, giving the free group F_5.
---

::: {.problem}
Find the fundamental group of the space $X$ consisting of $\mathbb{R}^3$ with the three coordinate axes removed; see figure.

![](../../assets/Topology/figures/2002Q1-topology-B2.png)
:::

::: {.solution}
Let
\[
L=\{(x,0,0):x\in\mathbb R\}
\cup
\{(0,y,0):y\in\mathbb R\}
\cup
\{(0,0,z):z\in\mathbb R\},
\]
so that $X=\mathbb R^3\setminus L$.

<1>1. The space $X$ strongly deformation retracts onto
\[
S^2\setminus\{\pm e_1,\pm e_2,\pm e_3\}.
\]
::: {.proof}
Every point of $X$ is nonzero.
Define
\[
H:X\times[0,1]\longrightarrow X,
\qquad
H(v,t)=\left((1-t)+\frac{t}{\|v\|}\right)v.
\]
The scalar multiplying $v$ is strictly positive, so $H(v,t)$ lies on the same ray from the origin as $v$.
Consequently, if $v$ is not on a coordinate axis then no $H(v,t)$ lies on a coordinate axis.
Thus $H$ indeed takes values in $X$.

At $t=0$ it is the identity, while
\[
H(v,1)=\frac{v}{\|v\|}\in S^2.
\]
If $v\in S^2\cap X$, then $H(v,t)=v$ for every $t$.
Finally,
\[
S^2\cap L=\{\pm e_1,\pm e_2,\pm e_3\}.
\]
Hence $H$ is the asserted strong deformation retraction.
:::

<1>2. The punctured sphere in <1>1 is homeomorphic to a plane with five points removed.
::: {.proof}
Choose one of the six deleted points, say $-e_3$, as the pole for stereographic projection.
Stereographic projection gives a homeomorphism
\[
S^2\setminus\{-e_3\}\cong\mathbb R^2.
\]
The other five deleted points map to five distinct points
\[
p_1,\dots,p_5\in\mathbb R^2.
\]
Restricting the homeomorphism therefore gives
\[
S^2\setminus\{\pm e_1,\pm e_2,\pm e_3\}
\cong
\mathbb R^2\setminus\{p_1,\dots,p_5\}.
\]
:::

<1>3. The five-punctured plane is homotopy equivalent to a wedge of five circles.
::: {.proof}
Choose a large closed disk $D\subset\mathbb R^2$ containing all five punctures in its interior.
Radially collapsing the complement of $D$ onto $\partial D$ gives a strong deformation retraction
\[
\mathbb R^2\setminus\{p_1,\dots,p_5\}
\simeq
D\setminus\{p_1,\dots,p_5\}.
\]

Choose pairwise disjoint small closed disks $D_i$ centered at $p_i$ and contained in $\operatorname{int}D$.
Inside each punctured disk $D_i\setminus\{p_i\}$, push points radially outward to $\partial D_i$, fixing the complement of the interiors of the $D_i$.
This gives a deformation retraction onto
\[
M=D\setminus\bigcup_{i=1}^5\operatorname{int}(D_i),
\]
a disk with five holes.

Choose five pairwise disjoint arcs joining the five inner boundary circles to the outer boundary.
Cutting $M$ along these arcs produces a disk.
Equivalently, $M$ has a handle decomposition with one $0$-handle and five $1$-handles.
Collapsing the $0$-handle to a point and each $1$-handle across its transverse interval gives a deformation retraction onto the core graph
\[
\bigvee_{i=1}^5 S^1.
\]
Thus
\[
\mathbb R^2\setminus\{p_1,\dots,p_5\}
\simeq
\bigvee_{i=1}^5S^1.
\]
:::

<1>4. Therefore
\[
\pi_1(X)\cong F_5,
\]
the free group of rank $5$.
::: {.proof}
By <1>1--<1>3,
\[
X\simeq\bigvee_{i=1}^5S^1.
\]
The Seifert--van Kampen theorem gives
\[
\pi_1\left(\bigvee_{i=1}^5S^1\right)
\cong
\underbrace{\mathbb Z*\cdots*\mathbb Z}_{5\text{ factors}}
=F_5.
\]
Hence $\pi_1(X)\cong F_5$.
:::
:::
