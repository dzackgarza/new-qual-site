---
schema: qual/card@1
id: E-6AOD7
kind: exercise
title: "Applications of the class equation"
classification:
  areas:
  - algebra
  topics:
  - class-equation
  - p-groups
  - abelian-groups
relations: []
review: draft
solved: true
---

::: {.exercise title="Applications of the class equation"}
\envlist

- Show that $p$ groups have nontrivial centers.

- Show that groups of order $p^2$ are abelian.
:::

::: {.solution}
$p\dash$groups have nontrivial centers:

- Abusing notation by identifying sets with their cardinalities, the class equation says $G = Z(G) + \sum_{g}' [G: Z(g)]$ where the terms in the sum are all bigger than 1.

- Reducing mod $p$ yields $0 = Z(g) + 0$, since $p$ must divide $[G:Z(g)]$ when $[G:Z(g)] > 1$ because $G = [G:Z(g)]Z(g)$ and $p$ divides the LHS.

- So $p$ divides $Z(g)$, making $Z(g)$ nontrivial.

$p^2$ groups are abelian:

- $Z(G) = 1,p,p^2$, and by above we know $Z(G)\neq 1$.
  If $Z(G) = p^2$ we're done, so assume $Z(G) = p$.

- Then $G/Z(G) = p$ and groups of order $p$ are cyclic, so the $G/Z(G)$ theorem applies and $G$ is abelian.
:::
