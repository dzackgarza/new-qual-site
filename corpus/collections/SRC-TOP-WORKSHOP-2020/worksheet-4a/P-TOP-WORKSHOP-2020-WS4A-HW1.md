---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW1
kind: problem
title: A Δ-complex structure and chain complex for the standard 2-simplex
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the boundary maps as their own steps. Re-checked
    the signs against the formula $\partial[v_0,\ldots,v_n]=\sum_i(-1)^i[v_0,\ldots,\widehat{v_i},
    \ldots,v_n]$: $\partial_2\sigma=[v_1,v_2]-[v_0,v_2]+[v_0,v_1]$, that is $e_{12}-e_{02}+e_{01}$, and
    $\partial_1[v_i,v_j]=[v_j]-[v_i]$; the composite is
    $(v_2-v_1)-(v_2-v_0)+(v_1-v_0)=0$, computed term by term. Added: the degree-wise description of
    the chain groups, the reason the boundary formula gives these signs, and the resulting homology
    $\ZZ$ in degree $0$ and $0$ above, none of which the earlier solution stated. No defect found in
    the statement. The collection's provenance is the worksheet, so no retained solution set covers
    the item.
---

::: {.problem}
Give a $\Delta$-complex structure for a standard 2-simplex $\Delta$ and write down its chain complex.
Explicitly describe the boundary homomorphisms.
:::

::: {.solution}
No retained solution set covers this item, the collection's provenance being the worksheet, so the computation is the card's own; it uses the formula $\partial[v_0,\ldots,v_n]=\sum_i(-1)^i[v_0,\ldots,\widehat{v_i},\ldots,v_n]$ for the boundary in a $\Delta$-complex.

::: pf

::: {.pf-step #structure}
The standard $2$-simplex $\Delta$ has vertices $v_0,v_1,v_2$, edges $e_{01}=[v_0,v_1]$, $e_{12}=[v_1,v_2]$, $e_{02}=[v_0,v_2]$ oriented by increasing index, and one $2$-simplex $\sigma=[v_0,v_1,v_2]$.

::: pf-proof
A $\Delta$-complex structure consists of a set of vertices, a set of edges each with an orientation and an ordered pair of endpoints, and a set of $n$-simplices for each $n$, with the faces attached by the prescribed identifications. For the standard $2$-simplex the three edges are the three pairs of vertices, each attached to its endpoints, and the single $2$-simplex has its boundary attached along $e_{01},e_{12},e_{02}$ in the order given by its orientation.
:::

:::

::: {.pf-step #complex}
The associated chain complex is
$$
0\to\ZZ\langle\sigma\rangle\xrightarrow{\partial_2}\ZZ\langle e_{01},e_{02},e_{12}\rangle\xrightarrow{\partial_1}\ZZ\langle v_0,v_1,v_2\rangle\to0
$$
with the displayed groups in degrees $2,1,0$ and zero elsewhere.

::: pf-proof
The $n$-th chain group of a $\Delta$-complex is free abelian on its $n$-simplices, so $C_2=\ZZ\langle\sigma\rangle$, $C_1=\ZZ\langle e_{01},e_{02},e_{12}\rangle$ and $C_0=\ZZ\langle v_0,v_1,v_2\rangle$; there are no simplices in other degrees, so those groups vanish. The maps between them are the boundary homomorphisms, which are determined below.
:::

:::

::: {.pf-step #boundary-two}
$\partial_2\sigma=e_{12}-e_{02}+e_{01}$.

::: pf-proof
By the boundary formula with $n=2$, $\partial_2[v_0,v_1,v_2]=[v_1,v_2]-[v_0,v_2]+[v_0,v_1]$, the alternating signs coming from $(-1)^i$ for $i=0,1,2$; in the notation above this is $e_{12}-e_{02}+e_{01}$.
:::

:::

::: {.pf-step}
$\partial_1e_{01}=v_1-v_0$, $\partial_1e_{02}=v_2-v_0$, $\partial_1e_{12}=v_2-v_1$, and $\partial_1\partial_2=0$.

::: pf-proof
The boundary formula with $n=1$ gives $\partial_1[v_i,v_j]=[v_j]-[v_i]$, which is the three displayed values. Then
$$
\partial_1\partial_2\sigma=(v_2-v_1)-(v_2-v_0)+(v_1-v_0)=v_2-v_1-v_2+v_0+v_1-v_0=0,
$$
so $\partial^2=0$, as a chain complex requires. The complex above is therefore the simplicial chain complex of $\Delta$, and its homology is $\ZZ$ in degree $0$ and $0$ in degrees $1,2$.
:::

:::

:::
:::
