---
schema: qual/card@1
id: E-HAT-1.2-12
kind: problem
title: Fundamental groups of Klein bottle and related spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 12 and
    its figure on pages 53--54. The local statement and displayed relator match.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Used the cut-open fundamental polygon for the punctured bottle, then the
    radial deformation visible in the graph-complement figure to compare with
    R^3 minus Z.
---

The Klein bottle is usually pictured as a subspace of $\mathbb{R}^3$ like the subspace $X \subset \mathbb{R}^3$ shown in the first figure at the right.
If one wanted a model that could actually function as a bottle, one would delete the open disk bounded by the circle of self-intersection of $X$, producing a subspace $Y \subset X$.
Show that $\pi_1(X) \approx \mathbb{Z} * \mathbb{Z}$ and that $\pi_1(Y)$ has the presentation $\langle a, b, c \mid aba^{-1}b^{-1}cb^\varepsilon c^{-1} \rangle$ for $\varepsilon = \pm 1$.
(Changing the sign of $\varepsilon$ gives an isomorphic group, as it happens.)
Show also that $\pi_1(Y)$ is isomorphic to $\pi_1(\mathbb{R}^3 - Z)$ for $Z$ the graph shown in the figure.
The groups $\pi_1(X)$ and $\pi_1(Y)$ are not isomorphic, but this is not easy to prove; see the discussion in Example 1B.13.

::: {.solution}
We use the orientation convention giving $\varepsilon=-1$.
Reversing the orientation of the corresponding identified boundary circle gives the convention $\varepsilon=+1$ without changing the underlying space.

<1>1. The punctured bottle $Y$ has a CW structure with one $0$-cell, three $1$-cells $a,b,c$, and one $2$-cell attached along
\[
r=aba^{-1}b^{-1}cb^{-1}c^{-1}.
\]
::: {.proof}
Cut the surface in the source figure along arcs from the boundary of the deleted disk to the self-identification curves, so that the remaining $2$-cell is a disk.
After the cuts, all vertices are identified to one vertex and the three surviving edge classes are $a,b,c$.
Traversing the boundary of the cut-open disk once gives, in order,
\[
a,\ b,\ a^{-1},\ b^{-1},\ c,\ b^{-1},\ c^{-1}.
\]
Thus the attaching word is exactly $r$.
This is the standard one-disk fundamental polygon obtained by opening the bottle picture along the deleted self-intersection disk.
:::

<1>2. Therefore
\[
\boxed{
\pi_1(Y)
\cong
\left\langle a,b,c\ \middle|\
aba^{-1}b^{-1}cb^{-1}c^{-1}=1
\right\rangle .
}
\]
::: {.proof}
The $1$-skeleton in <1>1 is
\[
S^1\vee S^1\vee S^1,
\]
so its fundamental group is the free group $F(a,b,c)$.
Attaching the single $2$-cell quotients by the normal closure of its attaching word $r$.
This is precisely the displayed presentation by van Kampen.
:::

<1>3. With the opposite orientation convention on the indicated boundary identification, the same computation gives
\[
\pi_1(Y)
\cong
\left\langle a,b,c\ \middle|\
aba^{-1}b^{-1}cb c^{-1}=1
\right\rangle .
\]
::: {.proof}
Only the orientation in which that copy of the $b$-edge is traversed changes.
Since this is merely a change of orientation in the same CW decomposition of the same space $Y$, the two presentations present isomorphic groups.
Thus the answer can be written uniformly as
\[
\left\langle a,b,c\ \middle|\
aba^{-1}b^{-1}cb^{\varepsilon}c^{-1}=1
\right\rangle,
\qquad \varepsilon=\pm1.
\]
:::

<1>4. Reattaching the deleted disk to $Y$ to recover the immersed Klein-bottle model $X$ kills the generator $b$ in the presentation of <1>2.
::: {.proof}
In the cut-open model of <1>1, the boundary of the disk deleted at the circle of self-intersection is represented by the $b$-loop.
Passing from $Y$ back to $X$ attaches a $2$-cell along this boundary loop, so van Kampen adds the relation
\[
b=1.
\]
:::

<1>5. Hence
\[
\boxed{\pi_1(X)\cong\mathbb Z*\mathbb Z.}
\]
::: {.proof}
Adding $b=1$ to the presentation in <1>2 makes the original relator trivial:
\[
aba^{-1}b^{-1}cb^{-1}c^{-1}
\longmapsto
aa^{-1}cc^{-1}=1.
\]
Therefore
\[
\pi_1(X)
\cong
\langle a,c\mid\ \rangle
\cong F(a,c)
\cong\mathbb Z*\mathbb Z.
\]
:::

<1>6. The graph complement $\mathbb R^3\setminus Z$ has the same fundamental group as $Y$.
::: {.proof}
Use the graph $Z$ exactly as embedded in the rightmost source figure.
Take a sufficiently small regular neighborhood of the pictured graph and use the transverse cross-sections indicated by the drawing.
In every cross-section, the complement of the central graph point radially retracts onto the corresponding arc of the bottle surface $Y$.
These radial retractions agree along the edge and vertex cross-sections, so over a large ball containing $Z$ they give a deformation onto the pictured copy of $Y$ together with the outer boundary sphere.

Outside that ball, radial projection retracts the unbounded complement onto the same outer sphere.
Consequently
\[
\mathbb R^3\setminus Z\simeq Y\vee S^2.
\]
Since $S^2$ is simply connected, van Kampen gives
\[
\pi_1(\mathbb R^3\setminus Z)
\cong
\pi_1(Y)*\pi_1(S^2)
\cong
\pi_1(Y).
\]
:::

<1>7. Thus all requested groups are
\[
\pi_1(X)\cong\mathbb Z*\mathbb Z,
\qquad
\pi_1(Y)
\cong
\pi_1(\mathbb R^3\setminus Z)
\cong
\left\langle a,b,c\mid aba^{-1}b^{-1}cb^{\varepsilon}c^{-1}\right\rangle .
\]
::: {.proof}
Combine <1>2--<1>6.
:::
:::
