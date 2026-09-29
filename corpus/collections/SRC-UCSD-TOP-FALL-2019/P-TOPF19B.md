---
schema: qual/card@1
id: P-TOPF19B
kind: problem
title: Index-$m$ subgroups of a surface group via covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $G_n$ be the group with generators $\{a_1, a_2, \cdots, a_n, b_1, b_2, \cdots, b_n\}$ and a single relation
$$
a_1 b_1 a_1^{-1} b_1^{-1} a_2 b_2 a_2^{-1} b_2^{-1} \cdots a_n b_n a_n^{-1} b_n^{-1} = 1.
$$
Classify (up to isomorphism) all subgroups of $G_n$ with index $m$.
(Hint: Use the fact that each subgroup of the fundamental group corresponds to a connected covering space.)
:::

::: {.solution}

::: pf

::: pf-step

The group $G_n$ is the fundamental group of the closed orientable surface $\Sigma_n$ of genus $n$.

::: pf-proof

The displayed presentation is the standard polygon presentation of $\pi_1(\Sigma_n)$.

:::

:::

::: {.pf-step #s2}

An index-$m$ subgroup $H\le G_n$ corresponds to a connected $m$-sheeted covering surface $\Sigma_g\to\Sigma_n$.

::: pf-proof

By the subgroup-covering correspondence, index equals the number of sheets. A covering of a closed orientable surface is again a closed orientable surface.

:::

:::

::: {.pf-step #s3}

Euler characteristic gives
$$2-2g=m(2-2n),$$
so
$$g=1+m(n-1).$$

::: pf-proof

Euler characteristic multiplies by the number of sheets of a finite covering.

:::

:::

::: pf-step

Consequently every index-$m$ subgroup is, as an abstract group,
$$\boxed{G_{\,1+m(n-1)}}.$$

::: pf-proof

The subgroup is the fundamental group of the covering surface from step [](#s2){.pf-ref}, whose genus is determined by step [](#s3){.pf-ref}. Thus all such subgroups have the same isomorphism type. Existence follows, for example, from the epimorphism $G_n\to\mathbb Z/m$ sending $a_1\mapsto1$ and all other standard generators to $0$; its kernel has index $m$.

:::

:::

:::

:::
