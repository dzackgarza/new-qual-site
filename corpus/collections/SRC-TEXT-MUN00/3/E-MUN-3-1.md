---
schema: qual/card@1
id: E-MUN-3-1
kind: problem
title: Equivalence classes of the relation $y-x^2=\text{const}$ on the plane
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
    Read against Munkres, Topology (2000), §3 Exercise 1, printed p. 28: two points of
    the plane are equivalent if y_0 - x_0^2 = y_1 - x_1^2, and the exercise asks that
    this be checked to be an equivalence relation and its classes described. The stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.1,
    printed p. 19 (tmp/sources/munkres-solutions-whitman.pdf). The three checks and the
    description of the classes as the parabolas y = x^2 + c are his.
---

::: {.exercise}

Define two points $(x_0, y_0)$ and $(x_1, y_1)$ of the plane to be equivalent if $y_0 - x_0^2 = y_1 - x_1^2$. Check that this is an equivalence relation and describe the equivalence classes.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.1, printed p. 19** (`tmp/sources/munkres-solutions-whitman.pdf`); the three checks and the description of the classes are his.

Write $(x_0,y_0)\sim(x_1,y_1)$ when $y_0-x_0^2=y_1-x_1^2$.

*Reflexive.* For every point, $y_0-x_0^2=y_0-x_0^2$, so $(x_0,y_0)\sim(x_0,y_0)$.

*Symmetric.* If $y_0-x_0^2=y_1-x_1^2$, then by symmetry of equality $y_1-x_1^2=y_0-x_0^2$, so $(x_1,y_1)\sim(x_0,y_0)$.

*Transitive.* If $y_0-x_0^2=y_1-x_1^2$ and $y_1-x_1^2=y_2-x_2^2$, then $y_0-x_0^2=y_2-x_2^2$ by transitivity of equality, so $(x_0,y_0)\sim(x_2,y_2)$.

Hence $\sim$ is an equivalence relation. Its classes are the parabolas $y=x^2+c$: a point $(x_0,y_0)$ lies in the class of the points with $y-x^2=c$ exactly when $y_0=x_0^2+c$, that is when it lies on that parabola. Two points are equivalent precisely when they lie on the same one of these translates of $y=x^2$, and distinct translates are disjoint.
:::
