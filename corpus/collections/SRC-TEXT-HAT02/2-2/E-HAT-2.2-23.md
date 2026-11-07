---
schema: qual/card@1
id: E-HAT-2.2-23
kind: problem
title: If $M_g$ covers $M_h$ then $g = n(h-1)+1$
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 23; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the computation: $\chi(M_g)=2-2g$, multiplicativity under an $n$-sheeted covering gives
    $2-2g=n(2-2h)$, and dividing by $-2$ gives $g=n(h-1)+1$ with $n$ the number of sheets.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 23 as printed on p. 157, bracketed converse included. The
    argument is correct; chi(M_g) = 2-2g is now cited as the cell count of the standard structure
    of Example 2.36 p. 141 read through the definition of chi on p. 146, the multiplicativity is
    Exercise 22 p. 157, and the converse is explicitly marked as quoted from Example 1.41 p. 73
    rather than proved. What is not covered: the converse construction, and no certificate.
---

::: {.problem}
Show that if the closed orientable surface $M_g$ of genus $g$ is a covering space of $M_h$, then $g = n(h-1)+1$ for some $n$, namely, $n$ is the number of sheets in the covering.
[Conversely, if $g = n(h-1)+1$ then there is an $n$ sheeted covering $M_g \to M_h$, as we saw in Example 1.41.]
:::

::: {.solution}
For a closed orientable surface $M_g$ of genus $g$,
$$
\chi(M_g)=2-2g.
$$
This is the cell count of the standard CW structure of $M_g$ given in Example 2.36 (p. 141), one $0$-cell, $2g$ $1$-cells and one $2$-cell, read through the definition of $\chi$ as the alternating sum of numbers of cells (p. 146).
Suppose
$$
p:M_g\to M_h
$$
is an $n$-sheeted covering. By Exercise 22 (p. 157),
$$
\chi(M_g)=n\chi(M_h).
$$
Hence
$$
2-2g=n(2-2h).
$$
Dividing by $-2$ gives
$$
g-1=n(h-1),
$$
so
$$
\boxed{g=n(h-1)+1}.
$$
The integer $n$ is exactly the number of sheets of the covering. The bracketed converse in the printed statement is not part of what is proved here: it is the construction of Example 1.41 (p. 73), where a free action of a cyclic group of order $n$ on $M_{n(h-1)+1}$ gives the $n$-sheeted covering, and it is quoted from the book rather than re-proved.
:::
