---
schema: qual/card@1
id: PR-IOMVN
kind: proposition
title: Characteristic subgroups of normal subgroups are normal
slogan: 'Characteristic inside normal is normal in the ambient group.'
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Automorphisms
  - Subgroups
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a group, $H \normal G$ a [[D-EKE4Q|normal subgroup]], and $N \operatorname{char} H$ a [[D-53LTN|characteristic subgroup]] of $H$.
Then $N \normal G$.
:::

::: {.proof}
Let $g \in G$.
Because $H \normal G$, conjugation $\psi_g(h) = ghg^{-1}$ restricts to an automorphism of $H$.
Because $N$ is characteristic in $H$, $\psi_g(N) = N$.
Hence $gNg^{-1} = N$ for every $g \in G$, and $N \normal G$.
:::
