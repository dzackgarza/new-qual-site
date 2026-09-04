---
schema: qual/card@1
id: P-KJBAM
kind: problem
title: Free subgroup on five generators in $F_2$ via a cover of $S^1\vee S^1$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 4 of the official UGA Spring 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the four-sheeted graph covering locally at every vertex, the maximal-tree rank-five calculation, and the explicit Schreier basis of the injected subgroup.
---

::: problem
Prove that the free group on two generators contains a subgroup isomorphic to the free group on five generators by constructing an appropriate covering space of $S^1 \lor S^1$.
:::

::: {.solution}
Let
\[
R=S^1_a\vee S^1_b,
\]
so that
\[
\pi_1(R,*)\cong F(a,b),
\]
the free group on two generators.

<1>1. Define a graph $\widetilde R$ with vertices
\[
v_0,v_1,v_2,v_3.
\]
For each $i\in\ZZ/4\ZZ$, give it an oriented edge
\[
A_i:v_i\longrightarrow v_{i+1}
\]
and a loop
\[
B_i:v_i\longrightarrow v_i.
\]
Map every vertex to the wedge point $*$.
On each oriented edge $A_i$ use the standard characteristic map to $S^1_a$, sending the interior of $A_i$ homeomorphically and orientation-preservingly onto $S^1_a\setminus\{*\}$; do the analogous thing from each $B_i$ to $S^1_b$.
::: {.proof}
This specifies a continuous cellular map
\[
p:\widetilde R\longrightarrow R.
\]
The $A_i$ form a $4$-cycle, so $\widetilde R$ is connected.
:::

<1>2. The map $p$ is a four-sheeted covering map.
::: {.proof}
The inverse image of the wedge point is
\[
p^{-1}(*)=\{v_0,v_1,v_2,v_3\}.
\]
At each $v_i$ there is exactly one half-edge mapping to each of the four oriented germs
\[
a,\ a^{-1},\ b,\ b^{-1}
\]
at $*$: the outgoing edge $A_i$, the incoming edge $A_{i-1}$, and the two ends of the loop $B_i$.
Thus the star of every $v_i$ maps homeomorphically onto a sufficiently small star neighborhood of $*$ in $R$.
Away from the vertices, every edge maps homeomorphically onto the corresponding open edge of $R$.
Hence every point of $R$ has an evenly covered neighborhood, with four sheets.
:::

<1>3. The group $\pi_1(\widetilde R,v_0)$ is free of rank $5$.
::: {.proof}
Take the maximal tree
\[
T=A_0\cup A_1\cup A_2.
\]
Collapsing $T$ to a point is a homotopy equivalence of graphs.
The edges not in $T$ are
\[
A_3,\ B_0,\ B_1,\ B_2,\ B_3,
\]
so the quotient graph $\widetilde R/T$ is a wedge of five circles.
Therefore
\[
\pi_1(\widetilde R,v_0)\cong F_5.
\]
:::

<1>4. The induced homomorphism
\[
p_*:\pi_1(\widetilde R,v_0)\longrightarrow\pi_1(R,*)
\]
is injective.
::: {.proof}
An induced map on fundamental groups of a covering is injective.
Indeed, if a based loop $\gamma$ in $\widetilde R$ has $p\circ\gamma$ null-homotopic in $R$, lift a based null-homotopy of $p\circ\gamma$ through the covering $p$.
Uniqueness of lifts makes its boundary lift equal to $\gamma$, so the lifted homotopy contracts $\gamma$ in $\widetilde R$.
Thus $[\gamma]=1$.
:::

<1>5. Consequently $F(a,b)$ contains a subgroup isomorphic to $F_5$.
More explicitly, the image subgroup has free basis
\[
\boxed{
b,
\quad
aba^{-1},
\quad
a^2ba^{-2},
\quad
a^3ba^{-3},
\quad
a^4.
}
\]
::: {.proof}
By <1>3 and <1>4, the subgroup
\[
p_*\pi_1(\widetilde R,v_0)\le F(a,b)
\]
is isomorphic to $F_5$.

For the displayed basis, use the maximal tree $T$ from <1>3. The non-tree loop $B_i$ is based at $v_0$ by first following
\[
A_0A_1\cdots A_{i-1}
\]
from $v_0$ to $v_i$ and then returning along the same tree path.
Its image in $R$ represents
\[
a^i b a^{-i}
\qquad(0\le i\le3).
\]
The remaining non-tree edge $A_3$ closes the $A$-cycle and maps to $a^4$.
These five loops are the standard free basis associated to the maximal tree, proving the claim.
:::
:::
