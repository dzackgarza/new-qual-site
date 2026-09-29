---
schema: qual/card@1
id: E-ZCJZC
kind: problem
title: The union of conjugates of a proper subgroup is a proper subset
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Cosets and Lagrange
relations: []
review: draft
---

::: {.exercise}
Show that if $H < G$ is a proper subgroup, then $\Union_{g\in G} gH\inverseof{g} \subset G$ is a proper subset.

> Hint: consider the intersection and count.
> Try Orbit-stabilizer?

:::

::: {.solution}
Let $G$ be finite, $m=\size H$, and $n'=[G:H]>1$.

::: pf

::: {.pf-step #n-conjugates-bound}
$H$ has $n=[G:N_G(H)]\le n'$ distinct conjugates.

::: pf-proof
By orbit-stabilizer for the conjugation action on subgroups, $n=[G:N_G(H)]$, and $H\le N_G(H)$ gives $n\le[G:H]$.
:::

:::

::: {.pf-step #union-size-bound}
$\size \Union_{g\in G} gH\inverseof{g}\le 1+n(m-1)$.

::: pf-proof
Each of the $n$ conjugates has $m$ elements, one of which is the identity, and the identity is common to all of them.
:::

:::

::: pf-qed
By steps [](#n-conjugates-bound){.pf-ref} and [](#union-size-bound){.pf-ref} and Lagrange's theorem $n'm=\size G$, $$\size \Union_{g\in G} gH\inverseof{g}\le 1+n'(m-1)=\size G-(n'-1)<\size G .$$
:::

:::

:::

::: {.remark}
Erratum: the statement needs $G$ finite.
Every matrix in $\mathrm{GL}_2(\CC)$ is conjugate to an upper-triangular matrix, so the conjugates of the proper subgroup of invertible upper-triangular matrices cover $\mathrm{GL}_2(\CC)$.
:::
