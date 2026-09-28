---
schema: qual/card@1
id: PR-GJLQP
kind: proposition
title: The center is a characteristic subgroup
slogan: 'Every automorphism preserves the center.'
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Automorphisms
  - Subgroups
relations: []
review: draft
---

::: {.proposition}
For every group $G$, the [[D-NK7G7|center]] $Z(G)$ is a [[D-53LTN|characteristic subgroup]] of $G$, $Z(G) \ch G$.
:::

::: {.proof}
Let $\phi \in \Aut(G)$, $z \in Z(G)$, and $g \in G$.
Then $\phi(z)\,g = \phi\big(z\,\inverseof{\phi}(g)\big) = \phi\big(\inverseof{\phi}(g)\,z\big) = g\,\phi(z)$, so $\phi(z) \in Z(G)$.
:::
