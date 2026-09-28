---
schema: qual/card@1
id: P-TOPS07A
kind: problem
title: "Fundamental group of a tetrahedron with faces glued in pairs"
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
Consider a solid tetrahedron $ABCD$.
The face $ABC$ is glued to $ABD$ by an affine map preserving the order of vertices (i.e. $A$ goes to $A$, $B$ goes to $B$, $C$ goes to $D$). Similarly, $BCD$ is glued to $ACD$.
Compute the fundamental group of the resulting quotient space.
:::

::: {.solution}
<1>1. Under the first face pairing $ABC\to ABD$, the vertices satisfy $C\sim D$, and under the second pairing $BCD\to ACD$, they satisfy $B\sim A$.
::: {.proof}
The first affine pairing sends $A\mapsto A$, $B\mapsto B$, $C\mapsto D$. The second, preserving the listed order, sends $B\mapsto A$, $C\mapsto C$, $D\mapsto D$.
:::

<1>2. Thus the quotient has two vertex classes, say $v=[A]=[B]$ and $w=[C]=[D]$. The four edges $AC,AD,BC,BD$ form a single edge orbit joining $v$ to $w$, while $AB$ and $CD$ become loops at $v$ and $w$ respectively.
::: {.proof}
The first face pairing identifies $AC$ with $AD$ and $BC$ with $BD$. The second identifies $BC$ with $AC$ and $BD$ with $AD$. Hence all four cross-edges are identified. The edges $AB$ and $CD$ are each mapped to themselves by their respective face pairings.
:::

<1>3. Collapse the cross-edge, which is a maximal tree in the $1$-skeleton. Let $a$ and $c$ denote the loops arising from $AB$ and $CD$. Then the two $2$-cells impose the relations $a=1$ and $c=1$.
::: {.proof}
The boundary of the first face $ABC$ is $AB\cdot BC\cdot CA$. After collapsing the cross-edge, the last two factors cancel, leaving $a$. Similarly, the boundary of $BCD$ is $BC\cdot CD\cdot DB$, whose two cross-edge factors cancel after the collapse, leaving $c$.
:::

<1>4. Therefore
$$
\boxed{\pi_1(X)=1}.
$$
::: {.proof}
The presentation is $\langle a,c\mid a,c\rangle$, the trivial group.
:::
:::
