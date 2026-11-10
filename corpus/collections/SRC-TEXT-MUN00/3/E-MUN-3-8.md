---
schema: qual/card@1
id: E-MUN-3-8
kind: problem
title: Ordering the real line by absolute value
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Example 7 and Exercise 8, printed p. 29.
    Example 7 defines xCy iff x^2 < y^2, or x^2 = y^2 and x < y, and says "you can check
    that this is an order relation"; Exercise 8 asks for that check. The stored
    statement matches, and the definition is stated on the card so that the exercise
    stands alone.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.8,
    printed p. 27 (tmp/sources/munkres-solutions-whitman.pdf). His three checks are the
    ones below; the remark that the order differs from the usual one, with -2 and 1 as
    witnesses, is his.
---

::: {.exercise}

Check that the relation defined in Example 7 is an order relation; that is, define $xCy$ if $x^2 < y^2$, or if $x^2 = y^2$ and $x < y$, and show that $C$ is an order relation on the real line.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.8, printed p. 27** (`tmp/sources/munkres-solutions-whitman.pdf`); the three checks and the closing comparison with the usual order are his.

*Comparability.* Let $x\ne y$. If $x^2\ne y^2$ then one of $x^2<y^2$, $y^2<x^2$ holds and $xCy$ or $yCx$. If $x^2=y^2$ then $y=-x$ because $x\ne y$, and $x\ne0$; if $x>0$ then $y=-x<0<x$, and if $x<0$ then $x<0<-x=y$. In either case $x<y$ or $y<x$, so $xCy$ or $yCx$.

*Nonreflexivity.* For every $x$, $x^2=x^2$ and $x<x$ fails, so not $xCx$.

*Transitivity.* Suppose $xCy$ and $yCz$. If $x^2<y^2$: then either $y^2<z^2$, giving $x^2<z^2$, or $y^2=z^2$ with $y<z$, giving $x^2<z^2$; in both cases $xCz$. If $x^2=y^2$ with $x<y$: then $y^2<z^2$ gives $x^2<z^2$, and $y^2=z^2$ with $y<z$ gives $x^2=z^2$ with $x<y<z$; in both cases $xCz$.

So $C$ is an order relation. It differs from the usual order: $-2<1$, but $1^2<(-2)^2$, so $1C(-2)$.
:::
