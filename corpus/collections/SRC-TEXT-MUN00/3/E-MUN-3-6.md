---
schema: qual/card@1
id: E-MUN-3-6
kind: problem
title: Ordering the plane by the translates of the parabola $y=x^2$
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
    Read against Munkres, Topology (2000), §3 Exercise 6, printed p. 29: (x_0,y_0) <
    (x_1,y_1) if y_0 - x_0^2 < y_1 - x_1^2, or the two are equal and x_0 < x_1; show
    this is an order relation and describe it geometrically. The stored statement
    matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.6,
    printed pp. 25-26 (tmp/sources/munkres-solutions-whitman.pdf). The three properties
    and the geometric description by the level curves y - x^2 = c, with c compared first
    and x breaking ties, are his.
---

::: {.exercise}

Define a relation on the plane by setting
$$
(x_0, y_0) < (x_1, y_1)
$$
if either $y_0 - x_0^2 < y_1 - x_1^2$, or $y_0 - x_0^2 = y_1 - x_1^2$ and $x_0 < x_1$. Show that this is an order relation on the plane, and describe it geometrically.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.6, printed pp. 25--26** (`tmp/sources/munkres-solutions-whitman.pdf`); the three properties and the geometric description are his.

*Comparability.* Let $(x_0,y_0)\ne(x_1,y_1)$. If $y_0-x_0^2\ne y_1-x_1^2$ then one of the two strict inequalities holds and the corresponding point is smaller. So suppose $y_0-x_0^2=y_1-x_1^2$. If also $x_0=x_1$ then $y_0=y_1$, contrary to the two points being distinct; hence $x_0\ne x_1$, and either $x_0<x_1$ or $x_1<x_0$, so the two points are comparable.

*Nonreflexivity.* For any point, $y-x^2=y-x^2$ and yet $x<x$ fails, so $(x,y)<(x,y)$ is false.

*Transitivity.* Suppose $(x_0,y_0)<(x_1,y_1)$ and $(x_1,y_1)<(x_2,y_2)$.
If $y_0-x_0^2<y_1-x_1^2$, then either $y_1-x_1^2<y_2-x_2^2$, giving $y_0-x_0^2<y_2-x_2^2$, or $y_1-x_1^2=y_2-x_2^2$, giving $y_0-x_0^2<y_2-x_2^2$ again; in both cases $(x_0,y_0)<(x_2,y_2)$.
If $y_0-x_0^2=y_1-x_1^2$ and $x_0<x_1$, then the second comparison with $y_1-x_1^2<y_2-x_2^2$ gives $y_0-x_0^2<y_2-x_2^2$, and with $y_1-x_1^2=y_2-x_2^2$ gives $y_0-x_0^2=y_2-x_2^2$ together with $x_0<x_1<x_2$; in both cases $(x_0,y_0)<(x_2,y_2)$.

Geometrically, the level sets of $(x,y)\mapsto y-x^2$ are the translates $y=x^2+c$ of the standard parabola. The order first compares the translate on which a point sits, comparing $c=y-x^2$ as real numbers, and within one translate it compares the horizontal position, the point further to the right being larger. So the plane is ordered like a stack of parabolas, each of which is ordered by its $x$-coordinate.
:::
