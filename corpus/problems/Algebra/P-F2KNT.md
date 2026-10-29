---
schema: qual/card@1
id: P-F2KNT
kind: problem
title: $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic subfields of $\CC$ that are not equal
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Show that $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic fields but are not identical as subfields of $\CC$.
:::

::: {.solution}
Let
$$
\alpha=2^{1/3},\qquad \beta=\zeta_3\alpha.
$$
Both have irreducible minimal polynomial $x^3-2$, so
$$
\QQ(\alpha)\cong\QQ[x]/(x^3-2)\cong\QQ(\beta).
$$
But $\QQ(\alpha)\subset\RR$ while $\beta$ is nonreal, so the two subfields of $\CC$ are not equal.
:::