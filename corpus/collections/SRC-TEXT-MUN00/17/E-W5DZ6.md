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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as the two inclusions and the resulting equality. Both were re-checked against the basis of the product topology (printed p. 86). No statement change.
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

Let $A\subset X$ and $B\subset Y$; a basis element of $X\times Y$ is a product $U\times V$ of an open $U\subset X$ and an open $V\subset Y$.

::: pf

::: {.pf-step #inside}

$\overline{A\times B}\subset\overline{A}\times\overline{B}$.

::: pf-proof

Let $(x,y)\in\overline{A\times B}$. Let $U\ni x$ and $V\ni y$ be open in $X$ and $Y$. The set $U\times V$ is a basis element of $X\times Y$ containing $(x,y)$, so it meets $A\times B$: there are $w\in A$ and $z\in B$ with $(w,z)\in U\times V$. Then $w\in U\cap A$ and $z\in V\cap B$, so $U$ meets $A$ and $V$ meets $B$; as $U$ and $V$ were arbitrary, $x\in\overline{A}$ and $y\in\overline{B}$.

:::

:::

::: {.pf-step #outside}

$\overline{A}\times\overline{B}\subset\overline{A\times B}$.

::: pf-proof

Let $x\in\overline{A}$ and $y\in\overline{B}$, and let $U\times V$ be a basis element of $X\times Y$ containing $(x,y)$, with $U$ and $V$ open. Since $x\in\overline{A}$ there is $w\in U\cap A$, and since $y\in\overline{B}$ there is $z\in V\cap B$; then $(w,z)\in(U\times V)\cap(A\times B)$. So every basis element containing $(x,y)$ meets $A\times B$, and $(x,y)\in\overline{A\times B}$.

:::

:::

::: pf-step

$\overline{A\times B}=\overline{A}\times\overline{B}$.

::: pf-proof

The two inclusions are steps [](#inside){.pf-ref} and [](#outside){.pf-ref}.

:::

:::

:::
:::
