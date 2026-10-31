---
schema: qual/card@1
id: P-UCTOP290-S4-11
kind: problem
title: Rank of a cyclic-kernel subgroup of a free group
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
  note: Read sheet 4, Problem 11 against its extraction and PDF page image.
---

::: {.problem}
Let $F_2=\langle a,b\rangle$, and let
$\theta:F_2\to\ZZ/3$ send both $a$ and $b$ to $1$.
Construct the cover of $S^1\vee S^1$ corresponding to
$H=\ker\theta$ and show that $H$ is free of rank $4$.
If $\ZZ/3$ is replaced by $\ZZ/n$, what is the rank?
:::

::: {.solution}

For $n\ge1$, label the vertices of a covering graph by
$i\in\ZZ/n$. At each vertex put one directed $a$-edge and one
directed $b$-edge, both from $i$ to $i+1$.
This is a connected $n$-sheeted cover of $S^1\vee S^1$.
Following a word changes the vertex by its total exponent sum
modulo $n$, so the subgroup at vertex $0$ is exactly
$$
\ker(F_2\to\ZZ/n,\quad a,b\mapsto1).
$$
The graph has $n$ vertices and $2n$ edges. A spanning tree
therefore leaves $2n-(n-1)=n+1$ edges, which freely generate its
fundamental group. Thus
$$
\operatorname{rank}H=n+1.
$$
For $n=3$, the rank is $4$. The three-sheet graph and one explicit
free basis also appear in
[[P-UCTOP290-S4-7|sheet 4, Problem 7]].

:::
