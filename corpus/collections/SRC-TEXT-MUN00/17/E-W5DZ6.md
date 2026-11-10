---
schema: qual/card@1
id: E-W5DZ6
kind: problem
title: Closure of a product equals the product of closures
classification:
  areas:
  - topology
  topics:
  - Closure
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 9, printed p. 101, with Theorem 17.5
    and the product topology of §15; the stored statement is the printed equation.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.9, printed p. 164.
    Both inclusions are his and are proved with product basis elements, which is what the
    product topology requires in place of neighbourhood bases. (tmp/sources/munkres-
    solutions-whitman.pdf).
---

::: {.exercise}

Let $A \subset X$ and $B \subset Y$.
Show that in the space $X \times Y$,

$$
\overline{A \times B} = \overline{A} \times \overline{B}.
$$
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.9, printed p. 164** (`tmp/sources/munkres-solutions-whitman.pdf`); both inclusions are his.

*$\overline{A\times B}\subset\overline{A}\times\overline{B}$.* Let $(x,y)\in\overline{A\times B}$ and let $U$, $V$ be open in $X$, $Y$ with $x\in U$, $y\in V$. The set $U\times V$ is a basis element of $X\times Y$ containing $(x,y)$, so it meets $A\times B$: there are $w\in A$, $z\in B$ with $(w,z)\in U\times V$. Then $w\in U\cap A$ and $z\in V\cap B$; as $U$ and $V$ were arbitrary, $x\in\overline{A}$ and $y\in\overline{B}$.

*$\overline{A}\times\overline{B}\subset\overline{A\times B}$.* Let $x\in\overline{A}$, $y\in\overline{B}$, and let $U\times V$ be a basis element of $X\times Y$ containing $(x,y)$, with $U$ open in $X$ and $V$ open in $Y$. Since $x\in\overline{A}$, there is $w\in U\cap A$, and since $y\in\overline{B}$, there is $z\in V\cap B$. Then $(w,z)\in(U\times V)\cap(A\times B)$, so every basis element at $(x,y)$ meets $A\times B$ and $(x,y)\in\overline{A\times B}$.
:::
