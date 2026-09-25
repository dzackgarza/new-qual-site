---
schema: qual/card@1
id: T-RLVA4
kind: theorem
title: Correspondence theorem for groups
slogan: 'Subgroups of $G/N$ are exactly the subgroups of $G$ that contain $N$.'
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Normal Subgroups
  - Subgroups
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a group, $N \normal G$ a [[D-EKE4Q|normal subgroup]], and $\pi\colon G\to G/N$ the quotient map.
Then
$$
\theset{H \leq G \suchthat N \subseteq H} \mapstofrom \theset{\overline{H} \suchthat \overline{H} \leq G/N},
\qquad
H \mapsto H/N,
\qquad
\pi^{-1}(\overline{H}) \mapsfrom \overline{H},
$$
are mutually inverse bijections between the subgroups of $G$ containing $N$ and the subgroups of the quotient group $G/N$.
:::
