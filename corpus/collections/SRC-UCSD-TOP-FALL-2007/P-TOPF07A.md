---
schema: qual/card@1
id: P-TOPF07A
kind: problem
title: "Fundamental group of a quotient space from identifying four faces of a cube"
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
Consider a solid cube.
Four of the faces are identified together by means of rigid rotations, as pictured below.
(For example, the face $ABCD$ is identified with $BFGC$ via an affine map preserving the order of vertices.)
Compute the fundamental group of the resulting quotient space.
:::

::: {.solution}
<1>1. Under the four side-face rotations in the source diagram, the four top vertices become one vertex $T$, the four bottom vertices become one vertex $B$, the four vertical edges become one edge $v:T\to B$, the four top edges become one loop $a$ at $T$, and the four bottom edges become one loop $b$ at $B$.
::: {.proof}
The specified identification $ABCD\to BFGC$ preserving vertex order is the quarter-turn carrying one side face to the next; iterating it identifies all four side faces and their corresponding boundary cells.
:::

<1>2. The top and bottom square faces give relations $a^4=1$ and $b^4=1$, while a side face gives
$$a v b^{-1}v^{-1}=1.$$
::: {.proof}
Each top (respectively bottom) boundary traverses the single quotient horizontal edge four times. A representative side square has boundary top edge, vertical edge, reversed bottom edge, reversed vertical edge.
:::

<1>3. Therefore
$$\pi_1(X)\cong\langle a,b,v\mid a^4,b^4,avb^{-1}v^{-1}\rangle.$$
::: {.proof}
The cube interior is a $3$-cell and does not affect the fundamental group.
:::

<1>4. The side relation gives $b=v^{-1}av$, so the relation $b^4=1$ follows from $a^4=1$. Hence
$$\boxed{\pi_1(X)\cong\langle a,v\mid a^4=1\rangle\cong (\mathbb Z/4)*\mathbb Z.}$$
::: {.proof}
Eliminate $b$ by a Tietze transformation.
:::
:::
