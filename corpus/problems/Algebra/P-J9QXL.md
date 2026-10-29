---
schema: qual/card@1
id: P-J9QXL
kind: problem
title: The extension $\QQ(2^{1/3})/\QQ$ is not normal
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Is $\QQ(2^{1/3})/\QQ$ normal?
:::

::: {.solution}

::: pf

::: pf-step

$\QQ(2^{1/3})/\QQ$ is $\boxed{\text{not normal}}$.

::: pf-proof

The polynomial $x^3-2$ is irreducible over $\QQ$ by Eisenstein's criterion at $2$, and it has the root $2^{1/3}\in\QQ(2^{1/3})$. Its other roots $\zeta_3 2^{1/3}$ and $\zeta_3^2 2^{1/3}$ are nonreal, while $\QQ(2^{1/3})\subset\RR$. So an irreducible polynomial with a root in $\QQ(2^{1/3})$ does not split there.

:::

:::

:::

:::
