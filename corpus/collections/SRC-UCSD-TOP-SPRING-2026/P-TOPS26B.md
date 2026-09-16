---
schema: qual/card@1
id: P-TOPS26B
kind: problem
title: Finite 2-complex realizing a finitely presented group
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finitely presented group.
Show that there is a finite two dimensional CW complex whose fundamental group is isomorphic to $G$.
:::

::: {.solution}
<1>1. Choose a finite presentation $G=\langle x_1,\dots,x_r\mid w_1,\dots,w_s\rangle$.
::: {.proof}
This exists by hypothesis.
:::

<1>2. Start with the wedge $X^{(1)}=\bigvee_{i=1}^rS^1$, one circle for each generator, and attach one $2$-cell along a loop representing each relator $w_j$.
::: {.proof}
Every word in the free group on the circle generators is represented by a based loop in the wedge.
:::

<1>3. The resulting finite $2$-dimensional CW complex $X$ satisfies
$$\boxed{\pi_1(X)\cong G.}$$
::: {.proof}
Van Kampen says that attaching the $2$-cells quotients the free group by the normal closure of the relators, exactly producing the presented group.
:::
:::
