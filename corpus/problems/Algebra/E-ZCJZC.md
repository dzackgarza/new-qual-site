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
Show that if $H < G$ is a proper subgroup, then $\Union_{g\in G} gHg\inv \subset G$ is a proper subset.

> Hint: consider the intersection and count.
> Try Orbit-stabilizer?

:::

::: {.solution}
Let $G$ be finite, $m=\size H$, and $n'=[G:H]>1$.

<1>1. $H$ has $n=[G:N_G(H)]\le n'$ distinct conjugates.

::: {.proof}
By orbit-stabilizer for the conjugation action on subgroups, $n=[G:N_G(H)]$, and $H\le N_G(H)$ gives $n\le[G:H]$.
:::

<1>2. $\size \Union_{g\in G} gHg\inv\le 1+n(m-1)$.

::: {.proof}
Each of the $n$ conjugates has $m$ elements, one of which is the identity, and the identity is common to all of them.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2 and Lagrange's theorem $n'm=\size G$,
$$\size \Union_{g\in G} gHg\inv\le 1+n'(m-1)=\size G-(n'-1)<\size G .$$
:::
:::

::: {.remark}
Erratum: the statement needs $G$ finite. Every matrix in $\mathrm{GL}_2(\CC)$ is conjugate to an upper-triangular matrix, so the conjugates of the proper subgroup of invertible upper-triangular matrices cover $\mathrm{GL}_2(\CC)$.
:::

