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

::: pf

::: {.pf-step #coverings-correspond-to-subgroups}
Connected covering spaces of $X$ up to equivalence correspond to conjugacy classes of subgroups of
$$
\pi_1(X)\cong(\mathbb Z/2)^2.
$$

::: pf-proof
This is the standard classification of connected coverings for path-connected, locally simply-connected spaces.
:::

:::

::: {.pf-step #abelian-conjugacy-trivial}
Since the group is abelian, conjugacy classes of subgroups are just subgroups themselves.

::: pf-proof
Every subgroup is fixed under conjugation in an abelian group.
:::

:::

::: {.pf-step #five-subgroups}
The group $(\mathbb Z/2)^2$ has exactly five subgroups: the trivial subgroup, the whole group, and its three distinct subgroups of order $2$.

::: pf-proof
There are three nonzero elements, and each generates a distinct order-$2$ subgroup. There are no other possible subgroup orders by Lagrange's theorem.
:::

:::

::: pf-step
Hence
$$
\boxed{5}
$$
path-connected covering spaces occur up to equivalence.

::: pf-proof
Apply steps [](#coverings-correspond-to-subgroups){.pf-ref}, [](#abelian-conjugacy-trivial){.pf-ref} and [](#five-subgroups){.pf-ref}. The whole group corresponds to the identity cover and the trivial subgroup to the universal cover.
:::

:::

:::

:::
