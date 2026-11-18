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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §3 Exercise 1, printed p. 24, and the three checks and the description of the classes are transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.1, printed p. 19. Each of the three defining properties is one step, and the identification of the classes with the translates $y=x^2+c$ is separated into the class description and the disjointness.
---

::: {.exercise}

Define two points $(x_0, y_0)$ and $(x_1, y_1)$ of the plane to be equivalent if $y_0 - x_0^2 = y_1 - x_1^2$. Check that this is an equivalence relation and describe the equivalence classes.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.1, printed p. 19** (`tmp/sources/munkres-solutions-whitman.pdf`), whose three checks and description of the classes are the steps below; the statement is Munkres, *Topology* (2000), §3 Exercise 1, printed p. 24.

::: pf

::: {.pf-step #reflexive}
$(x_0,y_0)\sim(x_0,y_0)$ for every point of the plane.

::: pf-proof
The two sides of the defining equation are the same number $y_0-x_0^2$.
:::
:::

::: {.pf-step #symmetric}
$(x_0,y_0)\sim(x_1,y_1)$ implies $(x_1,y_1)\sim(x_0,y_0)$.

::: pf-proof
If $y_0-x_0^2=y_1-x_1^2$ then $y_1-x_1^2=y_0-x_0^2$, by symmetry of equality of real numbers.
:::
:::

::: {.pf-step #transitive}
$(x_0,y_0)\sim(x_1,y_1)$ and $(x_1,y_1)\sim(x_2,y_2)$ imply $(x_0,y_0)\sim(x_2,y_2)$.

::: pf-proof
The two hypotheses give $y_0-x_0^2=y_1-x_1^2$ and $y_1-x_1^2=y_2-x_2^2$, so $y_0-x_0^2=y_2-x_2^2$ by transitivity of equality.
:::
:::

::: {.pf-step #equivalence}
$\sim$ is an equivalence relation on the plane.

::: pf-proof
Steps [](#reflexive){.pf-ref}, [](#symmetric){.pf-ref} and [](#transitive){.pf-ref} are the three defining properties.
:::
:::

::: {.pf-step #classes}
The class of $(x_0,y_0)$ is the parabola $\{(x,y)\st y=x^2+c\}$ with $c=y_0-x_0^2$.

::: pf-proof
For a point $(x_1,y_1)$, the condition $(x_1,y_1)\sim(x_0,y_0)$ is $y_1-x_1^2=y_0-x_0^2=c$, that is $y_1=x_1^2+c$. So the class consists exactly of the points of that parabola, and each point of the parabola satisfies the condition.
:::
:::

::: {.pf-step #disjoint}
Distinct classes are disjoint, and every point lies in one.

::: pf-proof
A point $(x,y)$ lies in the class with $c=y-x^2$, so the classes cover the plane. If two classes with parameters $c\neq c'$ shared a point, that point would satisfy $y=x^2+c$ and $y=x^2+c'$, forcing $c=c'$; so distinct classes are disjoint. Thus the classes are the translates $y=x^2+c$ for $c\in\RR$.
:::
:::

::: {.pf-step}
The relation is an equivalence relation and its classes are the parabolas $y=x^2+c$, $c\in\RR$.

::: pf-proof
Steps [](#equivalence){.pf-ref} and [](#classes){.pf-ref} with [](#disjoint){.pf-ref} give both assertions of the exercise.
:::
:::

:::
:::
