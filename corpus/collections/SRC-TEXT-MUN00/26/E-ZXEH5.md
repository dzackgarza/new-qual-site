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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with four steps, one per stage of the proof, each carrying a `pf-proof`; the statement and
    the attribution are unchanged. One step is corrected: the prose's second stage took the
    intersection of the $U_a$ and the union of the $V_a$, which does not give $A\subseteq U_b$,
    since $U_a$ contains only its own $a$; step 2 takes the union of the $U_a$ and the
    intersection of the $V_a$, and the final stage then takes the intersection of the $U_b$ and
    the union of the $V_b$ as the prose did. Cited by number only: compactness of a slice and
    of a continuous image, and the definition of the product basis.
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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.9** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $A\subset X$, $B\subset Y$ be compact with $N\supset A\times B$ open in $X\times Y$. It is to be shown that there are open sets $U\supset A$ in $X$ and $V\supset B$ in $Y$ with $U\times V\subset N$.

::: pf

::: pf-step

For each $a\in A$ there are open sets $U_a\ni a$ and $V_a\supset B$ with $U_a\times V_a\subset N$.

::: pf-proof

The slice $\{a\}\times B$ is homeomorphic to the compact space $B$, hence compact. Each of its points $(a,b)$ lies in some basis element $W\times Z$ of $X\times Y$ with $a\in W$, $b\in Z$ and $W\times Z\subseteq N$, since $N$ is open. Finitely many of these, $W_1\times Z_1,\dots,W_n\times Z_n$, cover $\{a\}\times B$. Put $U_a=\bigcap_{i\le n}W_i$ and $V_a=\bigcup_{i\le n}Z_i$: both are open, $a\in U_a$ because $a\in W_i$ for every $i$, and $B\subseteq V_a$ because each $(a,b)$ lies in some $W_i\times Z_i$ and then $b\in Z_i$. If $x\in U_a$ and $y\in V_a$, then $y\in Z_i$ for some $i$ and $x\in W_i$, so $x\times y\in W_i\times Z_i\subseteq N$; hence $U_a\times V_a\subseteq N$.

:::

:::

::: pf-step

For each $b\in B$ there are open sets $U_b\supset A$ and $V_b\ni b$ with $U_b\times V_b\subset N$.

::: pf-proof

The family $\{U_a:a\in A\}$ covers $A$, and $A$ is compact, so finitely many $U_{a_1},\dots,U_{a_k}$ cover $A$. Put $U_b=\bigcup_{j\le k}U_{a_j}$ and $V_b=\bigcap_{j\le k}V_{a_j}$: both are open, $A\subseteq U_b$ by the choice of the finitely many indices, and $b\in V_b$ because $b\in B\subseteq V_{a_j}$ for every $j$. If $x\in U_b$ and $y\in V_b$, then $x\in U_{a_j}$ for some $j$ and $y\in V_{a_j}$ for that same $j$, so $x\times y\in U_{a_j}\times V_{a_j}\subseteq N$; hence $U_b\times V_b\subseteq N$. (The union is taken of the $U$'s and the intersection of the $V$'s: each $U_a$ contains only its own $a$, so an intersection of them would not contain $A$.)

:::

:::

::: pf-step

The sets $V_b$ cover $B$, so finitely many $V_{b_1},\dots,V_{b_m}$ cover $B$; then
$$
U=\bigcap_{j\le m}U_{b_j},\qquad V=\bigcup_{j\le m}V_{b_j}
$$
are open, contain $A$ and $B$ respectively, and satisfy $U\times V\subset N$.

::: pf-proof

Each $b$ lies in $V_b$ by step 2, and $B$ is compact, so finitely many of them cover $B$. $U$ is open and contains $A$ because every $U_{b_j}$ does, and $V$ is open and contains $B$ by the choice of the $b_j$. If $x\in U$ and $y\in V$, then $x\in U_{b_j}$ for every $j$ and $y\in V_{b_j}$ for some $j$, so $x\times y\in U_{b_j}\times V_{b_j}\subseteq N$.

:::

:::

::: pf-step

Thus $A\times B\subset U\times V\subset N$ with $U$, $V$ open, which is the theorem.

::: pf-proof

A point of $A\times B$ has its two coordinates in $A\subseteq U$ and $B\subseteq V$; the inclusion $U\times V\subseteq N$ is step 3.

:::

:::

:::
:::
