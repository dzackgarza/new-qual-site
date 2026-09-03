---
schema: qual/card@1
id: E-6AOD7
kind: problem
title: Applications of the class equation
classification:
  areas:
  - algebra
  topics:
  - Class Equation
  - p-Groups
  - Abelian Groups
relations: []
review: draft
---

::: {.exercise}
\envlist

- Show that $p$ groups have nontrivial centers.

- Show that groups of order $p^2$ are abelian.
:::

::: {.solution}
$p\dash$groups have nontrivial centers:

- Abusing notation by identifying sets with their cardinalities, the class equation says $G = Z(G) + \sum_{g}' [G: Z(g)]$ where the terms in the sum are all bigger than 1.

- Reducing mod $p$ yields $0 = Z(G) + 0$, since $p$ must divide $[G:Z(g)]$ when $[G:Z(g)] > 1$ because $G = [G:Z(g)]Z(g)$ and $p$ divides the LHS.

- So $p$ divides $Z(G)$, making $Z(G)$ nontrivial.

$p^2$ groups are abelian:

- $Z(G) = 1,p,p^2$, and by above we know $Z(G)\neq 1$.
  If $Z(G) = p^2$ we're done, so assume $Z(G) = p$.

- Then $G/Z(G) = p$ and groups of order $p$ are cyclic, so the $G/Z(G)$ theorem applies and $G$ is abelian.
:::
