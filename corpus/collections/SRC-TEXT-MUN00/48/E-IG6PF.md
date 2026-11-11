---
schema: qual/card@1
id: E-IG6PF
kind: problem
title: Powers of the line are Baire spaces in the box, product, and uniform topologies
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 12 (printed p. 300) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book: in the product
    topology the standard nested-basic-open construction works because a basic open set restricts finitely many
    coordinates, each coordinate sequence of closed intervals is nested and eventually constant, and the point
    assembled coordinatewise lies in every closure, hence in every G_n; in the box topology the same
    construction shrinks every coordinate with diameter below 1/n, so each coordinate intersection is a single
    point and the point lies in every closure; in the uniform topology R^J is complete in the uniform metric by
    Theorem 43.5 and so Baire by Theorem 48.2, which is the exercise's point that the box and product topologies
    need a different argument. Nothing needed correction.
---

::: {.exercise}

Show that $\RR^J$ is a Baire space in the box, product, and uniform topologies.
:::

::: {.solution}
For the product topology, let $G_1, G_2, \ldots$ be dense open sets and $U_0$ a nonempty basic open set. Recursively choose nonempty basic opens $U_n$ with
$$
\overline{U_n}\subset U_{n-1}\cap G_n,
$$
changing only finitely many coordinates at stage $n$ and choosing closed bounded coordinate intervals there. In a coordinate that is ever restricted, the first closed bounded interval there is compact, and all later closed intervals are nested inside it, so their intersection is nonempty. Choose any real number in every coordinate never restricted. The resulting point lies in $U_0\cap\bigcap G_n$.

For the box topology, perform the same construction coordinatewise, now shrinking every coordinate interval at stage $n$ and arranging diameter $<1/n$. Completeness of $\RR$ gives a point in every coordinate intersection, hence a point of $U_0\cap\bigcap G_n$.

For the uniform topology, the uniform metric
$$
\bar\rho(x,y)=\sup_{j\in J}\min\{\abs{x_j-y_j},1\}
$$
is complete: a Cauchy sequence is uniformly Cauchy in every coordinate, has coordinatewise limits, and the same uniform estimate gives convergence in $\bar\rho$. Hence the uniform topology is Baire by the complete-metric Baire theorem.

Thus $\RR^J$ is Baire in all three topologies.
:::
