---
schema: qual/card@1
id: PR-E4T3S
kind: proposition
title: "Classification for quartics"
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - classification
  - polynomials
relations: []
review: draft
---

::: {.proposition title="Classification for quartics"}
The Galois groups of irreducible quartics can be determined using discriminants, resolvents, and checking irreducibility:

- If $\sqrt{\Delta}\in \QQ$, then $G = A_4, C_2^2$.

  - If resolvent is irreducible: $A_4$.
    Otherwise $C_2^2$.

- If $\sqrt{\Delta}\not\in \QQ$ then $G = S_4, D_4, C_4$.

  - Is resolvent is irreducible: $S_4$.
    Otherwise, $D_4$ or $C_4$, argue by cycle types (or if $f$ is irreducible in $\QQ(\sqrt{\Delta})$, $D_4$).

- Summary: ![](../../assets/figures/2021-08-09_14-48-55.png)

A flow chart summarizing the full process:

![](../../assets/figures/2021-07-20_22-06-48.png)

See Hungerford 273 for classification.
:::
