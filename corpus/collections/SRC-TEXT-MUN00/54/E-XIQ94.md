---
schema: qual/card@1
id: E-XIQ94
kind: exercise
title: The order of the rectangles in the lifting-of-homotopies proof
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

In defining the map $\overline{F}$ in the proof of Lemma 54.2, why were we so careful about the order in which we considered the small rectangles?
:::

::: {.solution}
<1>1. Lemma 54.2 is the homotopy lifting property: a homotopy $F: I \times I \to X$ with a lift of $F(-, 0)$ lifts to a homotopy $\overline F: I \times I \to \tilde X$.
::: {.proof}
statement of the lemma.
:::

<1>2. The proof subdivides $I \times I$ into small rectangles and lifts $F$ rectangle by rectangle.
::: {.proof}
the standard proof.
:::

<1>3. The order matters because each rectangle's lift must agree with the lifts already defined on the adjacent rectangles (on their shared edges).
::: {.proof}
the lift on a rectangle is determined by the lift on one of its edges (by the unique lifting property), and to be well-defined and continuous, the lift on each new rectangle must match the previously defined lifts on the shared boundary.
:::

<1>4. Hence the rectangles must be processed in an order such that, when a rectangle is lifted, at least one of its edges (specifically, the edge shared with already-lifted rectangles) already has a lift.
::: {.proof}
this ensures the lift is well-defined and continuous across the whole square.
:::

<1>5. The natural order is to proceed row by row (or column by column), lifting each rectangle using the lift already established on its left and bottom edges.
::: {.proof}
this is the order used in the proof.
:::

<1>6. Q.E.D.
::: {.proof}
<1>3–<1>5.
:::
:::
