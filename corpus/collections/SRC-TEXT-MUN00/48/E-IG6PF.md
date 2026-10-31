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
