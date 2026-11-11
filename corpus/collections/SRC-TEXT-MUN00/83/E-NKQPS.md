---
schema: qual/card@1
id: E-NKQPS
kind: problem
title: The vertex assumption in the normality proof for linear graphs
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 83 Exercise 1, printed p. 505. Why the proof of normality of a linear graph may assume every vertex lies in B or C: vertices can be adjoined to the closed sets. Checked against the printed proof in Section 83. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Citations added: the paragraph before Lemma 83.1 (printed p. 502), which proves that $X^0$ is a closed discrete subspace and that every subset of $X^0$ is closed in $X$, and the two steps of the printed proof of Lemma 83.1 (printed p. 502) in which the assumption is used. Corrected: the proof did not say why the substituted set $B\cup D$ is still disjoint from $C$ nor that its closedness is what the substitution needs; both are now stated. What the certificate does not cover: Lemma 83.1 itself is the book's, and only the reduction in its first line is discussed here.
---

::: {.exercise}

In the proof of normality of a linear graph $X$, why did we assume that every vertex of $X$ belongs either to $B$ or to $C$?

:::

::: {.solution}

Let $X^0$ be the set of vertices of the linear graph $X$. As proved just before Lemma 83.1 (printed p. 502), $X^0$ is a closed discrete subspace of $X$, and in fact every subset of $X^0$ is closed in $X$, since its intersection with each edge is empty or a one-point set.

Given the disjoint closed sets $B,C$ of the printed proof of Lemma 83.1 (printed p. 502), let
$$
D=X^0-(B\cup C).
$$
Then $D$ is closed, because every subset of $X^0$ is closed in $X$; so $B'=B\cup D$ is closed, and $B'\cap C=\varnothing$ because $D\cap C=\varnothing$ and $B\cap C=\varnothing$. Replacing $B$ by $B'$ therefore leaves a pair of disjoint closed sets, whose union contains every vertex of $X$. Separating $B'$ and $C$ separates $B$ and $C$, so it is enough to prove the lemma under the extra assumption.

This extra condition is used twice in the printed proof. First, when open sets $U_\alpha\subseteq A_\alpha$ and $V_\beta\subseteq A_\beta$ for distinct edges are seen to be disjoint: a point of $U_\alpha\cap V_\beta$ lies on both arcs, hence is a vertex, and a vertex of $B$ lies in no $V_\beta$ while a vertex of $C$ lies in no $U_\alpha$. Second, when the unions $U=\bigcup U_\alpha$ and $V=\bigcup V_\beta$ are shown to be open through the coherent topology: a point of $U\cap A_\alpha$ outside $U_\alpha$ lies on another arc as well, hence is a vertex, and a vertex of $B$ lies in $U_\alpha$ by the definition of $U_\alpha$ while a vertex of $C$ cannot lie in $U$. Without the assumption those vertices outside $B\cup C$ would be unaccounted for, since the sets $U_\alpha$ are chosen only to contain $B\cap A_\alpha$.

:::
