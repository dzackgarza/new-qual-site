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

(a) False. The universal covering $\RR\to S^1$ has a line
as its total space.

(b) False. A connected cover of the torus has fundamental
group isomorphic to a subgroup of $\ZZ^2$, hence abelian.
The fundamental group of the Klein bottle is nonabelian.

(c) True. $F_3$ contains a free subgroup of rank $2$ generated
by two of its free generators. An index-two subgroup of $F_2$
has rank $1+2(2-1)=3$ by the
Nielsen–Schreier rank formula.

(d) True. The Nielsen–Schreier theorem makes every subgroup
free; if its index is $d<\infty$, its rank is
$1+d(n-1)$.

(e) False. The simply connected sphere $S^2$ is its own
universal cover and is not contractible.

:::
