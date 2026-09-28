---
schema: qual/card@1
id: P-TOPS11C
kind: problem
title: 'Coverings of a space with $\pi_1\cong(\ZZ/2)^2$'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Assume that $X$ is a path-connected, locally simply-connected space with fundamental group isomorphic to $\mathbb{Z}_2 \times \mathbb{Z}_2$.
How many path-connected covering spaces of $X$ are there, up to equivalence (isomorphism)?
:::

::: {.solution}
<1>1. Connected covering spaces of $X$ up to equivalence correspond to conjugacy classes of subgroups of
$$
\pi_1(X)\cong(\mathbb Z/2)^2.
$$
::: {.proof}
This is the standard classification of connected coverings for path-connected, locally simply-connected spaces.
:::

<1>2. Since the group is abelian, conjugacy classes of subgroups are just subgroups themselves.
::: {.proof}
Every subgroup is fixed under conjugation in an abelian group.
:::

<1>3. The group $(\mathbb Z/2)^2$ has exactly five subgroups: the trivial subgroup, the whole group, and its three distinct subgroups of order $2$.
::: {.proof}
There are three nonzero elements, and each generates a distinct order-$2$ subgroup. There are no other possible subgroup orders by Lagrange's theorem.
:::

<1>4. Hence
$$
\boxed{5}
$$
path-connected covering spaces occur up to equivalence.
::: {.proof}
Apply <1>1--<1>3. The whole group corresponds to the identity cover and the trivial subgroup to the universal cover.
:::
:::
