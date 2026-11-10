---
schema: qual/card@1
id: E-ZXEH5
kind: problem
title: Generalized tube lemma for compact rectangles
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 9, printed p. 171, with the tube
    lemma; the stored statement is the printed generalization.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.9, PDF p. 13. Finitely many basis elements
    cover each slice a x B and yield U_a x V_a inside N; finitely many of these cover a
    fixed slice A x {b}, and finitely many of those cover B, giving the two open sets.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Generalize the tube lemma as follows.

Theorem.
Let $A$ and $B$ be subspaces of $X$ and $Y$, respectively; let $N$ be an open set in $X \times Y$ containing $A \times B$.
If $A$ and $B$ are compact, then there exist open sets $U$ and $V$ in $X$ and $Y$, respectively, such that

$$
A \times B \subset U \times V \subset N.
$$
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.9, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

**Theorem.** Let $A\subset X$, $B\subset Y$ be compact with $N\supset A\times B$ open in $X\times Y$. Then there are open sets $U\supset A$ in $X$ and $V\supset B$ in $Y$ with $U\times V\subset N$.

*Proof.* Fix $a\in A$ and cover the compact slice $a\times B$ by finitely many basis elements $W_{i}\times Z_{i}\subset N$ meeting it ($i\le n$). Then
$$
U_{a}=\bigcap_{i\le n}W_{i},\qquad V_{a}=\bigcup_{i\le n}Z_{i}
$$
satisfy $a\in U_{a}$, $B\subset V_{a}$ and $U_{a}\times V_{a}\subset N$: for $x\times y\in U_{a}\times V_{a}$ there is $i$ with $y\in Z_{i}$, hence $x\times y\in W_{i}\times Z_{i}\subset N$.

The $U_{a}\times V_{a}$ cover $A\times B$ as $a$ varies, and for each $a$ the slice $A\times\{b\}$... precisely, fix $b\in B$: the sets $U_{a}\times V_{a}$ with $b\in V_{a}$ cover the compact $A\times\{b\}$, so finitely many of them do; their $U_{a}$'s intersect to an open set $U_{b}\ni A$ and their $V_{a}$'s union to an open set $V_{b}\ni b$, with $U_{b}\times V_{b}\subset N$. The $V_{b}$ cover the compact $B$, so finitely many $V_{b_{1}},\dots,V_{b_{m}}$ cover $B$; then $U=U_{b_{1}}\cap\cdots\cap U_{b_{m}}$ and $V=V_{b_{1}}\cup\cdots\cup V_{b_{m}}$ are open, contain $A$ and $B$, and $U\times V\subset N$. $\square$
:::
