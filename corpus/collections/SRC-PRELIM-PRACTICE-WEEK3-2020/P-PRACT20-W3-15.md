---
schema: qual/card@1
id: P-PRACT20-W3-15
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 15"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let \` be the line of intersection for the planes $x + y + z = 3$ and $x - y + z = 5$ . Find the equation for the plane containing (0, 0, 0) and perpendicular to \`.
:::

::: {.solution}
The planes have normal vectors (1, 1, 1) and (1, −1, 1); the line of intersection is normal to both of these so it is parallel to

$$
( 1 , 1 , 1 ) \times ( 1 , - 1 , 1 ) = { \left| \begin{array} { l l l } { { \hat { \mathbf { 1 } } } } & { { \hat { \mathbf { 3 } } } } & { { \hat { \mathbf { k } } } } \\ { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { - 1 } } & { { 1 } } \end{array} \right| } = ( 2 , 0 , - 2 ) .
$$

The new plane must be normal to this and contain zero so it is given by $2 x - 2 z = 0 \implies x = z$
:::
