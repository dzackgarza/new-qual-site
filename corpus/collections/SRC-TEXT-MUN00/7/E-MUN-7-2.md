---
schema: qual/card@1
id: E-MUN-7-2
kind: problem
title: Bijections in the countability proofs for $\QQ$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 2; the stored statement matches.
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
    Read against Munkres, Topology (2000), §7 Exercise 2 and Examples 1 and 2 of §7,
    printed pp. 44-46; the card states the book's two formulas, f(n) = 2n for n > 0 and
    -2n+1 for n <= 0, and f(x,y) = (x+y-1,y) into A = {y <= x} composed with
    g(x,y) = x(x-1)/2 + y, exactly as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.2,
    printed pp. 81-84 (tmp/sources/munkres-solutions-whitman.pdf). He checks each of the
    three maps separately; the card writes the explicit inverses f^{-1} and F^{-1} and
    the consecutive-block count for g, which is his argument that the blocks
    x(x-1)/2 + 1, ..., x(x+1)/2 partition Z_+. No defect found.
---

::: {.exercise}

Show that the maps $f$ and $g$ of Examples 1 and 2 are bijections.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.2, printed pp. 81--84** (`tmp/sources/munkres-solutions-whitman.pdf`); the three maps checked are the book's Examples 1 and 2, and the inverse formulas and the block count for $g$ are his argument written out.

For Example 1, the map $f:\ZZ\to\ZZ_+$ is
$$
f(n)=
\begin{cases}
2n,&n>0,\\
-2n+1,&n\le0.
\end{cases}
$$
Positive integers go to the positive even integers, while nonpositive integers go to the positive odd integers. These two image sets are disjoint and together exhaust $\ZZ_+$. Explicitly,
$$
f^{-1}(m)=
\begin{cases}
m/2,&m\text{ even},\\
(1-m)/2,&m\text{ odd}.
\end{cases}
$$
Thus $f$ is bijective.

For Example 2, let
$$
A=\{(x,y)\in\ZZ_+^2:y\le x\}.
$$
The first map is
$$
F:\ZZ_+^2\to A,
\qquad
F(x,y)=(x+y-1,y).
$$
Since $x\ge1$, the first coordinate is at least $y$, so $F$ maps into $A$. Its inverse is
$$
F^{-1}(u,v)=(u-v+1,v),
$$
which is well-defined because $u\ge v$. Hence $F$ is bijective.

The second map is
$$
G:A\to\ZZ_+,
\qquad
G(x,y)=\frac{x(x-1)}2+y.
$$
For fixed $x$, as $y$ runs from $1$ to $x$, the values of $G$ are precisely
$$
\frac{x(x-1)}2+1,\ldots,\frac{x(x+1)}2.
$$
These consecutive blocks are pairwise disjoint and concatenate to
$$
1,2,3,\ldots.
$$
Thus every positive integer occurs exactly once, so $G$ is bijective.
:::
