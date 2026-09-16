---
schema: qual/card@1
id: D-HWN6T
kind: definition
title: Quasi-isomorphism
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring and $C_\bullet$, $D_\bullet$ chain complexes of $R$-modules.
A [[D-36ONS|chain map]] $f\colon C_\bullet\to D_\bullet$ is a \dfn{quasi-isomorphism} if the induced map $H_n(f)\colon H_n(C_\bullet)\to H_n(D_\bullet)$ is an isomorphism for every $n\in\ZZ$.
:::

::: {.proposition}
Every chain homotopy equivalence is a quasi-isomorphism.
:::

::: {.example}
A quasi-isomorphism need not be a chain homotopy equivalence.
Let $C_\bullet$ be the complex of abelian groups with $C_1 = \ZZ$, $C_0 = \ZZ$, differential $C_1\to C_0$ multiplication by $2$, and all other terms zero, and let $D_\bullet$ be $\ZZ/2$ concentrated in degree $0$.
The reduction map $C_0 = \ZZ\to\ZZ/2 = D_0$ is a chain map inducing an isomorphism $H_0(C_\bullet) = \ZZ/2\to H_0(D_\bullet)$, and all other homology groups vanish, so it is a quasi-isomorphism.
Every chain map $D_\bullet\to C_\bullet$ is zero, since $\Hom(\ZZ/2, \ZZ) = 0$, so it induces the zero map on $H_0$ and cannot be a homotopy inverse.
:::

::: {.remark}
The derived category of $R$-modules is obtained from the category of chain complexes by formally inverting the quasi-isomorphisms.
:::

::: {.concept}
[@Wei94].
:::
