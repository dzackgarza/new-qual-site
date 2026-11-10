---
schema: qual/card@1
id: E-MUN-5-3
kind: problem
title: Containment and nonemptiness of infinite products
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §5 Exercise 3, printed p. 39; the four parts
    are stored as printed, including the parenthetical about changing a function's range
    in (a) and the cross-reference to the exercises of §19 in (c).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.3,
    printed pp. 69-70 (tmp/sources/munkres-solutions-whitman.pdf). His (b) replaces one
    coordinate of a chosen element of B, as the card does; his (d) has A union B
    contained in the product of the unions, with a counterexample to the converse, and
    the intersection equal to the product of the intersections. The card's (d) states
    the same inclusion and equality but does not write his counterexample; the strictness
    it asserts, that coordinates may come from different sides, is his reason. Its
    remark in (c), that for a countable family the converse is the countable axiom of
    choice and is not provable in ZF, is stronger than the manual's "this requires the
    Axiom of Choice" and is true; the book defers the point to the exercises of §19.
---

::: {.exercise}

Let $A = A_{1} \times A_{2} \times \cdots$ and $B = B_{1} \times B_{2} \times \cdots$ .

(a) Show that if $B_{i} \subset A_{i}$ for all $i$, then $B \subset A$ . (Strictly speaking, if we are given a function mapping the index set $\ZZ_{+}$ into the union of the sets $B_{i}$, we must change its range before it can be considered as a function mapping $\ZZ_{+}$ into the union of the sets $A_{i}$ . We shall ignore this technicality when dealing with cartesian products).

(b) Show the converse of (a) holds if $B$ is nonempty.

(c) Show that if $A$ is nonempty, each $A_i$ is nonempty.
Does the converse hold?
(We will return to this question in the exercises of §19.)

(d) What is the relation between the set $A \cup B$ and the cartesian product of the sets $A_i \cup B_i$ ? What is the relation between the set $A \cap B$ and the cartesian product of the sets $A_i \cap B_i$ ?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.3, printed pp. 69--70** (`tmp/sources/munkres-solutions-whitman.pdf`); the four parts below are his, and so is the reading of (c)'s converse as a use of the axiom of choice.

Write
$$
A=\prod_{i\ge1}A_i,
\qquad
B=\prod_{i\ge1}B_i.
$$

(a) If $B_i\subset A_i$ for every $i$ and $x\in B$, then $x_i\in B_i\subset A_i$ for every $i$. Hence $x\in A$, so
$$
B\subset A.
$$

(b) Suppose $B\ne\varnothing$ and $B\subset A$. Fix $i$ and $b\in B_i$. Choose $x=(x_j)\in B$, and form $y$ by replacing only the $i$-th coordinate of $x$ by $b$. Then $y_j\in B_j$ for every $j$, so $y\in B\subset A$. Therefore $b=y_i\in A_i$. Since $b\in B_i$ was arbitrary,
$$
B_i\subset A_i.
$$

(c) If $A\ne\varnothing$, choose $x\in A$. Then $x_i\in A_i$ for every $i$, so every $A_i$ is nonempty.

The converse is a choice statement: from the mere nonemptiness of all $A_i$, producing one element of $\prod_iA_i$ requires choosing one element from each $A_i$. For a countable family this is the countable axiom of choice. Thus the converse holds under the axiom of choice; it is not provable in ZF set theory without some form of choice.

(d) If $x\in A\cup B$, then either $x_i\in A_i$ for all $i$ or $x_i\in B_i$ for all $i$. In either case $x_i\in A_i\cup B_i$ for every $i$, hence
$$
A\cup B\subset\prod_i(A_i\cup B_i).
$$
The inclusion can be strict because the product on the right permits different coordinates to come from different sides.

For intersections,
$$
\begin{aligned}
x\in A\cap B
&\iff x_i\in A_i\text{ and }x_i\in B_i\text{ for every }i\\
&\iff x_i\in A_i\cap B_i\text{ for every }i,
\end{aligned}
$$
so
$$
\boxed{A\cap B=\prod_i(A_i\cap B_i).}
$$
:::
