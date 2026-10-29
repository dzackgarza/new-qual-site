---
schema: qual/card@1
id: P-PFUVL
kind: problem
title: Groups of order four as Galois groups over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Abelian Groups
relations: []
review: draft
---

::: {.problem}
Which groups of order $4$ occur as Galois groups over $\QQ$?
:::

::: {.solution}

::: pf

::: {.pf-step #two-groups}
Up to isomorphism the groups of order $4$ are $C_4$ and $C_2\times C_2$.

::: pf-proof
A group of order $4$ with an element of order $4$ is cyclic. Otherwise every nonidentity element has order $2$, so the group is abelian, and it is $C_2\times C_2$.
:::

:::

::: {.pf-step #cyclic}
$C_4$ occurs.

::: pf-proof
The cyclotomic extension $\QQ(\zeta_5)/\QQ$ is Galois, and
$$\Gal(\QQ(\zeta_5)/\QQ)\cong(\ZZ/5\ZZ)^\times\cong C_4.$$
:::

:::

::: {.pf-step #klein}
$C_2\times C_2$ occurs.

::: pf-proof
The biquadratic extension $\QQ(\sqrt2,\sqrt3)/\QQ$ is the splitting field of $(x^2-2)(x^2-3)$, so it is Galois of degree $4$. Changing the signs of $\sqrt2$ and $\sqrt3$ independently gives four automorphisms, each of order dividing $2$, so
$$\Gal(\QQ(\sqrt2,\sqrt3)/\QQ)\cong C_2\times C_2.$$
:::

:::

::: pf-step
$\boxed{\text{Both groups of order } 4}$ occur as Galois groups over $\QQ$.

::: pf-proof
By step [](#two-groups){.pf-ref} there are no other groups of order $4$, and steps [](#cyclic){.pf-ref} and [](#klein){.pf-ref} realize each of them.
:::

:::

:::

:::
