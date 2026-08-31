---
schema: qual/card@1
id: E-HAT-2.1-7
kind: exercise
title: $\Delta$-complex structure on $S^3$ with a single 3-simplex
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Find a way of identifying pairs of faces of $\Delta^3$ to produce a $\Delta$-complex structure on $S^3$ having a single 3 simplex, and compute the simplicial homology groups of this $\Delta$-complex.

::: {.solution}
**Goal.** Give $S^3$ a $\Delta$-complex structure with a single $3$-simplex and compute its simplicial homology.

<1>1. Construct the $\Delta$-complex by identifying the four faces of $\Delta^3$ in two pairs.
<2>1. Label the vertices $v_0, v_1, v_2, v_3$ and the faces $F_0 = [v_1,v_2,v_3]$, $F_1 = [v_0,v_2,v_3]$, $F_2 = [v_0,v_1,v_3]$, $F_3 = [v_0,v_1,v_2]$.
::: {.proof}
these are the four $2$-faces of the tetrahedron $\Delta^3$.
:::
<2>2. Identify $F_0 \sim F_1$ (sending $v_1 \mapsto v_0$) and $F_2 \sim F_3$ (sending $v_3 \mapsto v_2$).
::: {.proof}
this glues the four faces in two pairs, as required.
:::
<2>3. The resulting $\Delta$-complex has one $3$-simplex, two $2$-simplices, three $1$-simplices, and two $0$-simplices.
::: {.proof}
the two face-pairs give two $2$-simplices $P = F_0 \sim F_1$ and $Q = F_2 \sim F_3$; the vertex identifications give $v_0 \sim v_1 =: A$ and $v_2 \sim v_3 =: B$; the six edges collapse to three: the loop $e_{01} = [v_0,v_1]$ at $A$, the loop $e_{23} = [v_2,v_3]$ at $B$, and a single edge $c$ from $A$ to $B$ (the four cross-edges $[v_0,v_2], [v_0,v_3], [v_1,v_2], [v_1,v_3]$ are all identified).
:::

<1>2. Compute the boundary maps.
<2>1. $\partial_3 = 0$.
::: {.proof}
$\partial_3(\sigma) = F_0 - F_1 + F_2 - F_3 = P - P + Q - Q = 0$.
:::
<2>2. $\partial_2(P) = e_{23}$ and $\partial_2(Q) = e_{01}$.
::: {.proof}
$\partial_2(F_0) = [v_2,v_3] - [v_1,v_3] + [v_1,v_2] = e_{23} - c + c = e_{23}$; $\partial_2(F_2) = [v_1,v_3] - [v_0,v_3] + [v_0,v_1] = c - c + e_{01} = e_{01}$.
:::
<2>3. $\partial_1(e_{01}) = 0$, $\partial_1(e_{23}) = 0$, $\partial_1(c) = B - A$.
::: {.proof}
$e_{01}$ is a loop at $A$ and $e_{23}$ a loop at $B$, so their boundaries vanish; $c$ runs from $A$ to $B$.
:::

<1>3. Compute the homology.
<2>1. $H_0 = \ZZ$.
::: {.proof}
$C_0 = \ZZ^2$ and $\im \partial_1 = \ZZ(B - A)$, so $H_0 = \ZZ^2/\ZZ = \ZZ$ (the space is connected).
:::
<2>2. $H_1 = 0$.
::: {.proof}
$\ker \partial_1 = \ZZ e_{01} \oplus \ZZ e_{23} = \ZZ^2$, and $\im \partial_2 = \ZZ e_{23} \oplus \ZZ e_{01} = \ZZ^2$, so $H_1 = \ZZ^2/\ZZ^2 = 0$.
:::
<2>3. $H_2 = 0$.
::: {.proof}
$\partial_2$ is injective (it sends the basis $P, Q$ to the independent elements $e_{23}, e_{01}$), so $\ker \partial_2 = 0$; hence $H_2 = 0/\im \partial_3 = 0$.
:::
<2>4. $H_3 = \ZZ$.
::: {.proof}
$\ker \partial_3 = \ZZ$ and there is no $4$-simplex, so $H_3 = \ZZ/0 = \ZZ$.
:::

<1>4. Q.E.D.
::: {.proof}
$H_0 = H_3 = \ZZ$ and $H_1 = H_2 = 0$, the homology of $S^3$.
:::
:::
