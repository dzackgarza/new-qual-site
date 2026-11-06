---
schema: qual/card@1
id: P-UCTOP290-S4-16
kind: problem
title: True or false statements about covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 16 against its extraction and PDF page image.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 4, problem 16
    (assets/attachments/UCSD_290_F14_sheet4.pdf, printed page 254), from the
    checked-in extraction and a 300 dpi render. The five printed items agree
    word for word with the card's five items, including the direction of (b),
    "The Klein bottle is a covering space of the torus", which is the false
    direction and is the opposite of the true statement of problem 3 on the same
    sheet. No repair was needed.
---

::: {.problem}
Decide whether each statement is true or false.

(a) Every covering space of $S^1$ is homeomorphic to a disjoint
union of circles.

(b) The Klein bottle covers the torus.

(c) Each of the free groups $F_2$ and $F_3$ has a subgroup
isomorphic to the other.

(d) A finite-index subgroup of $F_n$ is free of finite rank.

(e) The universal cover of every path-connected, locally
path-connected, semilocally simply connected space is
contractible.
:::

::: {.solution}

::: pf

::: {.pf-step #circles}

(a) and (b) are false.

::: pf-proof

(a) The universal cover $\RR\to S^1$, $t\mapsto e^{2\pi it}$, is a covering
space of $S^1$ whose total space is a line, and a line is not homeomorphic to
a disjoint union of circles: it is connected but not compact, while a circle
is compact and a disjoint union of circles with more than one term is
disconnected. (b) A connected cover $p\colon Y\to T^2$ injects $\pi_1(Y)$ into
$\pi_1(T^2)=\ZZ^2$, which is abelian, so $\pi_1(Y)$ is abelian. The Klein
bottle has $\pi_1=\langle u,v\mid vuv^{-1}=u^{-1}\rangle$, which is not
abelian, since $vuv^{-1}u^{-1}=u^{-2}\ne1$ in the infinite dihedral group that
this presentation defines. So the Klein bottle is not a covering space of the
torus. The true statement on the same sheet is the other direction, that the
torus double covers the Klein bottle, whose fundamental group therefore has an
abelian subgroup of index two.

:::

:::

::: {.pf-step #freeness}

(c) and (d) are true.

::: pf-proof

(c) $F_3=\langle x,y,z\rangle$ contains $\langle x,y\rangle\cong F_2$ as the
subgroup of words in two of its free generators. Conversely the two-vertex
graph with $a$-edges $0\to1$ and $1\to0$ and a $b$-loop at each vertex is a
connected two-sheeted covering of $S^1\vee S^1$, so its fundamental group is a
subgroup of index two of $F_2$, free on $1-2+4=3$ generators; with the tree
$0\xrightarrow{a}1$ the basis at $0$ is $a^2$, $b$ and $aba^{-1}$. So $F_2$
has a subgroup isomorphic to $F_3$. (d) Let $H\le F_n$ have finite index $k$.
The cover of the wedge $W_n$ of $n$ circles corresponding to $H$ is connected
with $k$ sheets, so its total space is a connected graph with $k$ vertices and
$kn$ edges, one edge of each label over each vertex; its fundamental group is
free of rank $1-k+kn=1+k(n-1)$, a finite number, and equals $H$. So $H$ is
free of finite rank.

:::

:::

::: {.pf-step #contractible}

(e) is false.

::: pf-proof

$S^2$ is path-connected, locally path-connected and semilocally simply
connected, being a manifold, and it is simply connected, so it is its own
universal cover; its identity cover is the universal cover of $S^2$. But $S^2$
is not contractible: $H_2(S^2;\ZZ)=\ZZ$, while a contractible space has
vanishing reduced homology in every degree. So a simply connected space can be
its own universal cover without that cover being contractible.

:::

:::

:::


:::
