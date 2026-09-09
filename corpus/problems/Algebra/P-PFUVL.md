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

::: problem
Which groups of order $4$ occur as Galois groups over $\QQ$?
:::

::: {.solution}
Up to isomorphism there are exactly two groups of order $4$:
\[
C_4,\qquad C_2\times C_2.
\]
Both occur over $\QQ$.

<1>1. The cyclic group $C_4$ occurs.
::: {.proof}
The cyclotomic extension
\[
\QQ(\zeta_5)/\QQ
\]
is Galois, and
\[
\operatorname{Gal}(\QQ(\zeta_5)/\QQ)
\cong (\ZZ/5\ZZ)^\times
\cong C_4.
\]
:::

<1>2. The Klein four group occurs.
::: {.proof}
The biquadratic extension
\[
\QQ(\sqrt2,\sqrt3)/\QQ
\]
is Galois. Independently changing the signs of $\sqrt2$ and $\sqrt3$ gives four automorphisms, so
\[
\operatorname{Gal}(\QQ(\sqrt2,\sqrt3)/\QQ)
\cong C_2\times C_2.
\]
:::

Thus every group of order $4$ is realizable as a Galois group over $\QQ$.
:::
