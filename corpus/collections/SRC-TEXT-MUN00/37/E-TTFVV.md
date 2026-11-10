---
schema: qual/card@1
id: E-TTFVV
kind: problem
title: The countable intersection property characterizes Lindelof spaces
classification:
  areas:
  - topology
  topics:
  - Countability
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof has been checked line by
    line against the book and the search is recorded in the COMPLAINTS.md entry for §37--§42 of
    SRC-TEXT-MUN00. Searched: Aleksey Zinger, "MAT 530" Problem Sets 2-9 (the only problems of Chapter 5
    or 6 among them are Munkres p235 #1, p236 #5, p260 #2 and p260 #7); "Solutions to exercises in
    Munkres", file S38.pdf (Exercise 38.4 onwards); "Solutions to exercises for Mathematics 205A" (UC
    Riverside, Fall 2014), section VI.4 (§38 Exercises 2 and 3); Orellana (whose §37 selection does not
    include this exercise), Doug's World (Chapter 4), Whitman (to §22), "positron0802" (Chapters 2 and 3),
    "shenapse" (§1--§11), "9beach" (§1--§4), "kyp44" (§1--§22); and the dbFin pages, which have no
    chapter-5 or chapter-6 section. Checked against Munkres, Topology (2000), Section 37 Exercise 2,
    printed p. 235, Definition of Lindelof and De Morgan's laws: from a countable subcover of the
    complements of the closures one gets a countable subfamily with empty intersection, and conversely an
    open cover with no countable subcover gives a family of closed sets with the countable intersection
    property and empty intersection. No correction was needed; the proof uses closedness only in the
    converse direction, where the exercise's arbitrary subsets are replaced by their closures.
---

::: {.exercise}

A collection $\mathcal{A}$ of subsets of $X$ has the countable intersection property if every countable intersection of elements of $\mathcal{A}$ is nonempty.
Show that $X$ is a Lindelöf space if and only if for every collection $\mathcal{A}$ of subsets of $X$ having the countable intersection property,

$$
\bigcap_{A \in \mathcal{A}} \overline{A}
$$

is nonempty.
:::

::: {.solution}
Assume first that $X$ is Lindelöf, and let $\mathcal A$ have the countable intersection property. Suppose
$$
\bigcap_{A\in\mathcal A}\overline A=\varnothing.
$$
Then the open sets
$$
X\setminus\overline A,\qquad A\in\mathcal A,
$$
cover $X$. Lindelöfness gives a countable subcover
$$
X=\bigcup_{n=1}^\infty (X\setminus\overline{A_n}).
$$
Taking complements,
$$
\bigcap_{n=1}^\infty\overline{A_n}=\varnothing,
$$
so certainly $\bigcap_{n=1}^\infty A_n=\varnothing$, contradicting the countable intersection property. Hence the intersection of all closures is nonempty.

Conversely, assume the stated closure-intersection property, and let
$$
\mathcal U=\{U_i:i\in I\}
$$
be an open cover of $X$. Suppose no countable subfamily covers $X$. Put
$$
A_i=X\setminus U_i.
$$
For every countable set of indices $i_1,i_2,\dots$, the union $U_{i_1}\cup U_{i_2}\cup\cdots$ is not all of $X$, so
$$
A_{i_1}\cap A_{i_2}\cap\cdots\ne\varnothing.
$$
Thus $\{A_i:i\in I\}$ has the countable intersection property. Each $A_i$ is closed, so the assumed property gives
$$
\varnothing\ne\bigcap_{i\in I}\overline{A_i}
=\bigcap_{i\in I}A_i
=X\setminus\bigcup_{i\in I}U_i,
$$
contradicting that $\mathcal U$ covers $X$. Therefore every open cover has a countable subcover, and $X$ is Lindelöf.
:::
