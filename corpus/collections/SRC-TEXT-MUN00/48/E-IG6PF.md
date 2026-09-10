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

Show that $\mathbb{R}^J$ is a Baire space in the box, product, and uniform topologies.
:::

::: {.solution}
For the product topology, $\mathbb R^J$ is a product of completely metrizable spaces. A direct basic-open proof is convenient: given dense open sets $G_n$ and a nonempty basic product-open $U_0$, recursively choose nonempty basic opens $U_n$ with
\[
\overline{U_n}\subset U_{n-1}\cap G_n,
\]
changing only finitely many coordinates at stage $n$ and choosing closed bounded coordinate intervals there. In each coordinate the resulting nested closed intervals have the finite intersection property; choosing one point in every coordinate gives a point of $U_0\cap\bigcap G_n$.

For the box topology, perform the same construction coordinatewise, now shrinking every coordinate interval at stage $n$ and arranging diameter $<1/n$. Completeness of $\mathbb R$ gives a point in every coordinate intersection, hence a point of $U_0\cap\bigcap G_n$.

For the uniform topology, the uniform metric
\[
\bar\rho(x,y)=\sup_{j\in J}\min\{|x_j-y_j|,1\}
\]
is complete: a Cauchy sequence is uniformly Cauchy in every coordinate, has coordinatewise limits, and the same uniform estimate gives convergence in $\bar\rho$. Hence the uniform topology is Baire by the complete-metric Baire theorem.

Thus $\mathbb R^J$ is Baire in all three topologies.
:::
