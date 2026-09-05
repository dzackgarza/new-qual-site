---
schema: qual/card@1
id: P-6UCWP
kind: problem
title: Euler characteristic of a cylinder after identifying two disjoint closed intervals
  on the boundary, and which bordered surfaces arise
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both questions against problem 6 of the official UGA Fall 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Repaired the incorrect disconnected example, verified chi=-1 by cell counting, and checked all four connected surface types arising from arc placement and seam orientation.
---

::: problem
Let $C$ be a cylinder.
Let $I$ and $J$ be disjoint closed intervals contained in $\partial C$.
What is the Euler characteristic of the surface $S$ obtained by identifying $I$ and $J$?
Can all surfaces with nonempty boundary and with this Euler characteristic be obtained from this construction?
:::

::: {.solution}
Assume that the identification $I\to J$ is by a homeomorphism, as usual in this construction.

<1>1. The quotient surface has
\[
\chi(S)=-1.
\]
::: {.proof}
The cylinder has
\[
\chi(C)=0.
\]
Choose a finite CW decomposition of $C$ for which $I$ and $J$ are disjoint subcomplexes, and subdivide so that the chosen homeomorphism $I\to J$ is cellular.
Passing to the quotient merges every cell of $I$ with the corresponding cell of $J$ and makes no other cell identifications.
Thus the alternating cell count decreases by
\[
\chi(I)=1.
\]
Therefore
\[
\chi(S)=\chi(C)-\chi(I)=0-1=-1.
\]
:::

<1>2. Up to homeomorphism, the connected compact surfaces with nonempty boundary and Euler characteristic $-1$ are exactly
\[
\Sigma_{0,3},
\qquad
\Sigma_{1,1},
\qquad
N_{1,2},
\qquad
N_{2,1},
\]
where $\Sigma_{g,b}$ is orientable of genus $g$ with $b$ boundary components and $N_{k,b}$ is nonorientable of genus $k$ with $b$ boundary components.
::: {.proof}
For an orientable connected compact surface,
\[
\chi(\Sigma_{g,b})=2-2g-b.
\]
The equation
\[
2-2g-b=-1,
\qquad b\ge1,
\]
is equivalent to $2g+b=3$, whose solutions are
\[
(g,b)=(0,3),(1,1).
\]
For a nonorientable connected compact surface,
\[
\chi(N_{k,b})=2-k-b.
\]
The equation
\[
2-k-b=-1,
\qquad k,b\ge1,
\]
is equivalent to $k+b=3$, whose solutions are
\[
(k,b)=(1,2),(2,1).
\]
The classification theorem for compact connected surfaces gives the stated list.
:::

<1>3. All four connected surfaces in <1>2 occur by identifying two boundary intervals of a cylinder.
::: {.proof}
The cylinder has two boundary circles.
There are two placement choices for the intervals and, for each placement, two inequivalent ways to glue the interval ends, corresponding to an untwisted or twisted seam.
Tracing the boundary arcs after the identification gives the following possibilities:

\[
\begin{array}{c|c|c|c}
\text{positions of }I,J&\text{seam}&\text{orientability}&\text{number of boundary components}\\
\hline
\text{same boundary circle}&\text{untwisted}&\text{orientable}&3\\
\text{same boundary circle}&\text{twisted}&\text{nonorientable}&2\\
\text{different boundary circles}&\text{untwisted}&\text{orientable}&1\\
\text{different boundary circles}&\text{twisted}&\text{nonorientable}&1
\end{array}
\]

Indeed, if the two intervals lie on the same boundary circle, cutting out their interiors leaves two boundary arcs; the untwisted identification closes these into two boundary circles, whereas the twisted identification joins them into one.
The other boundary circle is unchanged.
If the intervals lie on different boundary circles, the identification joins those two boundary circles into one, regardless of the twist.
The untwisted seam preserves an orientation of the cylinder, while the twisted seam reverses it along the glued band and produces a one-sided closed curve, so the latter quotient is nonorientable.

Together with <1>1 and the classification in <1>2, the four cases are therefore
\[
\Sigma_{0,3},
\qquad
N_{1,2},
\qquad
\Sigma_{1,1},
\qquad
N_{2,1},
\]
respectively.
Thus every connected compact surface with nonempty boundary and Euler characteristic $-1$ occurs.
:::

<1>4. If the word ``surface'' is allowed to include disconnected surfaces, then not every such surface arises from the construction.
::: {.proof}
The cylinder $C$ is connected, and every quotient of a connected space is connected.
Hence every surface obtained by identifying $I$ and $J$ is connected.
On the other hand,
\[
\Sigma_{0,3}\amalg(S^1\times[0,1])
\]
is a disconnected compact surface with nonempty boundary and
\[
\chi
=\chi(\Sigma_{0,3})+\chi(S^1\times[0,1])
=-1+0
=-1.
\]
It cannot be obtained as such a quotient.
Therefore, under the standard convention that a surface is connected, the answer to the second question is yes; if disconnected surfaces are admitted, the answer is no.
:::
:::
