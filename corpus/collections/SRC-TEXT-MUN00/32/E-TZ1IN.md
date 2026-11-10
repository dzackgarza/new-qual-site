---
schema: qual/card@1
id: E-TZ1IN
kind: problem
title: Complete normality characterized by separated sets
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), the second item printed there
    under the heading "Problem 32.6", printed pp. 6-7
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 32 Exercise 6, printed p. 205, Theorem 17.2 (closed sets in subspaces) and the printed
    hint. What was corrected: the source calls the ambient set S = X - (closure A cap closure B)
    and then asserts "the sets A' = A cap S and B' = B cap S are closed in S" and "Then V_A and V_B
    are open in X because S is open", which needs the two facts the card supplies: A is contained
    in closure A, hence in S by separatedness, so A' = S cap closure A is the trace of a closed set
    of X, and likewise for B. The converse direction is the source's.
---

::: {.exercise}

A space $X$ is said to be completely normal if every subspace of $X$ is normal.
Show that $X$ is completely normal if and only if for every pair $A, B$ of separated sets in $X$ (that is, sets such that $\overline{A} \cap B = \varnothing$ and $A \cap \overline{B} = \varnothing$), there exist disjoint open sets containing them.
[Hint: If $X$ is completely normal, consider $X - (\overline{A} \cap \overline{B})$.]
:::

::: {.solution}
Suppose first that $X$ is completely normal, and let $A,B\subset X$ be separated:
$$
\overline A\cap B=\varnothing,
\qquad
A\cap\overline B=\varnothing.
$$
Set
$$
Y=X\setminus(\overline A\cap\overline B).
$$
The subspace $Y$ is normal. In $Y$, the sets
$$
A'=\overline A\cap Y,
\qquad
B'=\overline B\cap Y
$$
are closed and disjoint, because their intersection is
$$
(\overline A\cap\overline B)\cap Y=\varnothing.
$$
Also $A\subset A'$ and $B\subset B'$ by separatedness. Normality of $Y$ gives disjoint sets $U',V'$ open in $Y$ with $A'\subset U'$ and $B'\subset V'$. Since $Y$ is open in $X$, the sets $U',V'$ are open in $X$ as well, and they are disjoint neighborhoods of $A$ and $B$.

Conversely, suppose every pair of separated subsets of $X$ has disjoint open neighborhoods. Let $Y\subset X$, and let $A,B\subset Y$ be disjoint closed subsets of $Y$. Since $A$ is closed in $Y$,
$$
Y\cap\overline_X A=A,
$$
so $B\cap\overline_X A=\varnothing$. Similarly $A\cap\overline_X B=\varnothing$. Thus $A$ and $B$ are separated in $X$. By hypothesis there are disjoint open sets $U,V\subset X$ with $A\subset U$, $B\subset V$. Then $U\cap Y$ and $V\cap Y$ are disjoint open neighborhoods of $A,B$ in $Y$. Hence every subspace $Y$ is normal, so $X$ is completely normal.
:::
