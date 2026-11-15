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
  date: 2026-11-15
  note: >-
    Munkres §83 Exercise 1, printed p. 505. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-4911475-E-NKQPS.md, read whole.
    Math StackExchange 4911475 quotes this exercise and asks why the hypothesis is without loss of generality;
    the accepted answer 4911528 by Paul Frost (2024-05-05) answers it: add the remaining vertices to B, a
    closed set by the result on printed p. 502. That is transcribed on the card with its URL. The answer does
    not say why the proof needs the hypothesis, i.e. what fails at a vertex in neither B nor C; the card's own
    proof does, and it is kept.
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

The question of this exercise is answered by Paul Frost, answer 4911528 (https://math.stackexchange.com/a/4911528), posted 2024-05-05 to Math Stack Exchange question 4911475, "Every linear graph $X$ is normal" (https://math.stackexchange.com/questions/4911475, asked by Davood Karimi on the same day): let $V$ be the set of vertices belonging to neither $B$ nor $C$; by the result on printed p. 502 a union of vertices and edges is closed in a linear graph, so $V$ is closed, $B'=B\cup V$ is a closed set disjoint from $C$, and every vertex lies in $B'$ or in $C$. That is why the assumption costs nothing. What the answer does not do is show where the assumption is used: the printed proof's argument that $U$ and $V$ are disjoint fails at a vertex in neither $B$ nor $C$, since such a vertex may lie in some $U_\alpha$ and some $V_\beta$ with $\alpha\ne\beta$. The card's own proof below makes that point.


Let $X^0$ be the set of vertices of the linear graph $X$. As proved just before Lemma 83.1 (printed p. 502), $X^0$ is a closed discrete subspace of $X$, and in fact every subset of $X^0$ is closed in $X$, since its intersection with each edge is empty or a one-point set.

Given the disjoint closed sets $B,C$ of the printed proof of Lemma 83.1 (printed p. 502), let
$$
D=X^0-(B\cup C).
$$
Then $D$ is closed, because every subset of $X^0$ is closed in $X$; so $B'=B\cup D$ is closed, and $B'\cap C=\varnothing$ because $D\cap C=\varnothing$ and $B\cap C=\varnothing$. Replacing $B$ by $B'$ therefore leaves a pair of disjoint closed sets, whose union contains every vertex of $X$. Separating $B'$ and $C$ separates $B$ and $C$, so it is enough to prove the lemma under the extra assumption.

This extra condition is used twice in the printed proof. First, when open sets $U_\alpha\subseteq A_\alpha$ and $V_\beta\subseteq A_\beta$ for distinct edges are seen to be disjoint: a point of $U_\alpha\cap V_\beta$ lies on both arcs, hence is a vertex, and a vertex of $B$ lies in no $V_\beta$ while a vertex of $C$ lies in no $U_\alpha$. Second, when the unions $U=\bigcup U_\alpha$ and $V=\bigcup V_\beta$ are shown to be open through the coherent topology: a point of $U\cap A_\alpha$ outside $U_\alpha$ lies on another arc as well, hence is a vertex, and a vertex of $B$ lies in $U_\alpha$ by the definition of $U_\alpha$ while a vertex of $C$ cannot lie in $U$. Without the assumption those vertices outside $B\cup C$ would be unaccounted for, since the sets $U_\alpha$ are chosen only to contain $B\cap A_\alpha$.

:::
