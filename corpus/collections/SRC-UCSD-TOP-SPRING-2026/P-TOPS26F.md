---
schema: qual/card@1
id: P-TOPS26F
kind: problem
title: $S^2 \vee S^1 \vee S^1$ not homotopy equivalent to $S^1 \times S^1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Show that $S^2 \vee S^1 \vee S^1$ is not homotopy equivalent to $S^1 \times S^1$.
:::

::: {.solution}
<1>1. The fundamental group of $S^2\vee S^1\vee S^1$ is the free group $F_2$.
::: {.proof}
The sphere is simply connected, and van Kampen gives the free product of the two circle groups.
:::

<1>2. The fundamental group of $S^1\times S^1$ is $\mathbb Z^2$.
::: {.proof}
Fundamental groups commute with products.
:::

<1>3. These groups are not isomorphic: $F_2$ is nonabelian whereas $\mathbb Z^2$ is abelian.
::: {.proof}
The two free generators of $F_2$ do not commute.
:::

<1>4. Therefore
$$\boxed{S^2\vee S^1\vee S^1\not\simeq S^1\times S^1.}$$
::: {.proof}
Homotopy-equivalent path-connected spaces have isomorphic fundamental groups.
:::
:::
