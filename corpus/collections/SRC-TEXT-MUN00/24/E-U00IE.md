---
schema: qual/card@1
id: E-U00IE
kind: problem
title: Well-ordered sets times the half-open interval are linear continua
classification:
  areas:
  - topology
  topics:
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 6, printed p. 158; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.6, PDF p. 5. Density by the midpoint in the
    second coordinate, and the least upper bound property through the greatest lower bound
    property: the least first coordinate of a set bounded below exists by well-ordering, and
    the fibre over it has a greatest lower bound in [0,1). (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

Show that if $X$ is a well-ordered set, then $X \times [0, 1)$ in the dictionary order is a linear continuum.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.6, PDF p. 5** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs, with the greatest lower bound property used as they use it.

Let $X$ be well ordered and consider $X\times[0,1)$ in the dictionary order.

*Density.* If $x\times y<z\times w$: when $x=z$ take $x\times(y+w)/2$; when $x<z$ take $x\times(y+1)/2$, which satisfies $x\times y<x\times(y+1)/2<z\times w$ because its first coordinate is $x<z$.

*Least upper bound property.* It is equivalent, in a simply ordered set, to the greatest lower bound property, which we verify: let $S\ne\varnothing$ be bounded below and put $\pi_{1},\pi_{2}$ the projections. Since $X$ is well ordered, $\pi_{1}(S)$ has a least element $x_{0}$; then the set of second coordinates $\{t\mid x_{0}\times t\in S\}$ is a nonempty subset of $[0,1)$, bounded below by $0$, so it has a greatest lower bound $y_{0}$, and $x_{0}\times y_{0}$ is a greatest lower bound of $S$: it is a lower bound because every element of $S$ has first coordinate $\ge x_{0}$ with equality only in the fibre over $x_{0}$, and it is the greatest such because any smaller element either has a smaller first coordinate, which is then below some element of $S$ in the fibre, or lies below $x_{0}\times y_{0}$ in the same fibre.

So $X\times[0,1)$ is a linear continuum.
:::
