---
schema: qual/card@1
id: E-MJQTF
kind: problem
title: Interior and boundary of a connected set
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 11, printed p. 158; the stored
    statement is the printed two questions.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.11, PDF p. 6. Two tangent discs give a
    connected set whose interior is disconnected, the open interval gives a connected set
    with a two-point boundary, and the rationals give the failure of the converse.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

If $A$ is a connected subspace of $X$, does it follow that $\operatorname{Int} A$ and $\operatorname{Bd} A$ are connected?
Does the converse hold?
Justify your answers.
:::

::: {.solution}

The two counterexamples are those of **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.11, PDF p. 6 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the statement was checked against Munkres, *Topology* (2000), §24 Exercise 11, printed p. 158, with the definition of connectedness on printed p. 148, Theorem 23.3 on printed p. 150, and Theorem 24.1 on printed p. 153. Interior and boundary are taken in the ambient space.

::: pf

::: {.pf-step #interior-fails}
A connected subspace of $\RR^{2}$ whose interior is not connected.

:::: pf-proof

::: {.pf-step #two-discs-connected}
Let $D_{0}$ be the closed unit disc about the origin and $D_{2}$ the closed unit disc about $2\times0$, and put $A\coloneqq D_{0}\cup D_{2}$. Then $A$ is connected.

::: pf-proof
Each closed disc is path connected by straight-line paths and hence connected (printed p. 155), and $(1,0)\in D_{0}\cap D_{2}$; a union of connected subspaces with a common point is connected by Theorem 23.3 (printed p. 150).
:::

:::

::: {.pf-step #interior-separation}
$\operatorname{Int}A$ is the union of the open discs of radius $1$ about $0$ and about $2\times0$, which are disjoint and nonempty.

::: pf-proof
A point interior to $A$ has a ball about it inside $D_{0}\cup D_{2}$; a ball contained in the union of the two closed discs and meeting both must contain points outside both discs (the discs meet only in the single point $1\times0$), so such a ball lies in one of the discs. Hence $\operatorname{Int}A$ is the union of the two interiors, and the open discs are disjoint because their centres are $2$ apart and their radii are $1$.
:::

:::

::: {.pf-step #interior-not-connected}
$\operatorname{Int}A$ is not connected.

::: pf-proof
The two open discs are nonempty, disjoint, and open in $\RR^{2}$, hence open in the subspace $\operatorname{Int}A$, and their union is $\operatorname{Int}A$ by step [](#interior-separation){.pf-ref}; so they form a separation of $\operatorname{Int}A$.
:::

:::

::::

:::

::: {.pf-step #boundary-fails}
A connected subspace of $\RR$ whose boundary is not connected.

::: pf-proof
Let $A\coloneqq(0,1)\subset\RR$, which is connected by Theorem 24.1 (printed p. 153). Its closure is $[0,1]$ and the closure of its complement is $(-\infty,0]\cup[1,\infty)$, so $\operatorname{Bd}A=\theset{0,1}$ by the definition of the boundary (§17, printed p. 101). In the subspace $\theset{0,1}$ each of the one-point sets $\theset{0}$ and $\theset{1}$ is nonempty and open, and they are disjoint with union $\operatorname{Bd}A$, a separation.
:::

:::

::: {.pf-step #converse-fails}
There is a subspace $A$ with $\operatorname{Int}A$ and $\operatorname{Bd}A$ both connected and $A$ itself not connected.

:::: pf-proof

::: {.pf-step #rationals}
For $A\coloneqq\QQ\subset\RR$ one has $\operatorname{Int}\QQ=\varnothing$ and $\operatorname{Bd}\QQ=\RR$.

::: pf-proof
No interval of positive length is contained in $\QQ$, since every such interval contains an irrational; hence $\operatorname{Int}\QQ=\varnothing$. Both $\QQ$ and its complement are dense in $\RR$, so both closures are $\RR$ and $\operatorname{Bd}\QQ=\RR$ by the definition of the boundary.
:::

:::

::: {.pf-step #rationals-judgement}
$\operatorname{Int}\QQ$ and $\operatorname{Bd}\QQ$ are connected while $\QQ$ is not.

::: pf-proof
$\operatorname{Bd}\QQ=\RR$ is connected by Theorem 24.1 (printed p. 153). The empty space is connected: a separation is a pair of disjoint nonempty open sets with union the space (§23, printed p. 148), and no nonempty set has union $\varnothing$. The space $\QQ$ is not connected: choosing rationals $p<q$ and an irrational $a$ with $p<a<q$, the sets $\QQ\cap(-\infty,a)$ and $\QQ\cap(a,\infty)$ are nonempty, disjoint, open in $\QQ$, and cover $\QQ$, which is the argument of Example 4 on printed p. 149.
:::

:::

::::

:::

::: pf-step
Both questions have a negative answer.

::: pf-proof
Step [](#interior-fails){.pf-ref} gives a connected set with disconnected interior, step [](#boundary-fails){.pf-ref} a connected set with disconnected boundary, so connectedness of $A$ implies neither. Step [](#converse-fails){.pf-ref} gives a set whose interior and boundary are connected while the set is not, so the converse fails as well.
:::

:::

:::

:::
