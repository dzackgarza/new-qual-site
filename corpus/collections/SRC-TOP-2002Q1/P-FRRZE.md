---
schema: qual/card@1
id: P-FRRZE
kind: problem
title: Fundamental group of $\RR^3$ minus the three coordinate axes
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
Find the fundamental group of the space $X$ consisting of $\RR^3$ with the three coordinate axes removed; see figure.

![](../../assets/Topology/figures/2002Q1-topology-B2.png)
:::

::: {.solution}
Let $L\subset\RR^3$ be the union of the three coordinate axes, so that $X=\RR^3\setminus L$, and let $e_1,e_2,e_3$ be the standard basis of $\RR^3$.

<1>1. The space $X$ strongly deformation retracts onto $S^2\setminus\{\pm e_1,\pm e_2,\pm e_3\}$.

::: {.proof}
Every point of $X$ is nonzero.
Define $H\colon X\times[0,1]\to\RR^3$ by
$$H(v,t)=\left((1-t)+\frac{t}{\norm{v}}\right)v.$$
The scalar multiplying $v$ is strictly positive, so $H(v,t)$ lies on the open ray from the origin through $v$.
Each coordinate axis is a union of rays from the origin, so if $v\notin L$ then $H(v,t)\notin L$; thus $H$ takes values in $X$.

At $t=0$ it is the identity, and $H(v,1)=v/\norm{v}\in S^2$.
If $v\in S^2\cap X$, then $H(v,t)=v$ for every $t$.
Finally, $S^2\cap L=\{\pm e_1,\pm e_2,\pm e_3\}$.
Hence $H$ is a strong deformation retraction of $X$ onto $S^2\setminus\{\pm e_1,\pm e_2,\pm e_3\}$.
:::

<1>2. $S^2\setminus\{\pm e_1,\pm e_2,\pm e_3\}$ is homeomorphic to $\RR^2\setminus\{p_1,\ldots,p_5\}$ for five distinct points $p_1,\ldots,p_5\in\RR^2$.

::: {.proof}
Stereographic projection from $-e_3$ is a homeomorphism $S^2\setminus\{-e_3\}\cong\RR^2$.
It sends the other five deleted points to five distinct points $p_1,\ldots,p_5\in\RR^2$, and its restriction is the required homeomorphism.
:::

<1>3. $\RR^2\setminus\{p_1,\ldots,p_5\}$ is homotopy equivalent to $\bigvee_{i=1}^5 S^1$.

::: {.proof}
Choose a closed disk $D\subset\RR^2$ containing all five punctures in its interior.
Radially collapsing the complement of $D$ onto $\partial D$ gives a strong deformation retraction of $\RR^2\setminus\{p_1,\ldots,p_5\}$ onto $D\setminus\{p_1,\ldots,p_5\}$.

Choose pairwise disjoint closed disks $D_i$ centered at $p_i$ and contained in $\operatorname{int}D$.
Inside each punctured disk $D_i\setminus\{p_i\}$, push points radially outward to $\partial D_i$, fixing the complement of the interiors of the $D_i$.
This gives a deformation retraction onto the disk with five holes $M=D\setminus\bigcup_{i=1}^5\operatorname{int}(D_i)$.

Choose five pairwise disjoint arcs joining the five inner boundary circles to the outer boundary.
Cutting $M$ along these arcs produces a disk, so $M$ has a handle decomposition with one $0$-handle and five $1$-handles.
Collapsing the $0$-handle to a point and each $1$-handle across its transverse interval gives a deformation retraction onto the core graph $\bigvee_{i=1}^5 S^1$.
:::

<1>4. Q.E.D.

::: {.proof}
By steps <1>1, <1>2, and <1>3, $X\simeq\bigvee_{i=1}^5S^1$.
By the Seifert--van Kampen theorem,
$$\pi_1(X)\cong\pi_1\Bigl(\bigvee_{i=1}^5S^1\Bigr)\cong\underbrace{\ZZ*\cdots*\ZZ}_{5\text{ factors}}=\boxed{F_5},$$
the free group of rank $5$.
:::
:::
